"""Compare command-line argument quoting without executing any command."""
from __future__ import annotations
import argparse
import shlex


def posix_quote(value: str) -> str:
    return shlex.quote(value)


def powershell_quote(value: str) -> str:
    """Return a single-quoted PowerShell literal; embedded quotes are doubled."""
    return "'" + value.replace("'", "''") + "'"


def windows_quote(value: str) -> str:
    """Quote one argv item using the CommandLineToArgvW backslash rules."""
    if value and not any(ch in value for ch in ' \t\n\v"'):
        return value
    out = ['"']
    slashes = 0
    for ch in value:
        if ch == "\\":
            slashes += 1
        elif ch == '"':
            out.append("\\" * (slashes * 2 + 1))
            out.append('"')
            slashes = 0
        else:
            out.append("\\" * slashes)
            out.append(ch)
            slashes = 0
    out.append("\\" * (slashes * 2))
    out.append('"')
    return "".join(out)


def render(values: list[str]) -> str:
    rows = [
        ("POSIX shell", " ".join(posix_quote(v) for v in values)),
        ("PowerShell", " ".join(powershell_quote(v) for v in values)),
        ("Windows argv", " ".join(windows_quote(v) for v in values)),
    ]
    width = max(len(name) for name, _ in rows)
    return "\n".join(f"{name:<{width}}  {command}" for name, command in rows)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--arg", action="append", dest="values",
                        help="Argument to quote (repeat for multiple arguments).")
    parser.add_argument("--demo", action="store_true", help="Use a small example set.")
    args = parser.parse_args(argv)
    values = args.values or (["hello world", "it's fine", "C:\\Program Files\\Tool\\"] if args.demo else [])
    if not values:
        parser.error("provide one or more --arg values, or use --demo")
    print(render(values))
    print("\nNo command was executed. Review the output before using it.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:38bdf8&height=180&section=header&text=shell-quote-lab&fontSize=42&fontColor=ffffff&animation=fadeIn" alt="Shell Quote Lab banner" width="100%"/>

<a href="https://github.com/CyberLoop-dev/shell-quote-lab">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1100&color=38bdf8&center=true&vCenter=true&width=720&lines=Shell%20Quote%20Lab;Small+tools.+Clear+feedback.+Local+first." alt="Typing title"/>
</a>

<p><strong>Compare command-argument quoting for POSIX shells, PowerShell, and Windows command lines without executing commands.</strong></p>

[![License](https://img.shields.io/github/license/CyberLoop-dev/shell-quote-lab)](LICENSE)
[![Language](https://img.shields.io/github/languages/top/CyberLoop-dev/shell-quote-lab)](https://github.com/CyberLoop-dev/shell-quote-lab)
[![Stars](https://img.shields.io/github/stars/CyberLoop-dev/shell-quote-lab?style=flat)](https://github.com/CyberLoop-dev/shell-quote-lab/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/CyberLoop-dev/shell-quote-lab)](https://github.com/CyberLoop-dev/shell-quote-lab/commits/main)

<img src="assets/overview.svg" alt="Shell Quote Lab project illustration" width="100%"/>

</div>

## ✨ Overview

Compare command-argument quoting for POSIX shells, PowerShell, and Windows command lines without executing commands. **Shell Quote Lab** is a small Python command-line tool built with the standard library. It is designed for local use and keeps its behavior explicit.

## 🚀 Features

- ✨ 🧩 Compare POSIX, PowerShell, and Windows argument quoting.
- ✨ 🧪 Handle spaces, apostrophes, quotes, and trailing backslashes.
- ✨ 🛡️ Generate text only; no shell command is executed.
- ✨ 🧾 Review all target formats side by side.

## 🖥️ Demo

```bash
python main.py --demo
```

The demo prints equivalent quoting examples for POSIX shells, PowerShell, and Windows argv rules. It never executes the generated command.

## ⚡ Quick Start

```bash
python main.py --demo
```

Python 3.10 or newer is required. No third-party packages are needed.

## 🧰 Tech Stack

- **Language:** Python 3.10+
- **Libraries:** Python standard library
- **Dependencies:** None

## 📁 Folder Structure

```text
shell-quote-lab/
├── assets/overview.svg
├── tests/test_main.py
├── main.py
├── pyproject.toml
├── .gitignore
├── LICENSE
└── README.md
```

## 🗺️ Roadmap

- [ ] Add a JSON output mode for tooling integrations.
- [ ] Add more edge-case fixtures for platform-specific quoting.

## 🤝 Contributing

Issues and pull requests are welcome. Include a minimal input example, expected behavior, and a regression test when changing parsing or quoting rules.

## 📄 License

Released under the [MIT License](LICENSE).

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:38bdf8,100:0f172a&height=110&section=footer" alt="Animated wave footer" width="100%"/>
</div>

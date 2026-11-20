import unittest
from main import posix_quote, powershell_quote, windows_quote, render


class QuoteTests(unittest.TestCase):
    def test_posix_spaces(self):
        self.assertEqual(posix_quote("hello world"), "'hello world'")

    def test_powershell_single_quote(self):
        self.assertEqual(powershell_quote("it's fine"), "'it''s fine'")

    def test_windows_empty_and_spaces(self):
        self.assertEqual(windows_quote(""), '""')
        self.assertEqual(windows_quote("hello world"), '"hello world"')

    def test_render_has_three_targets(self):
        result = render(["a b"])
        self.assertIn("POSIX shell", result)
        self.assertIn("PowerShell", result)
        self.assertIn("Windows argv", result)


if __name__ == "__main__":
    unittest.main()

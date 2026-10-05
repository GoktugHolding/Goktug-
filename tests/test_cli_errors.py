import contextlib
import io
import tempfile
import unittest
from pathlib import Path

from goktug.cli import build_parser
from goktug.package_manager import build_parser as package_parser
from goktug.runtime import format_error, run_file


class CliAndErrorTests(unittest.TestCase):
    def test_cli_version_argument(self):
        parser = build_parser()
        output = io.StringIO()
        with contextlib.redirect_stdout(output), self.assertRaises(SystemExit) as caught:
            parser.parse_args(['--version'])
        self.assertEqual(caught.exception.code, 0)
        self.assertIn('Goktug+ 1.0.0', output.getvalue())

    def test_package_help_and_alias(self):
        args = package_parser().parse_args(['yukle', 'gorsel-paketi'])
        self.assertEqual(args.command, 'yukle')
        self.assertEqual(args.paketler, ['gorsel-paketi'])

    def test_help_headings_are_turkish(self):
        help_text = build_parser().format_help()
        self.assertIn('Kullanım:', help_text)
        self.assertIn('Seçenekler:', help_text)
        self.assertNotIn('options:', help_text)

    def test_run_tpg_file(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'merhaba.tpg'
            path.write_text('yazdir("Merhaba")\n', encoding='utf-8')
            stdout = io.StringIO()
            with contextlib.redirect_stdout(stdout):
                status = run_file(path)
            self.assertEqual(status, 0)
            self.assertEqual(stdout.getvalue(), 'Merhaba\n')

    def test_runtime_error_is_localized_and_points_to_file(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'hata.tpg'
            path.write_text('deger = 2\nyazdir(bulunmayan_ad)\n', encoding='utf-8')
            stderr = io.StringIO()
            with contextlib.redirect_stderr(stderr):
                status = run_file(path)
            self.assertEqual(status, 1)
            self.assertIn('İsim Hatası', stderr.getvalue())
            self.assertIn('hata.tpg:2', stderr.getvalue())
            self.assertNotIn('Traceback', stderr.getvalue())

    def test_syntax_error_localized(self):
        message = format_error(SyntaxError('invalid syntax', ('main.tpg', 3, 5, 'eger :')), 'main.tpg')
        self.assertIn('Sözdizimi Hatası', message)
        self.assertIn('main.tpg:3:5', message)

    def test_wrong_extension_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'program.py'
            path.write_text('pass')
            stderr = io.StringIO()
            with contextlib.redirect_stderr(stderr):
                status = run_file(path)
            self.assertEqual(status, 2)
            self.assertIn('.tpg', stderr.getvalue())


if __name__ == '__main__':
    unittest.main()

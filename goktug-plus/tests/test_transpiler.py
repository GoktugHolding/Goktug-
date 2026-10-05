import unittest
import contextlib
import io

from goktug.transpiler import translate


class TranspilerTests(unittest.TestCase):
    def test_translates_keywords_and_builtins(self):
        result = translate('eger Dogru: yazdir(aralik(3))\n')
        self.assertIn('if True', result.source)
        self.assertIn('print', result.source)
        self.assertIn('range', result.source)
        compile(result.source, '<test>', 'exec')

    def test_does_not_change_strings_or_comments(self):
        source = '# yazdir eger\nmetin = "yazdir eger"\nyazdir(metin)\n'
        result = translate(source).source
        self.assertIn('# yazdir eger', result)
        self.assertIn('"yazdir eger"', result)
        self.assertIn('print', result)

    def test_unicode_identifiers_are_retained(self):
        code = translate('öğrenci = "Çağrı"\nyazdir(öğrenci)\n').source
        namespace = {}
        with contextlib.redirect_stdout(io.StringIO()):
            exec(compile(code, '<test>', 'exec'), namespace)
        self.assertEqual(namespace['öğrenci'], 'Çağrı')

    def test_stdlib_and_attribute_aliases(self):
        code = translate('iceaktar matematik\nsonuc = matematik.karekok(25)\n').source
        self.assertIn('import math', code)
        self.assertIn('sqrt', code)
        namespace = {}
        exec(compile(code, '<test>', 'exec'), namespace)
        self.assertEqual(namespace['sonuc'], 5.0)

    def test_token_output_compiles_with_expanded_alias(self):
        code = translate('ile(ac("x")) olarak f:\n    gec\n').source
        compile(code, '<test>', 'exec')

    def test_iterator_builtin_aliases_execute(self):
        code = translate('sonuc = uzunluk(liste(suz(lambda n: n > 3, aralik(6))))\n').source
        namespace = {}
        exec(compile(code, '<test>', 'exec'), namespace)
        self.assertEqual(namespace['sonuc'], 2)


if __name__ == '__main__':
    unittest.main()

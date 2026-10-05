import unittest

from goktug.transpiler import translate


def execute(source):
    namespace = {}
    compiled = compile(translate(source).source, '<goktug-test>', 'exec')
    exec(compiled, namespace, namespace)
    return namespace


class LanguageFeatureTests(unittest.TestCase):
    def test_control_flow_and_recursion(self):
        ns = execute('''fonksiyon faktoriyel(n):
    eger n <= 1:
        dondur 1
    dondur n * faktoriyel(n - 1)
sonuc = faktoriyel(5)
''')
        self.assertEqual(ns['sonuc'], 120)

    def test_class_and_inheritance(self):
        ns = execute('''sinif Kisi:
    fonksiyon __init__(kendim, ad):
        kendim.ad = ad
sinif Ogrenci(Kisi):
    gec
nesne = Ogrenci("Ada")
sonuc = nesne.ad
''')
        self.assertEqual(ns['sonuc'], 'Ada')

    def test_comprehension_lambda_and_dict(self):
        ns = execute('''degerler = [x * 2 icin x icinde aralik(4)]
artir = lambda x: x + 1
map_degerleri = {x: artir(x) icin x icinde aralik(3)}
''')
        self.assertEqual(ns['degerler'], [0, 2, 4, 6])
        self.assertEqual(ns['map_degerleri'], {0: 1, 1: 2, 2: 3})

    def test_generator_and_exception(self):
        ns = execute('''fonksiyon sayilar():
    uret 4
    uret 9
sonuc = list(sayilar())
dene:
    1 / 0
hata_yakala ZeroDivisionError:
    yakalandi = Dogru
''')
        self.assertEqual(ns['sonuc'], [4, 9])
        self.assertTrue(ns['yakalandi'])

    def test_annotations_and_decorator(self):
        ns = execute('''@staticmethod
fonksiyon sabit(x: int) -> int:
    dondur x
sonuc = sabit(7)
''')
        self.assertEqual(ns['sonuc'], 7)

    def test_async_await_native_features(self):
        ns = execute('''asenkron fonksiyon al():
    bekle __import__("asyncio").sleep(0)
    dondur 42
sonuc = __import__("asyncio").run(al())
''')
        self.assertEqual(ns['sonuc'], 42)

    def test_turkish_pattern_matching_aliases(self):
        ns = execute('''deger = 2
eslestir deger:
    eslesme 2:
        sonuc = "ikili"
    eslesme _:
        sonuc = "diger"
''')
        self.assertEqual(ns['sonuc'], 'ikili')


if __name__ == '__main__':
    unittest.main()

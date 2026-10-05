"""Goktug+ sözcük eşlemeleri. Eşlemeler yalnızca kaynak kodu NAME tokenlarında uygulanır."""

KEYWORDS = {
    "eger": "if", "degilseeger": "elif", "degilse": "else",
    "icin": "for", "iken": "while", "icinde": "in",
    "degil": "not", "ve": "and", "veya": "or",
    "Dogru": "True", "Yanlis": "False", "Hic": "None",
    "fonksiyon": "def", "dondur": "return", "sinif": "class",
    "iceaktar": "import", "den": "from", "olarak": "as",
    "dene": "try", "hata_yakala": "except", "sonunda": "finally",
    "hata_olustur": "raise", "gec": "pass", "dur": "break",
    "devam": "continue", "uret": "yield", "asenkron": "async",
    "bekle": "await", "ile": "with", "dogrula": "assert",
    "sil": "del", "genel": "global", "yerel_olmayan": "nonlocal",
    "ayni": "is", "islev": "lambda", "eslestir": "match",
    "eslesme": "case",
}

BUILTINS = {
    "yazdir": "print", "girdi": "input", "aralik": "range",
    "uzunluk": "len", "tip": "type", "donustur": "str",
    "tamsayi": "int", "ondalik": "float", "liste": "list",
    "demet": "tuple", "sozluk": "dict", "kume": "set",
    "mantiksal": "bool", "mutlak": "abs", "en_buyuk": "max",
    "en_kucuk": "min", "toplam": "sum", "sirala": "sorted",
    "ters": "reversed", "say": "enumerate", "birlesik": "zip",
    "herhangi": "any", "tum": "all", "yardim": "help",
    "kimlik": "id", "karakter": "chr", "kod": "ord",
    "bicim": "format", "yuvarla": "round", "bolum_kalan": "divmod",
    "bayt": "bytes", "bayt_dizisi": "bytearray", "karmasik": "complex",
    "sabit_kume": "frozenset", "bellek_gorunumu": "memoryview",
    "nesne_taban": "object", "dilim": "slice", "yineleyici": "iter",
    "sonraki": "next", "esle_her_birine": "map", "suz": "filter",
    "temsili": "repr", "ascii_gosterim": "ascii", "ikili_yazim": "bin",
    "sekizlik_yazim": "oct", "onaltilik_yazim": "hex",
    "cagrilabilir_mi": "callable", "adlar": "dir", "ozellik_al": "getattr",
    "ozellik_ata": "setattr", "ozellik_var_mi": "hasattr",
    "ozellik_sil": "delattr", "degiskenler": "vars",
    "genel_degiskenler": "globals", "yerel_degiskenler": "locals",
    "duraklat": "breakpoint",
    "ac": "open", "super_sinif": "super", "ozellik": "property",
    "statik_yontem": "staticmethod", "sinif_yontem": "classmethod",
    "isinstance_mi": "isinstance", "alt_sinif_mi": "issubclass",
    "derle": "compile", "degerlendir": "eval", "calistir": "exec",
    "istisna": "Exception", "deger_hatasi": "ValueError",
    "isim_hatasi": "NameError", "tip_hatasi": "TypeError",
    "anahtar_hatasi": "KeyError", "dizin_hatasi": "IndexError",
    "calisma_hatasi": "RuntimeError", "dogrulama_hatasi": "AssertionError",
    "sifira_bolme_hatasi": "ZeroDivisionError", "durdurma_hatasi": "StopIteration",
    "ice_aktarim_hatasi": "ImportError", "dosya_bulunamadi": "FileNotFoundError",
}

# Kullanıcı dostu stdlib adları. Aynı eşlemeler noktalı kullanımda ve importta geçerlidir.
MODULES = {
    "matematik": "math", "rastgele": "random", "zaman": "time",
    "tarih": "datetime", "json": "json", "isletim": "os",
    "sistem": "sys", "yol": "pathlib", "duzenli_ifade": "re",
    "istatistik": "statistics", "koleksiyonlar": "collections",
    "is_parcalari": "threading", "surecler": "multiprocessing",
    "alt_surec": "subprocess", "soket": "socket", "url": "urllib",
    "csv": "csv", "veri_sikistirma": "zipfile", "dosya": "io",
    "asenkron_io": "asyncio", "veri_siniflari": "dataclasses",
    "sayim": "itertools", "islevler": "functools", "operator": "operator",
    "gunluk": "logging", "argumanlar": "argparse", "test": "unittest",
}

# Math dahil yaygın modüllerin Türkçe fonksiyon adları. Anahtar sözcüklerle çakışmaz.
ATTRIBUTES = {
    "karekok": "sqrt", "kuvvet": "pow", "sinus": "sin", "kosinus": "cos",
    "tanjant": "tan", "radyan": "radians", "derece": "degrees",
    "rastgele_sayi": "randint", "sec": "choice", "karistir": "shuffle",
    "simdi": "now", "bugun": "today", "uyku": "sleep",
    "dosya_yolu": "Path", "dosya_oku": "read_text", "dosya_yaz": "write_text",
    "eslestir": "match", "tam_eslestir": "fullmatch", "degistir": "sub",
    "kok": "root", "uzanti": "suffix", "ad": "name",
}

# All currently reserved spellings, exported for help and documentation.
ALL_WORDS = {**KEYWORDS, **BUILTINS, **MODULES, **ATTRIBUTES}

"""Goktug+ kaynaklarını derleyip çalıştıran çalışma zamanı."""
from __future__ import annotations

import os
import sys
import tokenize
import traceback
from pathlib import Path

from .transpiler import translate

ERROR_NAMES = {
    "SyntaxError": "Sözdizimi Hatası", "IndentationError": "Girinti Hatası",
    "TokenError": "Sözdizimi Hatası",
    "TabError": "Girinti Hatası", "NameError": "İsim Hatası",
    "TypeError": "Tür Hatası", "ValueError": "Değer Hatası",
    "ZeroDivisionError": "Sıfıra Bölme Hatası", "IndexError": "Dizin Hatası",
    "KeyError": "Anahtar Hatası", "AttributeError": "Özellik Hatası",
    "FileNotFoundError": "Dosya Bulunamadı", "ImportError": "Modül Yükleme Hatası",
    "ModuleNotFoundError": "Modül Bulunamadı", "AssertionError": "Doğrulama Hatası",
    "RuntimeError": "Çalışma Hatası", "PermissionError": "İzin Hatası",
    "OSError": "İşletim Sistemi Hatası", "Exception": "Program Hatası",
}


def format_error(exc: BaseException, filename: str) -> str:
    """Python traceback'i göstermeden kaynak konumlu, Türkçe hata üretir."""
    label = ERROR_NAMES.get(type(exc).__name__, "Program Hatası")
    line = getattr(exc, "lineno", None)
    column = getattr(exc, "offset", None)
    if isinstance(exc, tokenize.TokenError) and len(exc.args) > 1:
        token_location = exc.args[1]
        if isinstance(token_location, tuple) and len(token_location) == 2:
            line, column = token_location
    if line is None:
        tb = traceback.extract_tb(exc.__traceback__)
        candidates = [frame for frame in tb if frame.filename == filename]
        if candidates:
            line = candidates[-1].lineno
    location = filename
    if line:
        location += f":{line}"
        if column:
            location += f":{column}"
    detail = str(exc).strip()
    if isinstance(exc, NameError):
        missing = getattr(exc, "name", None)
        detail = f"'{missing}' adlı ad veya değişken bulunamadı." if missing else "Kullanılan ad bulunamadı."
    elif isinstance(exc, tokenize.TokenError):
        detail = str(exc.args[0]) if exc.args else "Kaynak kod çözümlenemedi."
        detail = detail.replace("EOF in multi-line string", "çok satırlı metin sabiti tamamlanmadı")
        detail = detail.replace("EOF in multi-line statement", "kaynak dosyası beklenmedik yerde bitti")
    elif isinstance(exc, SyntaxError):
        detail = exc.msg or "Kaynak kod çözümlenemedi."
        detail = detail.replace("invalid syntax", "geçersiz sözdizimi")
        detail = detail.replace("unexpected indent", "beklenmeyen girinti")
        detail = detail.replace("expected an indented block", "girintili bir kod bloğu bekleniyordu")
    elif isinstance(exc, ModuleNotFoundError):
        name = getattr(exc, "name", None)
        detail = f"'{name}' modülü bulunamadı; gerekli paketin kurulu olduğunu kontrol edin."
    elif isinstance(exc, TypeError):
        detail = detail.replace("'str'", "'metin'").replace("'int'", "'tamsayı'").replace("'list'", "'liste'")
    return f"{label}:\n{location}\n\n{detail}"


def run_file(path: str | os.PathLike[str], argv: list[str] | None = None) -> int:
    """Bir .tpg dosyasını çalıştır. Başarıda 0, program hatasında 1 döndürür."""
    source_path = Path(path).expanduser().resolve()
    if not source_path.is_file():
        print(f"Dosya Bulunamadı:\n{path}\n\nBelirtilen kaynak dosya mevcut değil.", file=sys.stderr)
        return 2
    if source_path.suffix.lower() != ".tpg":
        print("Dosya Türü Hatası:\nGoktug+ kaynak dosyalarının uzantısı .tpg olmalıdır.", file=sys.stderr)
        return 2
    try:
        with tokenize.open(source_path) as handle:
            source = handle.read()
        translated = translate(source)
        code = compile(translated.source, str(source_path), "exec")
        namespace = {
            "__name__": "__main__", "__file__": str(source_path),
            "__package__": None, "__cached__": None,
        }
        sys.path.insert(0, str(source_path.parent))
        previous_argv = sys.argv[:]
        sys.argv = [str(source_path)] + (argv or [])
        try:
            exec(code, namespace, namespace)
        finally:
            sys.argv = previous_argv
            try:
                sys.path.remove(str(source_path.parent))
            except ValueError:
                pass
        return 0
    except (KeyboardInterrupt, SystemExit):
        raise
    except (Exception, tokenize.TokenError, IndentationError) as exc:
        print(format_error(exc, str(source_path)), file=sys.stderr)
        return 1

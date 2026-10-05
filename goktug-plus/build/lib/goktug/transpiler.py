"""Token tabanlı Goktug+ kaynak dönüştürücüsü.

Metin sabitleri ve yorumlar tokenize edilip NAME tokenları dışında bırakılır.
Token çiftleriyle yeniden yazım, Türkçe ve çalışma zamanı sözcük uzunlukları
farklı olsa bile güvenlidir; NEWLINE/INDENT tokenları kaynak satırlarını korur.
"""
from __future__ import annotations

import io
import tokenize
from dataclasses import dataclass

from .mappings import ATTRIBUTES, BUILTINS, KEYWORDS, MODULES


@dataclass(frozen=True)
class Translation:
    source: str
    line_map: tuple[int, ...]


def translate(source: str) -> Translation:
    """Goktug+ kodunu çalışma zamanı koduna çevirir; satır eşlemesini saklar."""
    tokens = list(tokenize.generate_tokens(io.StringIO(source).readline))
    converted: list[tuple[int, str]] = []
    names = {**KEYWORDS, **BUILTINS, **MODULES, **ATTRIBUTES, "kendim": "self"}
    for token in tokens:
        spelling = names.get(token.string, token.string) if token.type == tokenize.NAME else token.string
        converted.append((token.type, spelling))
    line_map = tuple(range(1, source.count("\n") + 2))
    return Translation(tokenize.untokenize(converted), line_map)


def translated_names() -> dict[str, str]:
    """Tanımlı Türkçe→çalışma zamanı sözcük eşlemelerinin kopyasını döndürür."""
    return {**KEYWORDS, **BUILTINS, **MODULES, **ATTRIBUTES, "kendim": "self"}

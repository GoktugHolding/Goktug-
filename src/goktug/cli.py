"""Goktug+ komut satırı çalıştırıcısı."""
from __future__ import annotations

import argparse
import sys

from . import __version__
from .arguments import TurkishArgumentParser
from .runtime import run_file


def build_parser() -> argparse.ArgumentParser:
    parser = TurkishArgumentParser(
        prog="trp", description="Goktug+ Komut Satırı Aracı",
        usage="trp [seçenekler] dosya.tpg [program argümanları]",
    )
    parser.add_argument("--version", "-v", action="version", version=f"Goktug+ {__version__}",
                        help="Sürüm bilgisini göster ve çık")
    parser.add_argument("dosya", nargs="?", help="Çalıştırılacak .tpg kaynak dosyası")
    parser.add_argument("argumanlar", nargs=argparse.REMAINDER, help="Programa aktarılacak ek argümanlar")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    if not args.dosya:
        parser.print_help()
        return 0
    return run_file(args.dosya, args.argumanlar)


if __name__ == "__main__":
    sys.exit(main())

"""TPG Paket Yöneticisi; paket işlemlerini kurulu ortamın standart paket aracına iletir."""
from __future__ import annotations

import subprocess
import sys

from .arguments import TurkishArgumentParser


def build_parser() -> TurkishArgumentParser:
    parser = TurkishArgumentParser(prog="tpg", description="TPG Paket Yöneticisi")
    sub = parser.add_subparsers(dest="command", parser_class=TurkishArgumentParser,
                                title="Paket işlemleri")
    install = sub.add_parser("yukle", aliases=["install"], help="Paket yükle", description="Bir veya daha fazla paket yükle")
    install.add_argument("paketler", nargs="+", help="Yüklenecek paket adları")
    remove = sub.add_parser("kaldir", aliases=["uninstall", "remove"], help="Paket kaldır", description="Bir veya daha fazla paketi kaldır")
    remove.add_argument("paketler", nargs="+", help="Kaldırılacak paket adları")
    update = sub.add_parser("guncelle", aliases=["update"], help="Paket güncelle", description="Belirtilen paketleri güncelle")
    update.add_argument("paketler", nargs="+", help="Güncellenecek paket adları")
    sub.add_parser("liste", aliases=["list"], help="Kurulu paketleri listele", description="Kurulu paketleri göster")
    sub.add_parser("yardim", aliases=["help"], help="Bu yardım ekranını göster", description="TPG komut yardımı")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    if args.command in (None, "yardim", "help"):
        parser.print_help()
        return 0
    if args.command in ("yukle", "install"):
        command = [sys.executable, "-m", "pip", "install", *args.paketler]
    elif args.command in ("kaldir", "uninstall", "remove"):
        command = [sys.executable, "-m", "pip", "uninstall", "-y", *args.paketler]
    elif args.command in ("guncelle", "update"):
        command = [sys.executable, "-m", "pip", "install", "--upgrade", *args.paketler]
    elif args.command in ("liste", "list"):
        command = [sys.executable, "-m", "pip", "list"]
    else:
        parser.error("Bilinmeyen işlem")
    try:
        return subprocess.run(command, check=False).returncode
    except OSError as exc:
        print(f"Paket İşlemi Hatası: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

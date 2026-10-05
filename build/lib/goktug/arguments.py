"""Türkçe kullanıcı arayüzlü argüman ayrıştırıcısı."""
from __future__ import annotations

import argparse


class TurkishArgumentParser(argparse.ArgumentParser):
    """Argparse davranışını korurken yardım/usage metinlerini Türkçeleştirir."""

    def __init__(self, *args, **kwargs):
        kwargs["add_help"] = False
        super().__init__(*args, **kwargs)
        self._positionals.title = "Argümanlar"
        self._optionals.title = "Seçenekler"
        self.add_argument("-h", "--help", action="help", help="Bu yardım ekranını göster")

    def format_help(self) -> str:
        return super().format_help().replace("usage:", "Kullanım:").replace(
            "show this help message and exit", "Bu yardım ekranını göster ve çık"
        ).replace("show program's version number and exit", "Sürüm bilgisini göster ve çık")

    def format_usage(self) -> str:
        return super().format_usage().replace("usage:", "Kullanım:")

    def error(self, message: str) -> None:
        message = message.replace("unrecognized arguments", "tanınmayan argümanlar")
        message = message.replace("the following arguments are required", "şu argümanlar gerekli")
        super().error(message)

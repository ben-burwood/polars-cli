from enum import StrEnum, auto
from typing import Self


class FileType(StrEnum):
    """Polars supported File"""

    CSV = auto()
    PARQUET = auto()
    JSON = auto()

    @property
    def file_extension(self) -> str:
        return f".{self.name.lower()}"

    @classmethod
    def from_extension(cls, extension: str) -> Self:
        return cls[extension.lstrip(".").upper()]

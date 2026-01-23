import polars as pl

from polars_cli.io.filetype import FileType


def scan_file(filepath: str) -> pl.LazyFrame:
    """Scan File into a Polars LazyFrame"""
    extension = filepath.split(".")[-1]
    match FileType.from_extension(extension):
        case FileType.CSV:
            return pl.scan_csv(filepath)
        case FileType.PARQUET:
            return pl.scan_parquet(filepath)
        case _:
            raise ValueError(f"Unsupported file type: {extension} for Scan")


def read_file(filepath: str) -> pl.DataFrame:
    """Read File into a Polars DataFrame"""
    extension = filepath.split(".")[-1]
    match FileType.from_extension(extension):
        case FileType.CSV:
            return pl.read_csv(filepath)
        case FileType.PARQUET:
            return pl.read_parquet(filepath)
        case FileType.JSON:
            return pl.read_json(filepath)
        case _:
            raise ValueError(f"Unsupported file type: {extension} for Read")

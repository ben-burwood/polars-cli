import polars as pl

from polars_cli.io.filetype import FileType


def _scan_file(filepath: str) -> pl.LazyFrame:
    """Scan File into a Polars LazyFrame"""
    extension = filepath.split(".")[-1]
    match FileType.from_extension(extension):
        case FileType.CSV:
            return pl.scan_csv(filepath)
        case FileType.PARQUET:
            return pl.scan_parquet(filepath)
        case _:
            raise ValueError(f"Unsupported file type: {extension} for Scan")


def _read_file(filepath: str) -> pl.DataFrame:
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


def input_file(filepath: str, lazy: bool = True) -> pl.DataFrame | pl.LazyFrame:
    if lazy:
        return _scan_file(filepath)
    else:
        return _read_file(filepath)

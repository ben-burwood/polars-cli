import polars as pl

from polars_cli.io.filetype import FileType


def sink_file(df: pl.LazyFrame, filepath: str) -> None:
    """Sink Polars LazyFrame to File"""
    extension = filepath.split(".")[-1]
    match FileType.from_extension(extension):
        case FileType.CSV:
            return df.sink_csv(filepath)
        case FileType.PARQUET:
            return df.sink_parquet(filepath)
        case _:
            raise ValueError(f"Unsupported file type: {extension} for Scan")


def write_file(df: pl.DataFrame, filepath: str) -> None:
    """Write Polars DataFrame to File"""
    extension = filepath.split(".")[-1]
    match FileType.from_extension(extension):
        case FileType.CSV:
            return df.write_csv(filepath)
        case FileType.PARQUET:
            return df.write_parquet(filepath)
        case FileType.JSON:
            return df.write_json(filepath)
        case _:
            raise ValueError(f"Unsupported file type: {extension} for Read")

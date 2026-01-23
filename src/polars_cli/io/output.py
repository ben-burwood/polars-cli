import polars as pl

from polars_cli.io.filetype import FileType


def _sink_file(df: pl.LazyFrame, filepath: str) -> None:
    """Sink Polars LazyFrame to File"""
    extension = filepath.split(".")[-1]
    match FileType.from_extension(extension):
        case FileType.CSV:
            return df.sink_csv(filepath)
        case FileType.PARQUET:
            return df.sink_parquet(filepath)
        case _:
            raise ValueError(f"Unsupported file type: {extension} for Sink")


def _write_file(df: pl.DataFrame, filepath: str) -> None:
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
            raise ValueError(f"Unsupported file type: {extension} for Write")


def output_file(df: pl.LazyFrame | pl.DataFrame, filepath: str) -> None:
    """Output Polars LazyFrame/DataFrame to File"""
    if isinstance(df, pl.LazyFrame):
        _sink_file(df, filepath)
    elif isinstance(df, pl.DataFrame):
        _write_file(df, filepath)
    else:
        raise TypeError(f"DF of Type ({type(df)}) cannot be Output")

import argparse

import polars as pl

from polars_cli.datatype import CastableDataType
from polars_cli.io import input_file, output_file

PARSER = argparse.ArgumentParser(prog="Polars CLI", description="Polars CLI is a command-line interface for the Polars DataFrame Library")
PARSER.add_argument("input", type=str, help="Input File Path - with Extension")
PARSER.add_argument("-o", "--output", type=str, help="Output File Path - with Extension")
PARSER.add_argument("--select", type=str, help="List of Columns to Select (comma-seperated)")
PARSER.add_argument("--drop", type=str, help="List of Columns to Drop (comma-seperated)")
PARSER.add_argument("--rename", type=str, help="List of Columns to Rename (comma-seperated)")
PARSER.add_argument("--cast", type=str, help="List of Columns to Cast (comma-seperated)")
PARSER.add_argument("--sort", type=str, help="List of Columns to Sort (comma-seperated)")
PARSER.add_argument("--reverse", action="store_true", help="Reverse Sort Order")
PARSER.add_argument("--head", type=int, help="Head Rows to Keep")
PARSER.add_argument("--tail", type=int, help="Tail Rows to Keep")
PARSER.add_argument("--slice", type=str, help="Slice Rows to Keep (start:length?)")
PARSER.add_argument("--gather", type=int, help="Gather Every Value - i.e. 3 means take every Third Row")
PARSER.add_argument("--unique", action="store_true", help="Remove Duplicate Rows")
PARSER.add_argument("--schema", action="store_true", help="Print Schema")
PARSER.add_argument("--describe", action="store_true", help="Print Descriptive Statistics")
PARSER.add_argument("--explain", action="store_true", help="Explain the Execution Plan")


def cli() -> None:
    args = PARSER.parse_args()

    df = input_file(args.input, lazy=True)

    ## RENAME
    rename_list = set(args.rename.split(",")) if args.rename else None
    if rename_list:
        rename_cmds: dict[str, str] = {old: new for old, new in (rn.split(":") for rn in rename_list)}
        df = df.rename(rename_cmds)

    # CAST
    cast_list = set(args.cast.split(",")) if args.cast else None
    if cast_list:
        cast_cmds: dict[str, pl.DataType] = {
            col: CastableDataType.from_string(datatype).polars_datatype for col, datatype in (cs.split(":") for cs in cast_list)
        }
        df = df.cast(cast_cmds)

    # DROP / SELECT PROJECTION
    drop_list = set(args.drop.split(",")) if args.drop else None
    select_list = set(args.select.split(",")) if args.select else None
    if drop_list or select_list:
        if drop_list and select_list and (both := drop_list.intersection(select_list)):
            raise ValueError(f"Cannot Select and Drop the same Column(s) : {both}")
        if drop_list:
            df = df.drop(drop_list)
        if select_list:
            df = df.select(select_list)

    # SORT
    sort_list = args.sort.split(",") if args.sort else None
    if sort_list:
        df = df.sort(sort_list)
    if args.reverse:
        df = df.reverse()

    # UNIQUE
    if args.unique:
        df = df.unique()

    # LIMIT
    if args.slice:
        start, _, end = args.slice.partition(":")
        df = df.slice(int(start), int(end) if end else None)
    if args.head:
        df = df.head(args.head)
    if args.tail:
        df = df.tail(args.tail)
    if args.gather:
        df.gather_every(args.gather)

    if args.schema:
        print(df.collect_schema())
    if args.describe:
        print(df.describe())
    if args.explain:
        print(df.explain())

    print(df.collect())
    if args.output:
        output_file(df, args.output)

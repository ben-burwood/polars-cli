import argparse

import polars as pl

from polars_cli.datatype import CastableDataType
from polars_cli.io import input_file, output_file

PARSER = argparse.ArgumentParser(prog="Polars CLI", description="Polars CLI is a command-line interface for the Polars DataFrame Library")
PARSER.add_argument("-i", "--input", type=str, required=True, help="Input File Path - with Extension")
PARSER.add_argument("-o", "--output", type=str, help="Output File Path - with Extension")
PARSER.add_argument("-s", "--select", type=str, help="List of Columns to Select (comma-seperated)")
PARSER.add_argument("-d", "--drop", type=str, help="List of Columns to Drop (comma-seperated)")
PARSER.add_argument("-r", "--rename", type=str, help="List of Columns to Rename (comma-seperated)")
PARSER.add_argument("-c", "--cast", type=str, help="List of Columns to Cast (comma-seperated)")
PARSER.add_argument("-g", "--gather", type=int, help="Gather Every Value - i.e. 3 means take every Third Row")
PARSER.add_argument("--lazy", action="store_true", help="Use Lazy Evaluation")


def cli() -> None:
    args = PARSER.parse_args()
    input, output, drop, select, rename, cast, gather, lazy = (
        args.input,
        args.output,
        args.drop,
        args.select,
        args.rename,
        args.cast,
        args.gather,
        args.lazy,
    )

    df = input_file(input, lazy=lazy)

    rename_list = set(rename.split(",")) if rename else None
    if rename_list:
        rename_cmds: dict[str, str] = {old: new for old, new in (rn.split(":") for rn in rename_list)}
        df = df.rename(rename_cmds)

    cast_list = set(cast.split(",")) if cast else None
    if cast_list:
        cast_cmds: dict[str, pl.DataType] = {
            col: CastableDataType.from_string(datatype).polars_datatype for col, datatype in (cs.split(":") for cs in cast_list)
        }
        df = df.cast(cast_cmds)

    if gather:
        df.gather_every(gather)

    drop_list = set(drop.split(",")) if drop else None
    select_list = set(select.split(",")) if select else None
    if drop_list or select_list:
        if drop_list and select_list:
            if both := drop_list.intersection(select_list):
                raise ValueError(f"Cannot Select and Drop the same Column(s) : {both}")
        if drop_list:
            df = df.drop(drop_list)
        if select_list:
            df = df.select(select_list)

    if output:
        output_file(df, output)

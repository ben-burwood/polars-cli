import argparse

import polars as pl

from polars_cli.io import input_file, output_file

PARSER = argparse.ArgumentParser(prog="Polars CLI", description="Polars CLI is a command-line interface for the Polars DataFrame Library")
PARSER.add_argument("-i", "--input", type=str, required=True, help="Input File Path - with Extension")
PARSER.add_argument("-o", "--output", type=str, help="Output File Path - with Extension")
PARSER.add_argument("-l", "--lazy", action="store_true", help="Use Lazy Evaluation")


def main(input: str, output: str | None = None, lazy: bool = False) -> None:
    df = input_file(input, lazy=lazy)

    print(df)

    if output:
        output_file(df, output)


if __name__ == "__main__":
    args = PARSER.parse_args()
    print(args)
    main(args.input, args.output, args.lazy)

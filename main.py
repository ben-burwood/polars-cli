import argparse

from polars_cli.io import input_file, output_file

PARSER = argparse.ArgumentParser(prog="Polars CLI", description="Polars CLI is a command-line interface for the Polars DataFrame Library")
PARSER.add_argument("-i", "--input", type=str, required=True, help="Input File Path - with Extension")
PARSER.add_argument("-o", "--output", type=str, help="Output File Path - with Extension")
PARSER.add_argument("-l", "--lazy", action="store_true", help="Use Lazy Evaluation")
PARSER.add_argument("-s", "--select", type=str, help="List of Columns to Select (comma-seperated)")
PARSER.add_argument("-d", "--drop", type=str, help="List of Columns to Drop (comma-seperated)")


def main(input: str, output: str | None = None, lazy: bool = False, drop: str | None = None, select: str | None = None) -> None:
    df = input_file(input, lazy=lazy)

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

    print(df)

    if output:
        output_file(df, output)


if __name__ == "__main__":
    args = PARSER.parse_args()
    print(args)
    main(args.input, args.output, args.lazy, args.drop, args.select)

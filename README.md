# Polars CLI

The Polars CLI can be used for fairly rudimentary [Polars](https://pola.rs) usage.

## Installation

Use `uv tool` for easy installation : `uv tool install git+https://github.com/ben-burwood/polars-cli` 

## Usage

`polars`

- `*.csv` - Input Filepath
- `--output output.csv` - Output Filepath
- `--drop Name,Age` - Drop Columns (as 'Name,Age')
- `--select Name,Age` - Select Columns (as 'Name,Age')
- `--rename today:yesterday` - Rename Columns (as 'Name:name,Age:age')
- `--cast today:date` - Cast Columns (as 'Name:string,Age:uint32')
- `--sort Name,Age` - Sort Columns (as 'Name:asc,Age:desc')
- `--head 10` - Head Rows to Filter to
- `--tail 10` - Tail Rows to Filter to
- `--slice 10:20` - Slice Rows to Filter to (as 'start:length' where length is optional)
- `--gather 10` - Gather Every x Columns - Thin the Dataset
- `--unique` - Remove Duplicate Rows (at end of Execution so only for selected Columns)

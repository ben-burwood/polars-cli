# Polars CLI

The Polars CLI can be used for fairly rudimentary [Polars](https://pola.rs) usage.

## Features

- [X] Read/Write from CSV, Parquet, JSON
  - [X] Globbing
- [X] Select Columns (comma seperated list)
- [X] Drop Columns (comma seperated list)
- [X] Rename Columns (comma seperated list)
- [X] Cast Columns (comma seperated list)
- [X] Sort for Ordering Datasets
- [X] Head/Tail for Thinning Datasets to X Rows
- [X] Slice for Thinning Datasets
- [X] Gather for Thinning Datasets
- [X] Unique for Removing Duplicate Rows

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

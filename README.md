# Polars CLI

The Polars CLI can be used for fairly rudimentary [Polars](https://pola.rs) usage.

## Features

- [X] Read/Write from CSV, Parquet, JSON
  - [X] Globbing
  - [ ] S3 Cloud IO - Requires `s3fs` Dependency
- [X] Select Columns (comma seperated list)
- [X] Drop Columns (comma seperated list)
- [X] Rename Columns (comma seperated list)
- [X] Gather for Thinning Datasets
- [ ] Filter

## Usage

`polars-cli`

- `--input` - Input Filepath
- `--output` - Output Filepath
- `--drop` - Drop Columns (as 'Name,Age')
- `--select` - Select Columns (as 'Name,Age')
- `--rename` - Rename Columns (as 'Name:name,Age:age')
- `--gather` - Gather Every x Columns - Thin the Dataset
- `--lazy` - Execute Lazily (scan->sink)

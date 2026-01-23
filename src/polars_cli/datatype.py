from enum import Enum, auto

import polars as pl


class CastableDataType(Enum):
    """Data Type that can be Casted to in Polars"""

    # Numeric
    DECIMAL = auto()
    FLOAT_16 = auto()
    FLOAT_32 = auto()
    FLOAT_64 = auto()
    INT_8 = auto()
    INT_16 = auto()
    INT_32 = auto()
    INT_64 = auto()
    INT_128 = auto()
    UINT_8 = auto()
    UINT_16 = auto()
    UINT_32 = auto()
    UINT_64 = auto()
    # String
    STRING = auto()
    CATEGORICAL = auto()
    # Temporal
    DATETIME = auto()
    DATE = auto()
    TIME = auto()
    DURATION = auto()
    # Others
    BOOLEAN = auto()

    @property
    def polars_datatype(self) -> pl.DataType:
        return _CASTABLE_DATATYPE_TO_POLARS[self]

    @staticmethod
    def from_string(string: str) -> "CastableDataType":
        for dt in CastableDataType:
            if dt.name.replace("_", "").lower() == string.lower():
                return dt
        raise ValueError(f"Invalid CastableDataType: {string}")


_CASTABLE_DATATYPE_TO_POLARS = {
    CastableDataType.DECIMAL: pl.Decimal,
    CastableDataType.FLOAT_16: pl.Float16,
    CastableDataType.FLOAT_32: pl.Float32,
    CastableDataType.FLOAT_64: pl.Float64,
    CastableDataType.INT_8: pl.Int8,
    CastableDataType.INT_16: pl.Int16,
    CastableDataType.INT_32: pl.Int32,
    CastableDataType.INT_64: pl.Int64,
    CastableDataType.INT_128: pl.Int128,
    CastableDataType.UINT_8: pl.UInt8,
    CastableDataType.UINT_16: pl.UInt16,
    CastableDataType.UINT_32: pl.UInt32,
    CastableDataType.UINT_64: pl.UInt64,
    CastableDataType.STRING: pl.String,
    CastableDataType.CATEGORICAL: pl.Categorical,
    CastableDataType.DATETIME: pl.Datetime,
    CastableDataType.DATE: pl.Date,
    CastableDataType.TIME: pl.Time,
    CastableDataType.DURATION: pl.Duration,
    CastableDataType.BOOLEAN: pl.Boolean,
}

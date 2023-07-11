from datetime import datetime
from typing import Any, Callable
from zoneinfo import ZoneInfo

import orjson
from pydantic import BaseModel, root_validator


def orjson_dumps(v: Any, *, default: Callable[[Any], Any] | None) -> str:
    """orjson_dumps is a custom JSON encoder that uses orjson to serialize
    """
    return orjson.dumps(v, default=default).decode()


def convert_datetime_to_gmt(dt: datetime) -> str:
    """convert_datetime_to_gmt converts a datetime to a string in the gmt format
    """
    if not dt.tzinfo:
        dt = dt.replace(tzinfo=ZoneInfo('UTC'))

    return dt.strftime('%Y-%m-%dT%H:%M:%S%z')


class ORJSONModel(BaseModel):
    """ORJSONModel is a Pydantic model that uses orjson for serialization.
    """
    class Config:
        """Configures the ORJSONModel to use orjson for serialization.
        """
        json_loads = orjson.loads
        json_dumps = orjson_dumps
        json_encoders = {datetime: convert_datetime_to_gmt}
        allow_population_by_field_name = True

    @root_validator()
    def set_null_microseconds(cls, data: dict[str, Any]) -> dict[str, Any]:
        """Set microseconds to 0 for all datetime fields.
        """
        datetime_fields = {
            k: v.replace(microsecond=0)
            for k, v in data.items()
            if isinstance(k, datetime)
        }

        return {**data, **datetime_fields}

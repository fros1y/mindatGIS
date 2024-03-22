import datetime
import logging
from dataclasses import dataclass, field
import dataclasses
from typing import Optional
from dateutil.parser import isoparse

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class Locality:
    locality_id: int
    longid: Optional[str] = None
    guid: Optional[str] = None
    revtxtd: Optional[str] = None
    description_short: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    langtxt: Optional[str] = None
    elements: Optional[str] = None
    country: Optional[str] = None
    coordsystem: Optional[int] = None
    parent: Optional[int] = None
    links: Optional[str] = None
    area: Optional[int] = None
    non_hierarchical: Optional[int] = None
    meteorite_type: Optional[int] = None
    company: Optional[int] = None
    company2: Optional[int] = None
    loc_group: Optional[int] = None
    status_year: Optional[str] = None
    company_year: Optional[str] = None
    discovered_before: Optional[int] = None
    discovery_year: Optional[int] = None
    level: Optional[int] = None
    locsinclude: Optional[str] = None
    locsexclude: Optional[str] = None
    wikipedia: Optional[str] = None
    osmid: Optional[str] = None
    geonames: Optional[int] = None
    txt: Optional[str] = None
    dateadd: Optional[datetime.datetime] = None
    datemodify: Optional[datetime.datetime] = None
    refs: Optional[str] = None
    age: Optional[int] = None
    loc_status: Optional[int] = None
    discovery_year_type: Optional[str] = None
    timestamp: Optional[datetime.datetime] = None
    additional_properties: dict = field(default_factory=dict)

    @staticmethod
    def from_dict(src_dict: dict) -> "Locality":
        src_dict["locality_id"] = src_dict.pop("id")

        # Convert '0' values to None for specific fields if necessary
        fields_with_zeros = ["latitude", "longitude", "age", "loc_status"]
        for field in fields_with_zeros:
            if field in src_dict and src_dict[field] == 0:
                src_dict[field] = None

        # Handle date fields with error handling
        datetime_fields = ["dateadd", "datemodify", "timestamp"]
        for field in datetime_fields:
            date_str = src_dict.get(field)
            if date_str:
                try:
                    src_dict[field] = isoparse(date_str)
                except ValueError:
                    logger.warning(f"Invalid date format for '{field}': {date_str}")
                    src_dict[field] = None

        # Separate additional properties from known fields
        known_fields = {field.name for field in dataclasses.fields(Locality)}
        additional_properties = {
            k: v for k, v in src_dict.items() if k not in known_fields
        }
        src_dict = {k: v for k, v in src_dict.items() if k in known_fields}

        # Create the Locality instance
        locality_instance = Locality(**src_dict)
        locality_instance.additional_properties = additional_properties
        return locality_instance

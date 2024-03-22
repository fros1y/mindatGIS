import datetime
from typing import Any, Dict, Union, Type, TypeVar
from attrs import define as _attrs_define
from attrs import _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="Locality")


@_attrs_define
class Locality:
    id: int
    longid: str
    guid: str
    revtxtd: str
    description_short: str
    latitude: float
    longitude: float
    langtxt: str
    elements: str
    country: str
    coordsystem: int
    parent: int
    links: str
    area: int
    non_hierarchical: int
    meteorite_type: int
    company: int
    company2: int
    loc_group: int
    status_year: str
    company_year: str
    discovered_before: int
    discovery_year: int
    level: int
    locsinclude: str
    locsexclude: str
    wikipedia: str
    osmid: str
    geonames: int
    txt: Union[None, str] = None
    dateadd: Union[None, datetime.datetime] = None
    datemodify: Union[None, datetime.datetime] = None
    refs: Union[None, str] = None
    age: Union[None, int] = None
    loc_status: Union[None, int] = None
    discovery_year_type: Union[str] = None
    timestamp: Union[None, datetime.datetime] = None
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        result = {
            "id": self.id,
            "longid": self.longid,
            "guid": self.guid,
            "revtxtd": self.revtxtd,
            "description_short": self.description_short,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "langtxt": self.langtxt,
            "elements": self.elements,
            "country": self.country,
            "coordsystem": self.coordsystem,
            "parent": self.parent,
            "links": self.links,
            "area": self.area,
            "non_hierarchical": self.non_hierarchical,
            "meteorite_type": self.meteorite_type,
            "company": self.company,
            "company2": self.company2,
            "loc_group": self.loc_group,
            "status_year": self.status_year,
            "company_year": self.company_year,
            "discovered_before": self.discovered_before,
            "discovery_year": self.discovery_year,
            "level": self.level,
            "locsinclude": self.locsinclude,
            "locsexclude": self.locsexclude,
            "wikipedia": self.wikipedia,
            "osmid": self.osmid,
            "geonames": self.geonames,
            "txt": self.txt,
            "dateadd": self.dateadd.isoformat() if self.dateadd else None,
            "datemodify": self.datemodify.isoformat() if self.datemodify else None,
            "refs": self.refs,
            "age": self.age,
            "loc_status": self.loc_status,
            "discovery_year_type": self.discovery_year_type,
            "timestamp": self.timestamp.isoformat() if self.timestamp else None,
        }
        result.update(self.additional_properties)
        return result

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        d["dateadd"] = isoparse(d["dateadd"]) if d.get("dateadd") else None
        d["datemodify"] = isoparse(d["datemodify"]) if d.get("datemodify") else None
        d["timestamp"] = isoparse(d["timestamp"]) if d.get("timestamp") else None

        return cls(
            **d,
            additional_properties={
                k: v for k, v in d.items() if k not in cls.__annotations__
            }
        )

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

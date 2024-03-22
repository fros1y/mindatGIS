import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Locality")


@_attrs_define
class Locality:
    """to display -null- values as -empty string-

    Attributes:
        id (int):
        longid (str):
        guid (str):
        revtxtd (str):
        description_short (str):
        latitude (float):
        longitude (float):
        langtxt (str):
        elements (str):
        country (str):
        coordsystem (int):
        parent (int):
        links (str):
        area (int):
        non_hierarchical (int):
        meteorite_type (int):
        company (int):
        company2 (int):
        loc_group (int):
        status_year (str):
        company_year (str):
        discovered_before (int):
        discovery_year (int):
        level (int):
        locsinclude (str):
        locsexclude (str):
        wikipedia (str):
        osmid (str):
        geonames (int):
        txt (Union[None, Unset, str]):
        dateadd (Union[None, Unset, datetime.datetime]):
        datemodify (Union[None, Unset, datetime.datetime]):
        refs (Union[None, Unset, str]):
        age (Union[None, Unset, int]):
        loc_status (Union[None, Unset, int]):
        discovery_year_type (Union[Unset, str]):
        timestamp (Union[None, Unset, datetime.datetime]):
    """

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
    txt: Union[None, Unset, str] = UNSET
    dateadd: Union[None, Unset, datetime.datetime] = UNSET
    datemodify: Union[None, Unset, datetime.datetime] = UNSET
    refs: Union[None, Unset, str] = UNSET
    age: Union[None, Unset, int] = UNSET
    loc_status: Union[None, Unset, int] = UNSET
    discovery_year_type: Union[Unset, str] = UNSET
    timestamp: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        longid = self.longid

        guid = self.guid

        revtxtd = self.revtxtd

        description_short = self.description_short

        latitude = self.latitude

        longitude = self.longitude

        langtxt = self.langtxt

        elements = self.elements

        country = self.country

        coordsystem = self.coordsystem

        parent = self.parent

        links = self.links

        area = self.area

        non_hierarchical = self.non_hierarchical

        meteorite_type = self.meteorite_type

        company = self.company

        company2 = self.company2

        loc_group = self.loc_group

        status_year = self.status_year

        company_year = self.company_year

        discovered_before = self.discovered_before

        discovery_year = self.discovery_year

        level = self.level

        locsinclude = self.locsinclude

        locsexclude = self.locsexclude

        wikipedia = self.wikipedia

        osmid = self.osmid

        geonames = self.geonames

        txt: Union[None, Unset, str]
        if isinstance(self.txt, Unset):
            txt = UNSET
        else:
            txt = self.txt

        dateadd: Union[None, Unset, str]
        if isinstance(self.dateadd, Unset):
            dateadd = UNSET
        elif isinstance(self.dateadd, datetime.datetime):
            dateadd = self.dateadd.isoformat()
        else:
            dateadd = self.dateadd

        datemodify: Union[None, Unset, str]
        if isinstance(self.datemodify, Unset):
            datemodify = UNSET
        elif isinstance(self.datemodify, datetime.datetime):
            datemodify = self.datemodify.isoformat()
        else:
            datemodify = self.datemodify

        refs: Union[None, Unset, str]
        if isinstance(self.refs, Unset):
            refs = UNSET
        else:
            refs = self.refs

        age: Union[None, Unset, int]
        if isinstance(self.age, Unset):
            age = UNSET
        else:
            age = self.age

        loc_status: Union[None, Unset, int]
        if isinstance(self.loc_status, Unset):
            loc_status = UNSET
        else:
            loc_status = self.loc_status

        discovery_year_type = self.discovery_year_type

        timestamp: Union[None, Unset, str]
        if isinstance(self.timestamp, Unset):
            timestamp = UNSET
        elif isinstance(self.timestamp, datetime.datetime):
            timestamp = self.timestamp.isoformat()
        else:
            timestamp = self.timestamp

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "longid": longid,
                "guid": guid,
                "revtxtd": revtxtd,
                "description_short": description_short,
                "latitude": latitude,
                "longitude": longitude,
                "langtxt": langtxt,
                "elements": elements,
                "country": country,
                "coordsystem": coordsystem,
                "parent": parent,
                "links": links,
                "area": area,
                "non_hierarchical": non_hierarchical,
                "meteorite_type": meteorite_type,
                "company": company,
                "company2": company2,
                "loc_group": loc_group,
                "status_year": status_year,
                "company_year": company_year,
                "discovered_before": discovered_before,
                "discovery_year": discovery_year,
                "level": level,
                "locsinclude": locsinclude,
                "locsexclude": locsexclude,
                "wikipedia": wikipedia,
                "osmid": osmid,
                "geonames": geonames,
            }
        )
        if txt is not UNSET:
            field_dict["txt"] = txt
        if dateadd is not UNSET:
            field_dict["dateadd"] = dateadd
        if datemodify is not UNSET:
            field_dict["datemodify"] = datemodify
        if refs is not UNSET:
            field_dict["refs"] = refs
        if age is not UNSET:
            field_dict["age"] = age
        if loc_status is not UNSET:
            field_dict["loc_status"] = loc_status
        if discovery_year_type is not UNSET:
            field_dict["discovery_year_type"] = discovery_year_type
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        longid = d.pop("longid")

        guid = d.pop("guid")

        revtxtd = d.pop("revtxtd")

        description_short = d.pop("description_short")

        latitude = d.pop("latitude")

        longitude = d.pop("longitude")

        langtxt = d.pop("langtxt")

        elements = d.pop("elements")

        country = d.pop("country")

        coordsystem = d.pop("coordsystem")

        parent = d.pop("parent")

        links = d.pop("links")

        area = d.pop("area")

        non_hierarchical = d.pop("non_hierarchical")

        meteorite_type = d.pop("meteorite_type")

        company = d.pop("company")

        company2 = d.pop("company2")

        loc_group = d.pop("loc_group")

        status_year = d.pop("status_year")

        company_year = d.pop("company_year")

        discovered_before = d.pop("discovered_before")

        discovery_year = d.pop("discovery_year")

        level = d.pop("level")

        locsinclude = d.pop("locsinclude")

        locsexclude = d.pop("locsexclude")

        wikipedia = d.pop("wikipedia")

        osmid = d.pop("osmid")

        geonames = d.pop("geonames")

        def _parse_txt(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        txt = _parse_txt(d.pop("txt", UNSET))

        def _parse_dateadd(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dateadd_type_0 = isoparse(data)

                return dateadd_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        dateadd = _parse_dateadd(d.pop("dateadd", UNSET))

        def _parse_datemodify(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                datemodify_type_0 = isoparse(data)

                return datemodify_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        datemodify = _parse_datemodify(d.pop("datemodify", UNSET))

        def _parse_refs(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        refs = _parse_refs(d.pop("refs", UNSET))

        def _parse_age(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        age = _parse_age(d.pop("age", UNSET))

        def _parse_loc_status(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        loc_status = _parse_loc_status(d.pop("loc_status", UNSET))

        discovery_year_type = d.pop("discovery_year_type", UNSET)

        def _parse_timestamp(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                timestamp_type_0 = isoparse(data)

                return timestamp_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        timestamp = _parse_timestamp(d.pop("timestamp", UNSET))

        locality = cls(
            id=id,
            longid=longid,
            guid=guid,
            revtxtd=revtxtd,
            description_short=description_short,
            latitude=latitude,
            longitude=longitude,
            langtxt=langtxt,
            elements=elements,
            country=country,
            coordsystem=coordsystem,
            parent=parent,
            links=links,
            area=area,
            non_hierarchical=non_hierarchical,
            meteorite_type=meteorite_type,
            company=company,
            company2=company2,
            loc_group=loc_group,
            status_year=status_year,
            company_year=company_year,
            discovered_before=discovered_before,
            discovery_year=discovery_year,
            level=level,
            locsinclude=locsinclude,
            locsexclude=locsexclude,
            wikipedia=wikipedia,
            osmid=osmid,
            geonames=geonames,
            txt=txt,
            dateadd=dateadd,
            datemodify=datemodify,
            refs=refs,
            age=age,
            loc_status=loc_status,
            discovery_year_type=discovery_year_type,
            timestamp=timestamp,
        )

        locality.additional_properties = d
        return locality

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

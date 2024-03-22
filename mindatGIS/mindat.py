import json
import logging
from requests_ratelimiter import LimiterSession
from typing import Dict, Iterable, List, Union, Iterator, Generator, Any, Self, Optional
from retry_requests import retry

Params = Dict[str, str]


class MindatAPI:
    def __init__(
        self,
        api_key: str,
        session: LimiterSession = LimiterSession(per_second=1.5),
        base_url: str = "https://api.mindat.org",
    ) -> Self:
        self.api_key = api_key
        self.session = retry(session)
        self.base_url = base_url

    def request(self, url: str, params: Optional[Params] = None) -> Any:
        logging.debug(f"Requesting {url}")
        headers = {"Authorization": "Token " + self.api_key}
        response = self.session.get(url, params=params, headers=headers)

        if response.status_code != 200:
            logging.error(f"Request failed with status code {response.status_code}")
            logging.error(f"Response: {response.text}")
            raise Exception(f"Request failed with status code {response.status_code}")
        try:
            decoded = response.json()
        except json.decoder.JSONDecodeError:
            logging.error(f"Failed to decode JSON response: {response.text}")
            raise

        return decoded

    def get_paged_list(self, url: str, params: Optional[Params] = None):
        response = self.request(url, params)
        yield from response["results"]
        while response["next"]:
            response = self.request(response["next"])
            yield from response["results"]

    def get_locality(self, locality_id: int, params: Optional[Params] = None):
        return self.request(self.base_url + f"/localities/{locality_id}", params)

    def get_localities(self, params: Optional[Params] = None) -> Iterable[Any]:
        results = self.get_paged_list(self.base_url + "/localities", params)
        # HACK: Filter out localities without coordinates, represented by 0s
        filtered = filter(lambda x: x["longitude"] != 0 and x["latitude"] != 0, results)
        return filtered

    def get_geomaterial(self, geomaterial_id: int, params: Optional[Params] = None):
        return self.request(self.base_url + f"/geomaterials/{geomaterial_id}", params)

    def get_geomaterials(self, params: Optional[Params] = Dict()):
        params = params.update({"expand", "locality"})
        return self.get_paged_list(self.base_url + "/geomaterials", params)

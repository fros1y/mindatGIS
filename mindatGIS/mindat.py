import json
import logging
from requests_ratelimiter import LimiterSession
from typing import Dict, Iterable, List, Union, Iterator, Generator, Any, Self, Optional
from retry_requests import retry
from locality import Locality

Params = Dict[str, str]


class MindatAPI:
    """
    A Python wrapper for the Mindat.org API.

    This class provides methods to interact with the Mindat.org API and retrieve information about localities and geomaterials.

    Attributes:
        api_key (str): The API key for accessing the Mindat.org API.
        session (LimiterSession): The session object for rate limiting requests.
        base_url (str): The base URL of the Mindat.org API.

    Methods:
        request(url: str, params: Optional[Params] = None) -> Any:
            Sends a GET request to the specified URL with optional parameters and returns the response.

        get_paged_list(url: str, params: Optional[Params] = None) -> Iterator:
            Retrieves a paged list of results from the specified URL and returns an iterator over the results.

        get_locality(locality_id: int, params: Optional[Params] = None) -> Optional[Locality]:
            Retrieves information about a specific locality by its ID and returns a Locality object.

        get_localities(params: Optional[Params] = None) -> Iterable[Locality]:
            Retrieves a list of localities and returns an iterable of Locality objects.

        get_geomaterial(geomaterial_id: int, params: Optional[Params] = None) -> Any:
            Retrieves information about a specific geomaterial by its ID and returns the response.

        get_geomaterials(params: Optional[Params] = dict) -> Iterator:
            Retrieves a paged list of geomaterials and returns an iterator over the results.

    """

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
        """
        Sends a GET request to the specified URL with optional parameters and returns the response.

        Args:
            url (str): The URL to send the request to.
            params (Optional[Params]): Optional parameters to include in the request.

        Returns:
            Any: The decoded JSON response.

        Raises:
            Exception: If the request fails with a non-200 status code.
            json.decoder.JSONDecodeError: If the JSON response cannot be decoded.

        """
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

    def get_paged_list(self, url: str, params: Optional[Params] = None) -> Iterator:
        """
        Retrieves a paged list of results from the specified URL and returns an iterator over the results.

        Args:
            url (str): The URL to retrieve the paged list from.
            params (Optional[Params]): Optional parameters to include in the request.

        Yields:
            Any: The results from each page of the paged list.

        """
        response = self.request(url, params)
        yield from response["results"]
        while response["next"]:
            response = self.request(response["next"])
            yield from response["results"]

    def get_locality(
        self, locality_id: int, params: Optional[Params] = None
    ) -> Optional[Locality]:
        """
        Retrieves information about a specific locality by its ID and returns a Locality object.

        Args:
            locality_id (int): The ID of the locality to retrieve.
            params (Optional[Params]): Optional parameters to include in the request.

        Returns:
            Optional[Locality]: The Locality object representing the requested locality, or None if not found.

        """
        record = self.request(self.base_url + f"/localities/{locality_id}", params)
        if record:
            return Locality.from_dict(record)

    def get_localities(self, params: Optional[Params] = None) -> Iterable[Locality]:
        """
        Retrieves a list of localities and returns an iterable of Locality objects.

        Args:
            params (Optional[Params]): Optional parameters to include in the request.

        Yields:
            Locality: The Locality objects representing the retrieved localities.

        """
        results = self.get_paged_list(self.base_url + "/localities", params)
        for result in results:
            yield Locality.from_dict(result)

    def get_geomaterial(
        self, geomaterial_id: int, params: Optional[Params] = None
    ) -> Any:
        """
        Retrieves information about a specific geomaterial by its ID and returns the response.

        Args:
            geomaterial_id (int): The ID of the geomaterial to retrieve.
            params (Optional[Params]): Optional parameters to include in the request.

        Returns:
            Any: The decoded JSON response.

        """
        return self.request(self.base_url + f"/geomaterials/{geomaterial_id}", params)

    def get_geomaterials(self, params: Optional[Params] = dict) -> Iterator:
        """
        Retrieves a paged list of geomaterials and returns an iterator over the results.

        Args:
            params (Optional[Params]): Optional parameters to include in the request.

        Yields:
            Any: The results from each page of the paged list.

        """
        params = params.update({"expand": "locality"})
        return self.get_paged_list(self.base_url + "/geomaterials", params)

import webbrowser
from httpx import URL

from src.services.service import Service


class APISearch(Service):

    def __init__(self, api_url: str):
        self._api_url = api_url

    def __str__(self):
        return f"{self.__class__.__name__}({self.host})"

    def __repr__(self):
        return self.__str__()

    def _get_url(self, value: str) -> str:
        return self._api_url.format(value)

    @property
    def host(self):
        return URL(self._api_url).host

    def query(self, query: str) -> None:
        webbrowser.open(self._get_url(query))

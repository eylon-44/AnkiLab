import webbrowser
from dataclasses import dataclass

from httpx import URL

from src.services.service import Service


@dataclass
class APIService(Service):
    url: str
    use_translation: bool = False

    def __str__(self):
        return f"{self.__class__.__name__}({self.host})"

    def __repr__(self):
        return self.__str__()

    def _get_url(self, value: str) -> str:
        return self.url.format(value)

    @property
    def host(self):
        return URL(self.url).host

    def query(self, query: str) -> None:
        webbrowser.open(self._get_url(query))

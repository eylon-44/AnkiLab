import webbrowser
from httpx import URL

class APISearch:

    def __init__(self, api_url: str):
        self._api_url = api_url

    def __str__(self):
        return f"{self.__class__.__name__}({self.host})"

    def __repr__(self):
        return self.__str__()

    @property
    def host(self):
        return URL(self._api_url).host

    def get_url(self, value: str) -> str:
        return self._api_url.format(value)

    def open_in_browser(self, value: str) -> None:
        webbrowser.open(self.get_url(value))

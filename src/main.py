import sys
from pathlib import Path

from src.configuration import Configuration
from src.services.api_search import APIService
from src.services.service import Service
from src.services.translator import Translator
from src.services.tts.tts_client import TTSClient


def get_configuration() -> Configuration:
    configuration_file = Path(sys.argv[1])
    return Configuration.model_validate_json(configuration_file.read_text())


def get_services(configuration: Configuration) -> list[Service]:
    services: list[Service] = configuration.api_services
    services.append(TTSClient.from_configuration(configuration))
    return services


def get_user_input(prompt: str = "> ") -> str | None:
    while True:
        user_input = input(prompt)
        if user_input:
            if user_input in ["-q", "-quit"]:
                return None
            return user_input


def query_services(services: list[Service], translator_service: Service, query: str):
    results = []
    for service in services:
        results.append(service.query(query))
    return results


def main():
    configuration = get_configuration()
    api_services: list[APIService] = configuration.api_services
    translator_service = Translator(configuration.language)

    while True:
        search_value = get_user_input()
        if not search_value:
            break

        translated_search_value = translator_service.query(search_value)
        for api_service in api_services:
            api_service.query(translated_search_value if api_service.use_translation else search_value)


if __name__ == "__main__":
    main()

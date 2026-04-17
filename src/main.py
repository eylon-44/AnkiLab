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
    services: list[Service] = [
        Translator(configuration.language),
        TTSClient.from_configuration(configuration)
    ]
    services.extend(APIService(api) for api in configuration.services_apis)
    return services


def get_user_input(prompt: str = "> ") -> str | None:
    while True:
        user_input = input(prompt)
        if user_input:
            if user_input in ["-q", "-quit"]:
                return None
            return user_input


def query_services(services: list[Service], query: str):
    results = []
    for service in services:
        results.append(service.query(query))
    return results


def main():
    configuration = get_configuration()
    services = get_services(configuration)

    while True:
        user_input = get_user_input()
        if not user_input:
            break
        results = query_services(services, user_input)
        print(results)


if __name__ == "__main__":
    main()

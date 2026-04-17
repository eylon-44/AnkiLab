from deep_translator import GoogleTranslator

from src.datatypes.language_iso import LanguageISO
from src.services.service import Service


class Translator(Service):

    def __init__(self, source_language: LanguageISO, target_language: LanguageISO = "auto") -> None:
        self.source_language = source_language
        self.target_language = target_language
        self.google_translator = GoogleTranslator(source=source_language, target=target_language)

    def __str__(self):
        return f"{self.__class__.__name__}({self.source_language} -> {self.target_language})"

    def __repr__(self):
        return self.__str__()

    def query(self, query: str) -> str:
        return self.google_translator.translate(query)

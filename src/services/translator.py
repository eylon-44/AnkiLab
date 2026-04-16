from deep_translator import GoogleTranslator

class Translator:

    def __init__(self, source_language: Language, target_language: Language) -> None:
        self.source_language = source_language
        self.target_language = target_language
        self.google_translator = GoogleTranslator(source=source_language, target=target_language)

    def __str__(self):
        return f"Translator({self.source_language} -> {self.target_language})"

    def __repr__(self):
        return self.__str__()

    def translate(self, text: str) -> str:
        return self.google_translator.translate(text)

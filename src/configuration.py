from elevenlabs import VoiceSettings
from pydantic import BaseModel, Field

from src.datatypes.language_iso import LanguageISO

class TTSConfiguration(BaseModel):
    api_key: str = Field(default="sk_392a2e348d477104bef1d15f272981bfb76ddf09f12b06db")
    model_id: str = Field(default="eleven_multilingual_v2")
    output_format: str = Field(default="mp3_44100_128")
    voice_settings: VoiceSettings = Field(default_factory=VoiceSettings)


class Configuration(BaseModel):
    language: LanguageISO
    word_search_apis: list[str]
    tts: TTSConfiguration = Field(default_factory=TTSConfiguration)

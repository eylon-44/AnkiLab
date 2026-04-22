from pathlib import Path

from elevenlabs import VoiceSettings
from pydantic import BaseModel, Field

from src.datatypes.language_iso import LanguageISO
from src.services.api_search import APIService
from src.services.tts.tts_voices import TTSVoice


class TTSConfiguration(BaseModel):
    api_key: str = Field(default="sk_392a2e348d477104bef1d15f272981bfb76ddf09f12b06db")
    model_id: str = Field(default="eleven_multilingual_v2")
    output_format: str = Field(default="mp3_44100_128")
    voice: TTSVoice = Field(default=TTSVoice.Adam)
    voice_settings: VoiceSettings = Field(default_factory=VoiceSettings)
    output_directory: Path = Field(default=Path("anki-lab-media"))

class Configuration(BaseModel):
    language: LanguageISO
    api_services: list[APIService]
    tts: TTSConfiguration = Field(default_factory=TTSConfiguration)

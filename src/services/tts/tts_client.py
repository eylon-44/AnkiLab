from typing import Self

from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs

from src.configuration import Configuration
from src.datatypes.language_iso import LanguageISO
from src.services.service import Service
from src.services.tts.tts_voices import TTSVoice
from src.utils.audio_utils import stream_to_bytes


class TTSClient(Service):

    def __init__(self, api_key: str, language: LanguageISO, voice: TTSVoice, model_id: str, output_format: str,
                 voice_settings: VoiceSettings) -> None:
        self._client = ElevenLabs(api_key=api_key)
        self.language = language
        self.voice = voice
        self.model_id = model_id
        self.output_format = output_format
        self.voice_settings = voice_settings

    @classmethod
    def from_configuration(cls: Self, configuration: Configuration) -> Self:
        return cls(
            api_key=configuration.tts.eleven_labs.api_key,
            language=configuration.langauge,
            output_format=configuration.tts.eleven_labs.output_format
        )

    def query(self, query: str) -> bytes:
        audio_stream = self._client.text_to_speech.convert(
            text=query,
            voice_id=self.voice,
            model_id=self.model_id,
            output_format=self.output_format,
            voice_settings=self.voice_settings
        )
        return stream_to_bytes(audio_stream)

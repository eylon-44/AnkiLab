from collections.abc import Iterable
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play
from enum import Enum
from typing import Self
from src.configuration import Configuration
from src.datatypes.language_iso import LangaugeISO

from src.services.tts.tts_voices import TTSVoice
from src.utils.audio_utils import stream_to_bytes


class TTSClient:

    def __init__(self, api_key: str, language: LangaugeISO, output_format: str) -> None:
        self._client = ElevenLabs(api_key=api_key)
        self.language = language

    @classmethod
    def from_configuration(cls: Self, configuration: Configuration) -> Self:
        return cls(
            api_key = configuration.tts.eleven_labs.api_key,
            language = configuration.langauge,
            output_format = configuration.tts.eleven_labs.output_format
        )

    def tts(self, text: str, voice: TTSVoice = TTSVoice.Serge) -> bytes:
        audio_stream = self._client.text_to_speech.convert(
            text=text,
            voice_id=voice,
            model_id=self.MODEL_ID,
            output_format=self.OUTPUT_FORMAT,
            voice_settings={
                "stability": 1,
                "similarity_boost": 0.75,
                "style": 0.5,
                "use_speaker_boost": True,
                "speed": 0.7
            },
        )

        return stream_to_bytes(audio_stream)
    
def play_audio(audio: bytes) -> None:
    play(audio)

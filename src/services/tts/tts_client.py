from datetime import datetime
from pathlib import Path
from typing import Self

from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs

from src.configuration import Configuration
from src.datatypes.language_iso import LanguageISO
from src.services.service import Service
from src.services.tts.tts_voices import TTSVoice
from src.utils.audio_utils import stream_to_bytes, play_audio


class TTSClient(Service):
    AUDIO_FILENAME_FORMAT = "{}.mp3"

    def __init__(self, api_key: str, language: LanguageISO, voice: TTSVoice, model_id: str, output_format: str,
                 voice_settings: VoiceSettings, output_directory: Path) -> None:
        self._client = ElevenLabs(api_key=api_key)
        self.language = language
        self.voice = voice
        self.model_id = model_id
        self.output_format = output_format
        self.voice_settings = voice_settings
        self.output_directory = output_directory

    @classmethod
    def from_configuration(cls, configuration: Configuration) -> Self:
        return cls(
            api_key=configuration.tts.api_key,
            language=configuration.language,
            voice=configuration.tts.voice,
            model_id=configuration.tts.model_id,
            output_format=configuration.tts.output_format,
            voice_settings=configuration.tts.voice_settings,
            output_directory=configuration.tts.output_directory
        )

    def _get_audio_file_path(self, filename: str) -> Path:
        now = datetime.now().strftime("%Y-%M-%d_%H-%M-%S")
        return self.output_directory / f"{filename}_{now}.mp3"

    def _save_audio_to_file(self, filename: str, audio: bytes) -> Path:
        file = self._get_audio_file_path(filename)
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_bytes(audio)
        return file

    def query(self, query: str) -> Path:
        audio_stream = self._client.text_to_speech.convert(
            text=query,
            voice_id=self.voice,
            model_id=self.model_id,
            output_format=self.output_format,
            voice_settings=self.voice_settings,
            language_code=self.language
        )
        audio_bytes = stream_to_bytes(audio_stream)
        play_audio(audio_bytes, block=False)
        return self._save_audio_to_file(query, audio_bytes)

import threading
from typing import Iterable

from elevenlabs.play import play


def play_audio(audio: bytes, block: bool = True) -> None:
    if block:
        play(audio)
    else:
        threading.Thread(target=play, args=(audio,)).start()


def stream_to_bytes(audio) -> bytes:
    if isinstance(audio, (bytes, bytearray)):
        return bytes(audio)

    if isinstance(audio, Iterable):
        data = bytearray()
        for chunk in audio:
            if isinstance(chunk, (bytes, bytearray)):
                data.extend(chunk)
        return bytes(data)

    raise TypeError("Audio is not bytes or iterable of bytes")


def save_last_audio():
    audio_path = Path(AUDIO_FILE_PATH.format(word=last_word, content=str(time())))

    create_directory(audio_path.parent)
    write_to_file(audio_path, last_audio)
    open_file_explorer(audio_path.parent)

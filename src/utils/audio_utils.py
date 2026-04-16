from typing import Iterable

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

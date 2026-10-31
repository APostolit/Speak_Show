# Листинг 1.3
import torch
from TTS.api import TTS
from pydub import AudioSegment

def t_to_v(text_file, speaker, language, audio_file):
    device = "cuda" if torch.cuda.is_available() else "cpu"

    # Загрузить TTS модель
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

    # Загрузить текстовый файл
    with open(text_file, "r") as file:
      text = file.read()

    tts.tts_to_file(
        text=text,
        speaker=speaker,
        language=language,
        file_path=audio_file)

    # Конвертировать в MP3 со сжатием
    wav_audio = AudioSegment.from_wav(output_file)
    wav_audio.export(output_file, format='mp3')

if __name__ == '__main__':
    input_file = "text_inp/forum.txt"  # Исходный текстовый файл
    lang = "ru"  # Язык
    dictor = "Viktor Menelaos"   # Диктор
    output_file = "audio_out/forum.mp3"  # Итоговый аудио файл
    t_to_v(input_file, dictor, lang,  output_file)
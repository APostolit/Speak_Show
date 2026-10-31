# Листинг 1.4
import torch
from TTS.api import TTS
from pydub import AudioSegment

def v_to_v(input_file, set_voice, output_file):
    # Получить устройство
    device = "cuda" if torch.cuda.is_available() else "cpu"
    # Загрузить модель
    tts = (TTS("voice_conversion_models/multilingual/multi-dataset/openvoice_v2")
           .to(device))
    # Выполнить преобразование
    tts.voice_conversion_to_file(source_wav=input_file,
                                 target_wav=set_voice,
                                 file_path=output_file)
    # Конвертировать в MP3 со сжатием
    wav_audio = AudioSegment.from_wav(output_file)
    wav_audio.export(output_file, format='mp3')

if __name__ == '__main__':
    input_file = "audio_out/Tanja_Adelina.wav"  # Исходный аудио файл
    set_voice = "audio_inp/levitan.wav"  # Образец голоса
    output_file = "audio_out/levitan.mp3"  # Итоговый аудио файл
    v_to_v(input_file, set_voice, output_file)
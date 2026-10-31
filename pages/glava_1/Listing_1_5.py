# Листинг 1.5
import torch
from TTS.api import TTS

def v_to_v(input_file, set_voice, output_file):
    # Получить устройство
    device = "cuda" if torch.cuda.is_available() else "cpu"
    # Загрузить модель
    tts = TTS("voice_conversion_models/multilingual/vctk/freevc24").to(device)
    # Выполнить преобразование
    tts.voice_conversion_to_file(source_wav=input_file,
                                 target_wav=set_voice,
                                 file_path=output_file)

if __name__ == '__main__':
    input_file = "audio_out/Tanja_Adelina.wav"  # Исходный аудио файл
    set_voice = "audio_inp/levitan.wav"  # Образец голоса
    output_file = "audio_out/levitan.wav"  # Итоговый аудио файл
    v_to_v(input_file, set_voice, output_file)
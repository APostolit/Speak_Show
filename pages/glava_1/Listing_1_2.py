# Листинг 1.2
import torch
from TTS.api import TTS

# Получить устройство
device = "cuda" if torch.cuda.is_available() else "cpu"
# Загрузить TTS модель
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

# Формирование входных данных для модели
text = ("Всем добрый день! Сегодня на наших компьютерных курсах "
        "мы приступаем к изучению нейронных сетей, которые позволяют"
        " текстовые данные трансформировать в аудио контент.")
language = "ru"
speaker = "Tanja Adelina"
out_file = "audio_out/Tanja_Adelina.wav"

# Запуск обработки текста
tts.tts_to_file(text=text,
                speaker=speaker,
                language=language,
                file_path=out_file)
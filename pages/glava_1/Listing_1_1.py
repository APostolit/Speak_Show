# Листинг 1.1
import torch
from TTS.api import TTS

# Получить устройство
device = "cuda" if torch.cuda.is_available() else "cpu"
print('Устройство:', device)

# Получит список доступных TTS моделей
models = TTS().list_models()
# Сохранить список моделей в текстовом файле
with open('text_out/models_CoquiTTS.txt', 'w', encoding='utf-8') as file:
    i = 1
    for model in models:
        file.write(str(i) + '. ' + model + '\n')  # Добавляем перенос строки
        i += 1

# Загрузить TTS модель
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

# Получить список доступных спикеров
speakers = tts.speakers
# Сохранить список спикеров в текстовом файле
with open('text_out/speakers_xtts_v2.txt', 'w', encoding='utf-8') as file:
    i = 1
    for speaker in speakers:
        file.write(str(i) + '. ' + speaker + '\n')  # Добавляем перенос строки
        i += 1
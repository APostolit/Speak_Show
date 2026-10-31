# Листинг 2.3
import torch
from silero_tts.silero_tts import SileroTTS

device = "cuda" if torch.cuda.is_available() else "cpu"
text_file = "text_inp/forum.txt"
# Загрузить текстовый файл
with open(text_file, "r") as file:
    text = file.read()

# Создание TTS объекта (Мужской голос)
tts = SileroTTS(model_id='v5_ru', language='ru', speaker='eugene',
                sample_rate=24000, device=device)
# Формирование аудио файла
tts.tts(text, 'audio_out/eugene_ru.wav')

# Создание TTS объекта (Женский голос)
tts = SileroTTS(model_id='v5_ru', language='ru', speaker='baya',
                sample_rate=24000, device=device)
# Формирование аудио файла
tts.tts(text, 'audio_out/baya_ru.wav')
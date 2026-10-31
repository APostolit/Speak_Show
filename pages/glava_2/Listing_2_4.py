# Листинг 2.4
import torch
from silero_tts.silero_tts import SileroTTS

device = "cuda" if torch.cuda.is_available() else "cpu"
text_file = "text_inp/forum_en.txt"
# Загрузить текстовый файл
with open(text_file, "r") as file:
    text = file.read()

# Создание TTS объекта (Мужской голос)
tts = SileroTTS(model_id='v3_en_indic', language='en', speaker='kannada_male',
                sample_rate=24000, device=device)
# Формирование аудио файла
tts.tts(text, 'audio_out/forum_en_male.wav')

# Создание TTS объекта (Женский голос)
tts = SileroTTS(model_id='v3_en_indic', language='en', speaker='kannada_female',
                sample_rate=24000, device=device)
# Формирование аудио файла
tts.tts(text, 'audio_out/forum_en_female.wav')
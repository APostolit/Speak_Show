# Листинг 4.1
from omnivoice import OmniVoice
import soundfile as sf

# Загрузка модели
model = OmniVoice.from_pretrained("k2-fsa/OmniVoice")

# Исходный текст
text = ("Добрый день. Это образец аудио файла с параметрами по умолчанию."
        "Образец этого голоса можно использовать для озвучивания"
        " любых текстов на русском языке.")

# Формирование аудио дорожки
audio = model.generate(text=text)

# Запись аудио дорожки на диск
sample_rate = 24000
output_file = 'audio_out/spiker_1.mp3'
# output_file = 'audio_out/spiker_f1.wav'
sf.write(output_file, audio[0], sample_rate)
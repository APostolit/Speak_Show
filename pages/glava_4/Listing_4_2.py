# Листинг 4.2
from omnivoice import OmniVoice
import soundfile as sf

model = OmniVoice.from_pretrained("k2-fsa/OmniVoice")

text = ("Добрый день. Это образец аудио файла с заданными параметрами: "
        "мужчина, средний возраст, низкий тембр, русский акцент."
        "Образец этого мужского голоса можно использовать для озвучивания"
        " любых текстов на русском языке.")

instruct="male, middle-aged, low pitch, russian accent"

audio = model.generate(text=text, instruct=instruct)

# Запись аудио данных на диск
sample_rate = 24000
output_file = 'audio_out/spiker_m_ru.mp3'
sf.write(output_file, audio[0], sample_rate)
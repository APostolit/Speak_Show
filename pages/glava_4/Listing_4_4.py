# Листинг 4.4
from omnivoice import OmniVoice
import soundfile as sf

model = OmniVoice.from_pretrained("k2-fsa/OmniVoice")

text = ("Ходит осень в нашем парке. Дарит осень всем подарки. "
        "Фартук розовый — осинке. Бусы красные — рябинке. "
        "Образец этого детского голоса можно использовать для озвучивания"
        " любых детских стихов на русском языке.")

instruct="female, child, high pitch, russian accent"

audio = model.generate(text=text, instruct=instruct)

# Запись аудио данных на диск
sample_rate = 24000
output_file = 'audio_out/spiker_c_ru.mp3'
sf.write(output_file, audio[0], sample_rate)
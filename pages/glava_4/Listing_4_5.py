# Листинг 4.5
from omnivoice import OmniVoice
import soundfile as sf

model = OmniVoice.from_pretrained("k2-fsa/OmniVoice")

text = ("Good afternoon. This is a sample audio file with the specified parameters: "
        "female, middle age, medium timbre, English accent. "
        "This sample of a female voice can be used to voice any texts in English."
        )

instruct="female, middle-aged, low pitch, british accent"

audio = model.generate(text=text, instruct=instruct)

# Запись аудио данных на диск
sample_rate = 24000
output_file = 'audio_out/spiker_f_en.mp3'
sf.write(output_file, audio[0], sample_rate)
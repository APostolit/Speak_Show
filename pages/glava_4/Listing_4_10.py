# Листинг 4.10
from omnivoice import OmniVoice
import soundfile as sf
import torch

def made_audio(in_txt_file, audio_in, audio_out):
    # Загрузка модели
    model = OmniVoice.from_pretrained("k2-fsa/OmniVoice",
                                      device_map="cuda:0",
                                      dtype=torch.float16)
    # Загрузить текст файла
    with open(in_txt_file, "r", encoding="utf-8") as f:
        text = f.read()

    # Создание аудио дорожки
    audio = model.generate(text=text,
                           language_id="ru",
                           # speed=0.7,
                           # duration=48,
                           ref_audio=audio_in,)
    # Запись аудио файла
    sf.write(audio_out, audio[0], 24000)

if __name__ == '__main__':
    text_in = 'text_inp/forum.txt'
    audio_in = "audio_out/spiker_2.mp3"
    audio_out = "audio_out/forum_norm.mp3"
    made_audio(text_in, audio_in, audio_out)
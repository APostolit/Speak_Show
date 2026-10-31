# Листинг 3.3
from gtts import gTTS
from pydub import AudioSegment

def made_audio(in_file_txt, lin, out_audio_file):
    # Загрузить текст файла
    with open(in_file_txt, "r", encoding="utf-8") as f:
        text = f.read()

    # Озвучивание текста
    tts = gTTS(text=text, lang=lin)
    tts.save(out_audio_file)

    # Конвертировать в MP3 со сжатием
    wav_audio = AudioSegment.from_mp3(out_audio_file)
    wav_audio.export(out_audio_file, format='mp3')

if __name__ == '__main__':
    # Можно замедлить slow=True
    in_file = "text_inp/forum_en.txt"
    ling = 'en'
    out_file = "audio_out/forum_2_en.mp3"
    made_audio(in_file, ling, out_file)
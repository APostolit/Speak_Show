# Листинг 5.2
import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence
import glob
from moviepy.editor import *

#####################################
# Распознавание речи в видео файлах #
#####################################
def transcribe_video(path_v, path_a, out_txt, lang):
    # Извлечь аудио дорожку из видео файла
    video = VideoFileClip(path_v)
    video.audio.write_audiofile(path_a)

    # Создать объект распознавания речи
    r = sr.Recognizer()
    # Откройте аудиофайл с помощью pydub
    sound = AudioSegment.from_wav(path_a)
    # Разделите аудио файл на фрагменты, в которых пауза более 700 мс.
    chunks = split_on_silence(sound, min_silence_len=700,
                              silence_thresh=sound.dBFS - 14,
                              keep_silence=700)

    # Создайте папку для хранения фрагментов аудиофайлов
    folder_name = "audio-chunks"
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)

    whole_text = ""
    # Обработка каждого фрагмента аудио файла
    for i, audio_chunk in enumerate(chunks, start=1):
        # Экспортируйте фрагмент и сохраните в папке
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        # Распознать текст фрагмента аудио файла
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            # Преобразовать аудио в текст
            try:
                text = r.recognize_google(audio_listened, language=lang)
                # Сделать первую букву строки заглавной
                text = f"{text.capitalize()}. "
            except sr.UnknownValueError as e:
                text = 'ОШИБКА В РАСПОЗНАВАНИИ. '
            else:
                pass

            # Объединить фрагменты текста
            whole_text += text

    # Сохранить полный текст в текстовый файл
    with open(out_txt, 'w', encoding='utf-8') as f:
        f.write(whole_text)

    # Удалить не актуальные аудио файлы
    for f in glob.glob(os.path.join(folder_name, "chunk*.wav")):
        os.remove(f)
    # Удалить обработанную аудио дорожку видео файла
    # os.remove(path_a)
    return

if __name__ == "__main__":
    # Путь к исходному видео
    path_video = 'video_inp/leonov.mp4'
    # Путь к создаваемой аудио дорожке
    path_audio = 'audio_out/leonov.wav'
    # Путь к создаваемому текстовому файлу
    path_txt = 'text_out/leonov.txt'
    ling = 'ru-RU'
    # Обращение к функции транскрибирования
    transcribe_video(path_video, path_audio, path_txt, ling)
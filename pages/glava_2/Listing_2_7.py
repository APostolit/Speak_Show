# Листинг 2.7
import os
import re
import torch
import soundfile as sf
import combi_audio

# Функция для разбиения текста на блоки,
# не превышающие max_len символов, с учётом границ предложений
def split_text(text, max_len=900):
    sentences = re.split(r'(?<=[.?!])\s+', text)
    blocks = []
    current_block = ""
    for sentence in sentences:
        if len(current_block) + len(sentence) + 1 <= max_len:
            current_block = current_block + " " + sentence\
                if current_block else sentence
        else:
            if current_block:
                blocks.append(current_block.strip())
            # Если само предложение слишком длинное, разбиваем его на части
            if len(sentence) > max_len:
                parts = [sentence[i:i+max_len]
                         for i in range(0, len(sentence), max_len)]
                blocks.extend([part.strip() for part in parts])
                current_block = ""
            else:
                current_block = sentence
    if current_block:
        blocks.append(current_block.strip())
    return blocks

# Рекурсивная функция синтеза аудио из одного блока.
def synthesize_block(model, speaker,sample_rate, text, index, prefix="block"):
    try:
        # Генерируем аудио с помощью метода apply_tts модели
        audio = model.apply_tts(ssml_text=text,
                                speaker=speaker,
                                sample_rate=sample_rate,
                                put_accent=True,
                                put_yo=True,
                                put_stress_homo=True,
                                put_yo_homo=True)

        # Формируем путь для сохранения файла: temp_audi/res_{index}.wav
        file_path = os.path.join("temp_audi", f"res_{index}.mp3")

        # Запись фрагмента аудио файла на диск
        sf.write(file_path, audio, sample_rate)
        return [file_path]

    # Если возникает ошибка (например, блок слишком длинный),
    # текст делится на две части.
    except Exception as e:
        print(f"Ошибка при синтезе {prefix} {index}: {e}")
        # Если текст слишком короткий, чтобы делить его дальше,
        # пробрасываем исключение
        if len(text) < 50:
            raise e
        # Делим текст на две части, стараясь разрезать по границе предложения
        mid = len(text) // 2
        split_index = text.rfind('.', 0, mid)
        if split_index == -1:
            split_index = mid
        part1 = text[:split_index+1].strip()
        part2 = text[split_index+1:].strip()
        paths1 = synthesize_block(model, speaker,sample_rate, part1,
                                  f"{index}_1", prefix=prefix)
        paths2 = synthesize_block(model, speaker,sample_rate, part2,
                                  f"{index}_2", prefix=prefix)
        return paths1 + paths2

# Основная функция ----------------------------------------------------------
def long_file(local_model, input_txt_file, speaker, sample_rate, rate, pitch,
              out_audio):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    torch.set_num_threads(4)

    # Загрузка модели Silero TTS (версия V5)
    model = torch.package.PackageImporter(local_model).load_pickle("tts_models",
                                                                   "model")
    model.to(device)

    # Создаем папку temp_audi, если она не существует
    os.makedirs("temp_audi", exist_ok=True)

    # Читаем текст из исходного файла
    with open(input_txt_file, "r", encoding="utf-8") as file:
        full_text = file.read()

    # Обращение к функции разделения текст на блоки
    blocks = split_text(full_text, max_len=400)

    all_audio_paths = []
    # Форматируем индекс верхнего уровня как трехзначное число
    for i, block in enumerate(blocks, 1):
        index_str = f"{i:03d}"
        # Добавление разметки к блоку текста
        tex_start = '<speak>\n'
        tex_start += '<prosody rate="' + rate + '"' + ' pitch="' + pitch + '">\n'
        tex_end = '</prosody>\n'
        tex_end += '</speak>'
        block = tex_start + block + tex_end
        # Обращение к функции формирования аудио из текста -------------------
        paths = synthesize_block(model, speaker, sample_rate, block, index_str,
                                 prefix="block")
        all_audio_paths.extend(paths)

    # Объединить фрагменты аудио файлов
    directory = 'temp_audi'  # Папка с фрагментами аудио файлов
    combi_audio.sum_files(directory, out_audio)

    # Удалить фрагменты аудио файлов из временной директории
    os.chdir(directory)
    all_files = os.listdir()
    for f in all_files:
        os.remove(f)

if __name__ == '__main__':
    loc_model = 'models/v5_ru.pt'
    sample_r = 24000
    txt_file = 'text_inp/forum_1.txt'

    # Мужской голос
    lector = 'eugene'      # Мужской голос, быстрый
    rate_speed = "slow"  # Темп речи, замедленный
    pitch_niz = "low"      # Тембр речи, чуть ниже среднего
    out_audio_file = 'audio_out/forum_l_eugene.mp3'
    long_file(loc_model, txt_file, lector, sample_r, rate_speed, pitch_niz,
              out_audio_file)
    '''
    lector = 'xenia'  # Женский голос, спокойный
    rate_speed = "medium"  # Темп речи, средний
    pitch_niz = "low"      # Тембр речи, чуть ниже среднего
    out_audio_file = 'audio_out/forum_l_xenia.mp3'
    long_file(loc_model, txt_file, lector, sample_r, rate_speed, pitch_niz,
     out_audio_file)
    '''

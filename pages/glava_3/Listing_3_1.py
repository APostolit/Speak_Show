# Листинг 3.1
from gtts.lang import tts_langs

# Получить список доступных языков
languages = tts_langs()

with open('text_out/languages_gtts.txt', 'w', encoding='utf-8') as file:
    i = 1
    for key, value in languages.items():
        str_txt = f"{key}: {value}"
        file.write(str(i) + '. ' + str_txt + '\n')  # Добавляем перенос строки
        i += 1
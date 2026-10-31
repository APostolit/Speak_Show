# Листинг 2.1
from silero_tts.silero_tts import SileroTTS

# Получение доступных моделей
models = SileroTTS.get_available_models()

with open('text_out/models_SileroTTS.txt', 'w', encoding='utf-8') as file:
    i = 1
    for key, value in models.items():
        str_txt = f"{key}: {value}"
        file.write(str(i) + '. ' + str_txt + '\n')  # Добавляем перенос строки
        i += 1
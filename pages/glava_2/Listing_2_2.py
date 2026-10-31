# Листинг 2.2
from silero_tts.silero_tts import SileroTTS

ling = 'ru'
# Получить последнюю версию модели для заданного языка
latest_model = SileroTTS.get_latest_model(ling)

# Получите доступную частоту дискретизации для конкретной модели и языка
sample_rates = SileroTTS.get_available_sample_rates_static(ling, latest_model)
rates = ''
for el in sample_rates:
    rates += str(el) + ', '

# Создание TTS объекта
tts = SileroTTS(model_id=latest_model, language=ling, sample_rate=48000,
                device='cpu')
# Получение доступных спикеров для созданной модели
speakers = tts.get_available_speakers()
dictors = ''
for el in speakers:
    dictors += str(el) + ', '

with open('text_out/SileroTTS_ru.txt', 'w', encoding='utf-8') as file:
    file.write('Последняя модель' + '\n')
    file.write(latest_model + '\n')
    file.write('Частота дискретизации' + '\n')
    file.write(rates + '\n')
    file.write('Доступные спикеры' + '\n')
    file.write(dictors)

# -----------------------------------------
ling = 'en'
# Получить последнюю версию модели для заданного языка
latest_model = SileroTTS.get_latest_model(ling)

# Получите доступную частоту дискретизации для конкретной модели и языка
sample_rates = SileroTTS.get_available_sample_rates_static(ling, latest_model)

rates = ''
for el in sample_rates:
    rates += str(el) + ', '

# Создание TTS объекта
tts = SileroTTS(model_id=latest_model, language=ling, sample_rate=48000,
                device='cpu')
# Получение доступных спикеров для созданной модели
speakers = tts.get_available_speakers()

dictors = ''
for el in speakers:
    dictors += str(el) + ', '

with open('text_out/SileroTTS_en.txt', 'w', encoding='utf-8') as file:
    file.write('Последняя модель' + '\n')
    file.write(latest_model + '\n')
    file.write('Частота дискретизации' + '\n')
    file.write(rates + '\n')
    file.write('Доступные спикеры' + '\n')
    file.write(dictors)
# Листинг 2.5
import torch
import soundfile as sf

# Устройство обработки данных
device = "cuda" if torch.cuda.is_available() else "cpu"

# Создание модели
loc_model_v5_ru = 'models/v5_ru.pt'
model = torch.package.PackageImporter(loc_model_v5_ru).load_pickle("tts_models",
                                                                   "model")
model.to(device)

# Создание текстовой переменной с разметкой SSML
ssml_sample = """
              <speak>
              С использованием разметки текста можно настроить,
              <prosody rate="x-slow"> очень медленную речь</prosody>.
              Или увеличить темп речи, например, в скороговорках.
              <prosody rate="fast">Карл у Клары украл кораллы,
               а Клара у Карла украла кларнет.</prosody>
              <prosody rate="medium"> А потом перейти к обычному темпу
               речи, но сменить высоту тона,</prosody>.
              <prosody pitch="x-high"> Можно говорить высоким голосом
               </prosody>,
              <prosody pitch="x-low">или перейти на низкий голос</prosody>.
              А еще можно делать паузы любой длины, например две секунды
               <break time="2000ms"/>.
              Также можно правильно расставлять ударения.
              Перед глазами принца открылся вид на прекрасный з+амок.
              На дверь повесили массивный зам+ок.
              </speak>
              """
# Задание параметров обработки аудио
sample_rate = 24000
speaker = 'xenia'
# Создание аудио данных
audio = model.apply_tts(ssml_text=ssml_sample,
                        speaker=speaker,
                        sample_rate=sample_rate,
                        put_accent=True,
                        put_yo=True
                        )
# Запись аудио данных на диск
output_file = 'audio_out/xenia_ssml.mp3'
sf.write(output_file, audio, sample_rate)
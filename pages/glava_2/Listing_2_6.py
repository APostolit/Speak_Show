import torch
import soundfile as sf

def made_audio(model, sample_rate, speaker, txt_input, output_file, rate, pitch):
    # Получить устройство
    device = "cuda" if torch.cuda.is_available() else "cpu"

    # Загрузка текстового файла в текстовую переменную
    with open(txt_input, "r") as file:
        text_0 = file.read()

    # Формирование текстовой переменной с разметкой
    tex_start = '<speak>\n'
    tex_start += '<prosody rate="' + rate + '"' + ' pitch="' + pitch + '">\n'
    tex_end = '</prosody>\n'
    tex_end += '</speak>'
    text = tex_start + text_0 + tex_end

    # здание модели
    model = torch.package.PackageImporter(model).load_pickle("tts_models", "model")
    model.to(device)

    # Синтезирование речи из текстовой переменной с разметкой
    audio = model.apply_tts(ssml_text=text, speaker=speaker,
                            sample_rate=sample_rate, put_accent=True,
                            put_yo=True, put_stress_homo=True, put_yo_homo=True)
    # Запись аудио файла
    sf.write(output_file, audio, sample_rate)
    return

if __name__ == '__main__':
    model_v5_ru = 'models/v5_ru.pt'
    smp_rate = 24000
    file_in_txt = 'text_inp/forum_p.txt'
    # Мужской голос
    speak = 'eugene'
    file_out = 'audio_out/forum_p_eugene.mp3'
    rate_speed = "slow"  # темп
    pitch_niz = "x-low"  # высота тона
    made_audio(model_v5_ru, smp_rate, speak, file_in_txt, file_out,
               rate_speed, pitch_niz)
    # Женский голос
    speak = 'xenia'
    rate_speed = "fast"  # темп
    pitch_niz = "high"    # высота тона
    file_out = 'audio_out/forum_p_xenia.mp3'
    made_audio(model_v5_ru, smp_rate, speak, file_in_txt, file_out,
               rate_speed, pitch_niz)
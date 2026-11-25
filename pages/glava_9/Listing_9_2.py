# Листинг 9.2
import ffmpeg
import os

def mirror(file_inp,file_out):
    # Читаем видеофайл
    video_input = ffmpeg.input(file_inp)
    # Применяем горизонтальное отражение
    flipped_video = video_input.hflip()
    # Сохраняем аудиодорожку
    audio_input = video_input.audio
    # Создаём выходной поток, указывая видео и аудио
    output_stream = ffmpeg.output(flipped_video, audio_input, file_out)
    # Запускаем обработку
    ffmpeg.run(output_stream, overwrite_output=True)

if __name__ == '__main__':
    # Текущий каталог
    exe_path = os.getcwd()
    input_file = exe_path + '/video_in/Мама.mp4'
    output_file = exe_path + '/video_in/Мама_2.mp4'
    mirror(input_file, output_file)
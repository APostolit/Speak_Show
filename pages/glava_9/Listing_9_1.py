# Листинг 9.1
import ffmpeg
import os

def revers_video(file_inp,file_out):
    input_video = ffmpeg.input(file_inp)
    output_video = input_video.filter("reverse")  # Переворачиваем видеоряд
    ffmpeg.output(output_video, file_out).run(overwrite_output=True)

if __name__ == '__main__':
    # Текущий каталог
    exe_path = os.getcwd()
    input_file = exe_path + '/video_in/Юрский_образец.mp4'
    output_file = exe_path + '/video_in/Юрский_образец_2.mp4'
    revers_video(input_file, output_file)

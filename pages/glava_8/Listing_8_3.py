# Листинг 8.3
import subprocess
import os

def made_avatar(file_py_path, inp_img, inp_vid):
    # Формируем команду для запуска модуля inference.py с параметрами
    command = ['python', file_py_path, '-s' + inp_img, '-d' + inp_vid]
    # Процесс создания видео
    subprocess.run(command)

if __name__ == '__main__':
    pr_path = os.getcwd()
    file_py_path = os.path.join(pr_path, "LivePortrait/inference.py")
    inp_img = 'images/Puskin.png'
    inp_vid = 'video/Moroz.mp4'
    made_avatar(file_py_path, inp_img, inp_vid)
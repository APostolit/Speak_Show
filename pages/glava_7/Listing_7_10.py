# Листинг 7.10
from rembg import remove
from PIL import Image

# Исходное изображение
input_image = Image.open('Boris.jpg')
# Удаление фона
output_image = remove(input_image)
# Итоговое изображение
output_image.save('no_bg.png')
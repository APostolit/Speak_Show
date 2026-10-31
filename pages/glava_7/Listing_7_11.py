# Листинг 7.11
from rembg import remove, new_session
from PIL import Image

# Загрузка модели для многократного использования
session = new_session("birefnet-general")
# Исходное изображение
img = Image.open("volos.png")
# Удаление фона
result = remove(img, session=session)
# Итоговое изображение
result.save("volos_no_bg.png")

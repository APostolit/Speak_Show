# Листинг 7.8
from PIL import Image

##################################
# Гравировка изображений точками #
##################################
class gravure:
    def __init__(self, inp_fl, out_fl):
        self.image_fl = inp_fl
        self.alpha_fl = out_fl
        # загрузить изображение
        im = Image.open(inp_fl)
        im = im.convert('1')
        im = im.convert(mode='1', dither=Image.FLOYDSTEINBERG)  # Нарисовать
        im.save(out_fl)  # Сохранить
        return

if __name__ == "__main__":
    inp_image = 'img_inp/AV_500.jpg'     # исходный рисунок
    out_image = 'img_out/av_gravure.jpg' # гравюра
    # создать объект класса
    gravure(inp_image, out_image)

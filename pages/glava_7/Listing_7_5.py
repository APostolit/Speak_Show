# Листинг 7.5
import os
from PIL import Image
import M_S_21  # стилизация изображения (листинг 7.2)
# Суммирование переднего плана и фона
from Get_Sum_FgBg import get_sum_fgbg
import numpy as np

#####################################
# Класс вариантов тонкой стилизации #
#####################################
class made_style_21():
    def __init__(self, model_style=None, input_im=None, input_st=None, size=None,
                 out_img=None):
        self.model_style = model_style  # модель стиля
        self.input_im = input_im  # имя исходного рисунка
        self.input_st = input_st  # имя рисунка со стилем
        self.size = size
        self.out_img = out_img
        # Текущий каталог
        self.dir_p = os.getcwd()

    ######################################
    # Обработчик события стилизация фона #
    ######################################
    def create_style_fon(self):
        # Обращение к внешнему модулю стилизации M_S_21
        M_S_21.styl_21(self.input_im, self.input_st, self.size)

        # формирование параметров для суммирования
        # исходный рисунок
        input_image = self.dir_p + '/temp/fg.png'
        # имя файла маски переднего плана
        input_alpha = self.dir_p + '/alpha/al_maska.png'
        # стилизованный фон
        input_fonnn = self.dir_p + '/pages/style_2/img_out/temp_style.jpg'

        input_fon = Image.open(input_fonnn)  # загрузить фон
        h, w = input_fon.size  # получить размеры изображения

        input_img = Image.open(input_image)  # загрузить изображение
        h1, w1 = input_img.size
        if h1 != h or w1 != w:
            input_img = input_img.resize(input_fon.size)

        input_alp = Image.open(input_alpha)  # загрузить альфа маска
        h1, w1 = input_alp.size
        if h1 != h or w1 != w:
            input_alp = input_alp.resize(input_fon.size)

        # формирование 0-маски изображения для смешивания, массив np
        mask3 = np.zeros((w, h, 3), dtype=np.uint8)
        # преобразование массив np в изображение PLL - RGB
        mask3 = Image.fromarray(mask3.astype(np.uint8))
        # это вставило передний план в черный фон по маске
        mask3.paste(input_img, (0, 0), input_alp)
        # это вставило передний план в новый фон по маске
        input_fon.paste(input_img, (0, 0), input_alp)

        # сохранить стилизованный фон с передним планом
        self.out_img = self.dir_p + '/pages/style_2/img_out/temp.jpg'
        input_fon.save(self.out_img)
        return

    #################################################
    # Обработчик события стилизация переднего плана #
    #################################################
    def create_style_pp(self):
        # Обращение к внешнему модулю стилизации M_S_21
        M_S_21.styl_21(self.input_im, self.input_st, self.size)

        # формирование параметров для суммирования
        # имя файла стилизованного переднего плана
        input_image = self.dir_p + '/pages/style_2/img_out/temp.jpg'
        # имя файла маски переднего плана
        input_alpha = self.dir_p + '/alpha/al_maska.png'
        # исходный фон (может быть и исходный рисунок)
        input_fonnn = self.dir_p + '/temp/bg.png'
        # -----------------
        # суммирование фона со стилизованным передним планом
        # создать объект класса
        my_sum_fgbg = get_sum_fgbg(input_image, input_alpha, input_fonnn)
        img_sum = my_sum_fgbg.out_sum  # получить сумму фона и переднего плана

        # сохранить стилизованный передний план
        self.out_img = self.dir_p + '/pages/style_2/img_out/temp.jpg'
        img_sum.save(self.out_img)
        return

    ###################################################
    # Обработчик события стилизация всего изображения #
    ###################################################
    def create_style(self):
        # стилизация изображения модуль M_S_21.py, класс styl_21
        M_S_21.styl_21(self.input_im, self.input_st, self.size)
        return


# ############# конец класса №№№№№№№№№№№№№№№№№

if __name__ == "__main__":
    # Текущая директория
    exe_path = os.getcwd()
    # Формирование свойств класса
    # Изображение с образцом стиля
    path_style_img = exe_path + '/pages/style_2/21styles/mosaic_ducks_massimo.jpg'
    siz = 1024  # Размер итогового изображения
    # Создание объекта класса
    styler = made_style_21()

    # Стилизация всего изображения
    # исходное изображение
    styler.input_im = exe_path + '/pages/style_2/img_inp/temp.png'
    styler.input_st = path_style_img
    styler.size = siz
    styler.create_style()
    '''
    # Стилизация переднего плана
    path_in_img = exe_path + '/temp/fg.png'  # передний план
    styler.input_im = path_in_img
    styler.input_st = path_style_img
    styler.size = siz
    styler.create_style_pp()

    # Стилизация фона
    path_in_img = exe_path + '/temp/bg.png'  # фон
    styler.input_im = path_in_img
    styler.input_st = path_style_img
    styler.size = siz
    styler.create_style_fon()
    '''
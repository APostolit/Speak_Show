# Листинг 7.6
from Made_Al_Mask import al_mask # (см. Листинг 7.4)
from Made_Fg_Bg import made_fg_bg # (см. Листинг 7.7)
import cv2

#############################################
# Класс формирования переднего плана и фона #
#############################################
class get_fg_bg:
    def __init__(self, image_fl, in_klass):
        self.in_im_file = image_fl  # исходный рисунок
        self.in_class = in_klass    # распознаваемый класс (объект)

        # создать маску
        my_alpha = al_mask(self.in_class, self.in_im_file)  # создать объект класса
        input_alpha = './alpha/al_maska.png'

        # получить передний план и фон
        my_fg_bg = made_fg_bg(self.in_im_file, input_alpha)  # создать объект класса
        self.fg = my_fg_bg.fg  # получить передний план
        self.bg = my_fg_bg.bg  # получить фон
        return
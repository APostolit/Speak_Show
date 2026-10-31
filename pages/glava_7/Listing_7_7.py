# Листинг 7.7
import cv2

#############################################
# Класс формирования переднего плана и фона #
#############################################
class made_fg_bg:
    def __init__(self, image_fl, alpha_fl):
        self.image_fl = image_fl
        self.alpha_fl = alpha_fl
        # загрузить изображение
        self.input_img = cv2.imread(self.image_fl)
        # загрузить альфа маска
        self.input_alp = cv2.imread(self.alpha_fl)
        # получить передний план по маске
        self.fg = cv2.bitwise_and(self.input_img, self.input_alp)
        # получить фон
        self.bg = cv2.addWeighted(self.input_img, 1, self.input_alp, 1, 0.0)
        return

if __name__ == "__main__":
    input_image = 'images/volos1.png'    # исходный рисунок
    input_alpha = 'alpha/al_maska.png'   # исходный альфа маска
    # создать объект класса
    my_fg_bg = made_fg_bg(input_image, input_alpha)
    fg = my_fg_bg.fg  # получить передний план
    bg = my_fg_bg.bg  # получить фон

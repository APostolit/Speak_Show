# Листинг 7.4
import cv2
import torch
from torchvision import transforms
import numpy as np
import os

###########################################
# Класс формирования альфа маски, тримапа #
# переднего и заднего плана               #
###########################################
class al_mask:
    def __init__(self, in_class, in_im_file, al_mask_file, trimap_file, fg_file,
                 bg_file):
        self.in_class = in_class
        self.in_im_file = in_im_file
        self.al_mask_file = al_mask_file
        self.trimap_file = trimap_file
        self.fg_file = fg_file
        self.bg_file = bg_file

        # задать классы распознаваемых объектов
        CLASS_MAP = {"background": 0, "aeroplane": 1, "bicycle": 2, "bird": 3,
                     "boat": 4, "bottle": 5, "bus": 6, "car": 7, "cat": 8,
                     "chair": 9, "cow": 10, "diningtable": 11, "dog": 12,
                     "horse": 13, "motorbike": 14, "person": 15, "potted plant": 16,
                     "sheep": 17, "sofa": 18, "train": 19, "tv/monitor": 20}
        # загрузка модели
        model = torch.hub.load('pytorch/vision:v0.27.0', 'deeplabv3_resnet101',
                               pretrained=True)
        model.eval()

        input_image = cv2.imread(self.in_im_file)  # загрузить входное изображение
        input_img = input_image  # сохранить временно
        input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)
        # преобразовать в RGB
        preprocess = transforms.Compose([transforms.ToTensor(),
                                         transforms.Normalize(
                                             mean=[0.485, 0.456, 0.406],
                                             std=[0.229, 0.224, 0.225]), ])
        input_tensor = preprocess(input_image)
        # создайте мини-пакет в соответствии с ожиданиями модели
        input_batch = input_tensor.unsqueeze(0)
        with torch.no_grad():
            output = model(input_batch)['out'][0]
            output = torch.softmax(output, 0)
        # сформированная альфа-маска
        output_cat = output[CLASS_MAP[self.in_class], ...].numpy()
        self.amask = output_cat
        self.output_map = output_cat * 255
        cv2.imwrite(self.al_mask_file, self.output_map)  # сохранить альфа маску

        # формирование тримапа
        conf_threshold = 0.50
        # обращение к функции создания тримапа
        trimap_image = self.trimap(output_cat, 7, conf_threshold)
        # сохранение готового тримапа
        cv2.imwrite(self.trimap_file, trimap_image)

        # Загрузить альфа маску
        self.input_alp = cv2.imread(self.al_mask_file)

        # получить передний план по маске
        self.fg = cv2.bitwise_and(input_img, self.input_alp)
        cv2.imwrite(self.fg_file, self.fg)  # сохранить передний план

        # получить фон по маске
        self.bg = cv2.addWeighted(input_img, 1, self.input_alp, 1, 0.0)
        cv2.imwrite(self.bg_file, self.bg)  # сохранить фон
        return

    # функция создания тримапа
    def trimap(self, probs, size, conf_threshold):
        mask = (probs > 0.05).astype(np.uint8) * 255
        pixels = 2 * size + 1
        kernel = np.ones((pixels, pixels), np.uint8)
        dilation = cv2.dilate(mask, kernel, iterations=1)
        remake = np.zeros_like(mask)
        # Установите каждый пиксель в качестве возможного переднего плана
        remake[dilation == 255] = 127
        # Установите каждый пиксель в качестве определенного переднего плана.
        remake[probs > conf_threshold] = 255
        return remake

if __name__ == "__main__":
    # Текущая директория стилизации
    exe_path = os.getcwd() + '/pages/style_2'
    # Текущая директория проекта
    my_dir = os.getcwd()
    # Формирование свойств класса
    in_class = 'person'  # распознаваемый класс (объект)
    in_im_file = exe_path + '/img_inp/volos.png'        # исходное изображение
    al_mask_file = my_dir +'/alpha/volos_mask.png'      # альфа маска
    trimap_file = my_dir + '/trimaps/volos_trimap.png'  # тримап
    fg_file = my_dir + '/temp/volos_fg.png'             # передний план
    bg_file = my_dir + '/temp/volos_bg.png'             # задний план
    # создать объект класса
    al_mask(in_class, in_im_file, al_mask_file, trimap_file, fg_file, bg_file)

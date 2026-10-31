# Листинг 7.2
from net import Net
import torch
from torch.autograd import Variable
from PIL import Image
import numpy as np
import os

class style_21:
    def __init__(self, model, image, style, out_img, size):
        self.image = image
        self.style = style
        self.model = model
        self.content_size = size
        self.style_size = 512
        self.ngf = 128
        self.cuda = 0
        self.output_image = out_img

        content_image = self.tensor_load_rgbimage(self.image, size=self.content_size,
                                                  keep_asp=True)
        content_image = content_image.unsqueeze(0)
        style = self.tensor_load_rgbimage(self.style, size=self.style_size)
        style = style.unsqueeze(0)
        style = self.preprocess_batch(style)

        style_model = Net(ngf=self.ngf)
        model_dict = torch.load(self.model)
        model_dict_clone = model_dict.copy()
        for key, value in model_dict_clone.items():
            if key.endswith(('running_mean', 'running_var')):
                del model_dict[key]
        style_model.load_state_dict(model_dict, False)

        if self.cuda:
            style_model.cuda()
            content_image = content_image.cuda()
            style = style.cuda()

        style_v = Variable(style)
        content_image = Variable(self.preprocess_batch(content_image))
        style_model.setTarget(style_v)
        output = style_model(content_image)
        # Сохранить итоговый стиль
        self.tensor_save_bgrimage(output.data[0], self.output_image)
        # self.tensor_save_bgrimage(output.data[0], self.output_style)
        return

    def tensor_load_rgbimage(self, filename, size=None, scale=None, keep_asp=False):
        img = Image.open(filename).convert('RGB')
        if size is not None:
            if keep_asp:
                size2 = int(size * 1.0 / img.size[0] * img.size[1])
                img = img.resize((size, size2), Image.Resampling.LANCZOS)
            else:
                img = img.resize((size, size), Image.Resampling.LANCZOS)

        elif scale is not None:
            img = img.resize((int(img.size[0] / scale), int(img.size[1] / scale)),
                             Image.Resampling.LANCZOS)
        img = np.array(img).transpose(2, 0, 1)
        img = torch.from_numpy(img).float()
        return img

    def preprocess_batch(self, batch):
        batch = batch.transpose(0, 1)
        (r, g, b) = torch.chunk(batch, 3)
        batch = torch.cat((b, g, r))
        batch = batch.transpose(0, 1)
        return batch

    def tensor_save_bgrimage(self, tensor, filename, cuda=False):
        (b, g, r) = torch.chunk(tensor, 3)
        tensor = torch.cat((r, g, b))
        self.tensor_save_rgbimage(tensor, filename, cuda)
        return

    def tensor_save_rgbimage(self, tensor, filename, cuda=False):
        if cuda:
            img = tensor.clone().cpu().clamp(0, 255).numpy()
        else:
            img = tensor.clone().clamp(0, 255).numpy()
        img = img.transpose(1, 2, 0).astype('uint8')
        img = Image.fromarray(img)
        img.save(filename)

if __name__ == "__main__":
    exe_path = os.getcwd() + '/pages/style_2'          # Текущая директория
    model_21 = exe_path + '/model_21/21styles.model'   # Модель
    path_in_img = exe_path + '/img_inp/av.png'         # Исходное изображение
    path_style_img = exe_path + '/21styles/udnie.jpg'  # Изображение стиля
    path_out_img = exe_path + '/img_out/av_style.jpg'  # Обработанное изображение
    out_size = 512  # Размер итогового изображение
    # Стилизовать
    style_21(model_21, path_in_img, path_style_img, path_out_img, out_size)

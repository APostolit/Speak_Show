# Листинг 6.3
from diffusers import StableDiffusionPipeline
import torch

def generator(prompt, name_file):
    # Выбор модели
    model_id = "dreamlike-art/dreamlike-diffusion-1.0"

    # Загрузка модели
    pipe = StableDiffusionPipeline.from_pretrained(model_id,
                                                   torch_dtype=torch.float16)
    # Перемещение модели на GPU (если доступно)
    pipe = pipe.to("cuda")
    # Генерация изображения
    image = pipe(prompt).images[0]
    # Сохранение изображения
    image.save(name_file)

if __name__ == '__main__':
    txt = "An image of a women in Picasso style"
    image_name = "img_out/w_picasso.jpg"
    generator(txt, image_name)
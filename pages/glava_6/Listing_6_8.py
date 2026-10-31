# Листинг 6.8
from diffusers import StableDiffusionPipeline
import torch

def generator(prompt, name_file):
    # Выбор модели
    model_id = "dreamlike-art/dreamlike-photoreal-2.0"

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
    txt = ("A very beautiful Kazakh girl, a TV presenter, with short dark hair, "
           " background - TV news studio, hyperrealistic digital avatar, centered,"
           " serious look, rim lighting, studio lighting, looking at the camera")
    image_name = "img_out/dict_diff_2.jpg"
    generator(txt, image_name)
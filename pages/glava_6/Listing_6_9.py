# Листинг 6.9
from diffusers import StableDiffusionPipeline
from PIL import Image
import torch

# Путь к исходному изображению
image_path = "img_inp/women.jpg"  # Укажите путь к вашему файлу
# Загружаем исходное изображение
image = Image.open(image_path)

# Загружаем модель
model_id = "dreamlike-art/dreamlike-photoreal-2.0"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

# Текстовый запрос
prompt = ("The woman in the photo, thirty years old, gray eyes, "
          "wearing a blue dress, bright studio lighting, high resolution, "
          "8K detail, professional photography, soft focus on the face, "
          "shallow depth of field")
# Генерируем новое изображение на основе исходного и запроса
image = pipe(image=image, prompt=prompt).images[0]

# Сохраняем результат
image.save("img_out/txt_women.jpg")
# Листинг 6.7
import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

def generator(prompt, name_file):
    # Загрузка токена из файла .env
    load_dotenv()
    token = os.getenv("HF_TOKEN")
    client = InferenceClient(token=token,
                             model="stabilityai/stable-diffusion-xl-base-1.0")
    image = client.text_to_image(prompt)
    image.save(name_file)

if __name__ == '__main__':
    txt = ("A woman against the backdrop of beautiful mountains,"
           " a beautiful landscape, a photo, high resolution.")
    image_name = "img_out/vit_mountain.jpg"
    generator(txt, image_name)
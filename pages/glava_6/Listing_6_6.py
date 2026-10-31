# Листинг 6.6
import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

def generator(prompt, img_inp, img_out):
    # Загрузка токена из файла .env
    load_dotenv()
    token = os.getenv("HF_TOKEN")

    client = InferenceClient(provider="fal-ai",
                             api_key=token)

    with open(img_inp, "rb") as image_file:
        input_image = image_file.read()

    image = client.image_to_image(input_image,
                                  prompt=prompt,
                                  model="black-forest-labs/FLUX.2-klein-9B")
    image.save(img_out)

if __name__ == '__main__':
    txt = "Turn the women into a tiger.",
    image_inp = "img_inp/Vita.jpg",
    image_out = "img_out/vita_tiger.jpg"
    # txt = "An image of a women in Picasso style"
    # image_name = "img_out/vita_pic.jpg"
    generator(txt, image_inp, image_out)
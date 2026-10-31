# Листинг 6.2
from diffusers import StableDiffusionPipeline
import torch

def generator(prompt, name_file):
    model_id = "stable-diffusion-v1-5/stable-diffusion-v1-5"
    pipe = StableDiffusionPipeline.from_pretrained(model_id,
                                                   torch_dtype=torch.float16)
    pipe = pipe.to("cuda")
    image = pipe(prompt, height=512, width=512).images[0]
    image.save(name_file)

if __name__ == '__main__':
    txt = "A cat with striped fur and long whiskers, realistic photo."
    image_name = "img_out/cat.png"
    generator(txt, image_name)
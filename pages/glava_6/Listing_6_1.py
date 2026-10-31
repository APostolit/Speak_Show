# Листинг 6.1
from diffusers import StableDiffusionPipeline
import torch

def generator(prompt, negative_prompt, name_file):
    model_id ="stable-diffusion-v1-5/stable-diffusion-v1-5"
    pipe = StableDiffusionPipeline.from_pretrained(model_id,
                                                   torch_dtype=torch.float16)
    pipe = pipe.to("cuda")
    image = pipe(prompt=prompt, negative_prompt=negative_prompt).images[0]
    image.save(name_file)

if __name__ == '__main__':
    prmt = "An image of a squirrel in Picasso style"
    negative_prmt = "ugly, bad anatomy"
    image_name = "img_out/squirrel.jpg"
    generator(prmt, negative_prmt, image_name)
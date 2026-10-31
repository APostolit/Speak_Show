# Листинг 8.1
from lipsync import LipSync
import torch

def made_avatar(face, audio, my_model, outfile):
    # Получить устройство
    device = "cuda" if torch.cuda.is_available() else "cpu"
    lip = LipSync(
        model='wav2lip',
        checkpoint_path=my_model,
        nosmooth=True,
        device=device,
        cache_dir='cache',
        img_size=96,
        save_cache=True,
    )
    lip.sync(face=face, audio_file=audio, outfile=outfile)

if __name__ == '__main__':
    # Видео из фото
    get_face = 'images/Vita_1.jpg'
    get_aud = 'audio/ludk_a_lodk.wav'
    net_model = 'weights/wav2lip_gan.pth'
    out_file = 'video_out/vita_ludk.mp4'
    made_avatar(get_face, get_aud, net_model, out_file)
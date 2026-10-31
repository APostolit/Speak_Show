# Листинг 8.2
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
   # Выполнить синхронизацию
    lip.sync(face, audio, outfile)

if __name__ == '__main__':
    # Видео из видео
    get_face = 'video_in/Smokt.mp4'
    get_aud = 'audio/pacak.mp3'
    net_model = 'weights/wav2lip_gan.pth'
    out_file = 'video_out/smok_pacak.mp4'
    made_avatar(get_face, get_aud, net_model, out_file)

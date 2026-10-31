# Листинг 7.1
import cv2

def style_img(in_img, in_model, out_path):
    net = cv2.dnn.readNetFromTorch(in_model)  # Загрузка обученной модели
    image = cv2.imread(in_img)  # Открыть изображение
    h, w = image.shape[:2]  # Получить размеры

    # Прямой проход по сети
    blob = cv2.dnn.blobFromImage(image, 1.0, (w, h),
                                 (103.939, 116.779, 123.680),
                                 swapRB=False, crop=False)
    # Прямой проход по сети
    net.setInput(blob)
    output = net.forward()

    # Изменение формы выходного тензора и изменение порядка каналов
    output = output.reshape((3, output.shape[2], output.shape[3]))
    output[0] += 103.939
    output[1] += 116.779
    output[2] += 123.680
    output /= 255.0
    output = output.transpose(1, 2, 0)

    # Сохранить изображение
    cv2.imwrite(out_path, output * 255)

if __name__ == "__main__":
    inp_img = "img_inp/AV_500.jpg"
    model =  "pages/style_1/Model_Styl/mosaic.t7"
    output_img = "img_out/av_500.jpg"
    style_img(inp_img, model, output_img)
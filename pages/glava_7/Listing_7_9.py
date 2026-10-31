# Листинг 7.9
import numpy as np
import cv2

class Made_Color():
    def __init__(self, img_inp, img_out):
        image = cv2.imread(img_inp)  # загрузка изображения
        prototxt = "./model/colorization_deploy_v2.prototxt"
        caffe_model = "./model/colorization_release_v2.caffemodel"
        pts_npy = "./model/pts_in_hull.npy"

        # загрузка модели
        net = cv2.dnn.readNetFromCaffe(prototxt, caffe_model)
        pts = np.load(pts_npy)

        # добавьте центры кластеров в виде сверток 1x1 к модели
        class8 = net.getLayerId("class8_ab")
        conv8 = net.getLayerId("conv8_313_rh")
        pts = pts.transpose().reshape(2, 313, 1, 1)
        net.getLayer(class8).blobs = [pts.astype("float32")]
        net.getLayer(conv8).blobs = [np.full([1, 313], 2.606, dtype="float32")]

        # масштабируйте интенсивность пикселей в диапазон 0-1
        scaled = image.astype("float32") / 255.0
        # преобразование изображения из BGR в LAB
        lab = cv2.cvtColor(scaled, cv2.COLOR_BGR2LAB)

        # измените размер лабораторного изображения до 224x224
        resized = cv2.resize(lab, (224, 224))
        L = cv2.split(resized)[0]  # извлеките канал "L", а затем
        L -= 50  # выполнить среднее центрирование

        # пропустите L-канал через сеть,
        # которая будет предсказывать значения каналов "а" и 'b'
        net.setInput(cv2.dnn.blobFromImage(L))
        ab = net.forward()[0, :, :, :].transpose((1, 2, 0))

        # измените размер предсказанного "ab" до тех же размеров,
        # что и входное изображение
        ab = cv2.resize(ab, (image.shape[1], image.shape[0]))

        # захватите канал "L" из *исходного* входного изображения и объединить
        # исходный канал "L" с предсказанные каналы 'ab'
        L = cv2.split(lab)[0]
        colorized = np.concatenate((L[:, :, np.newaxis], ab), axis=2)

        # преобразуйте выходное изображение из лабораторного цветового
        # пространства в RGB
        # и обрезать любые значения, выходящие за пределы диапазона [0, 1]
        colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2BGR)
        colorized = np.clip(colorized, 0, 1)

        # текущее цветное изображение представлено в виде с плавающей точки
        # тип данных в диапазоне [0, 1] - преобразуем в беззнаковый
        # 8-битное целочисленное представление в диапазоне [0, 255]
        self.out_image = (255 * colorized).astype("uint8")
        cv2.imwrite(img_out, self.out_image)

if __name__ == "__main__":
    inp_image = 'img_inp/gray.jpg'
    out_image = 'img_out/color.jpg'
    Made_Color(inp_image, out_image)

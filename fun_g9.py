import streamlit as st

def run_9_1():
    st.markdown('#### 🐍 Создание видео из текстового запроса 🧠')
    tab1, tab2 = (
        st.tabs(["Текстовый запрос", "Итоговый видео файл"]))
    with tab1:
        with st.container(width=800):
            st.text("A large orange octopus is seen resting on the bottom of the ocean floor, "
                    "blending in with the sandy and rocky terrain. Its tentacles are spread "
                    "out around its body, and its eyes are closed. The octopus is unaware of "
                    "a king crab that is crawling towards it from behind a rock, its claws raised "
                    "and ready to attack. The crab is brown and spiny, with long legs and antennae. "
                    "The scene is captured from a wide angle, showing the vastness and depth of the ocean. "
                    "The water is clear and blue, with rays of sunlight filtering through. "
                    "The shot is sharp and crisp, with a high dynamic range. The octopus and the crab are in focus, "
                    "while the background is slightly blurred, creating a depth of field effect.")
    with tab2:
        with st.container(width=800):
            video_file = open("video_out/Crab.mp4", "rb")
            video_bytes = video_file.read()
            st.video(video_bytes)

def run_9_2():
    st.markdown('#### 🐍 Создание маски объекта на изображении 🧠')
    tab1, tab2 = (
        st.tabs(["Исходное изображение", "Объект переднего плана"]))
    with tab1:
        with st.container(width=400):
            st.image("img_inp/Vita.jpg")
    with tab2:
        with st.container(width=400):
            st.image("img_out/v_gr.jpg")

def run_9_3():
    st.markdown('#### 🐍 Создание видео из текстового запроса и изображения 🧠')
    tab1, tab2, tab3 = (
        st.tabs(["Текстовый запрос", "Исходное изображение", "Итоговый видео файл"]))
    with tab1:
        with st.container(width=800):
            st.text("Переместите девушку на изображении в парк, на танцпол; "
                    "она должна исполнить танец, продолжительность танца 10 секунд.")
            st.text("Move the girl in the image to the park, to the dance floor; "
                    "she should perform a dance, and the dance should last 10 seconds.")
    with tab2:
        with st.container(width=400):
            st.image("img_out/v_gr.jpg")
    with tab3:
        with st.container(width=800):
            video_file = open("video_out/Video_gen_0.mp4", "rb")
            video_bytes = video_file.read()
            st.video(video_bytes)

def run_9_4():
    st.markdown('#### 🐍 Создание видео из текстового запроса и изображения 🧠')
    tab1, tab2, tab3 = (
        st.tabs(["Текстовый запрос", "Исходное изображение", "Итоговый видео файл"]))
    with tab1:
        with st.container(width=800):
            st.text("Переместите девушку на снимке в танцевальный зал; она танцует легкий танец, "
                    "ее голова повернута к камере, высокое качество, танец длится 10 секунд.")
            st.text("Move the girl in the image to a dance hall; she is dancing a light dance, "
                    "her head is turned towards the camera, high quality, the dance lasts 10 seconds.")
    with tab2:
        with st.container(width=400):
            st.image("img_out/v_gr.jpg")
    with tab3:
        with st.container(width=400):
            video_file = open("video_out/Video_gen_2.mp4", "rb")
            video_bytes = video_file.read()
            st.video(video_bytes)

def run_9_5():
    st.markdown('#### 🐍 Создание видео из текстового запроса и изображения 🧠')
    tab1, tab2, tab3 = (
        st.tabs(["Текстовый запрос", "Исходное изображение", "Итоговый видео файл"]))
    with tab1:
        with st.container(width=800):
            st.text("Перенести девушку на изображении в танцевальный зал на конкурс танцев, "
                    "она танцует танец ча-ча ча, голова повернута к камере, танцует зажигательно и эмоционально, "
                    "на лице легкая улыбка, на заднем фоне зрители, фокус на объекте переднего плана, "
                    "высокое качество, продолжительность танца 10 секунд.")
            st.text("Move the girl in the image to a dance hall for a dance competition."
                    " She is dancing the cha‑cha‑cha; her head is turned towards the camera; "
                    "she is dancing energetically and emotionally; there is a slight smile on her face; "
                    "there are spectators in the background; the focus is on the foreground object; "
                    "high quality; the dance lasts 10 seconds.")
    with tab2:
        with st.container(width=400):
            st.image("img_out/v_gr.jpg")
    with tab3:
        with st.container(width=400):
            video_file = open("video_out/Video_gen_3.mp4", "rb")
            video_bytes = video_file.read()
            st.video(video_bytes)

def run_9_6():
    st.markdown('#### 🐍 Создание видео из текстового запроса и изображения 🧠')
    tab1, tab2, tab3 , tab4 = (
        st.tabs(["Текстовый запрос", "Исходное изображение",  "Обработанное изображение",
                 "Итоговый видео файл"]))
    with tab1:
        with st.container(width=800):
            st.text("Перенести девушку с изображения в студию новостей BBC, "
                    "девушка с изображения диктор телевидения в деловом костюме, "
                    "девушка с изображения сидит за столом лицом к камере, "
                    "в камере только верхняя часть тела, добавить руки, руки лежат на столе, "
                    "девушка с изображения активно говорит в камеру и жестикулирует руками,"
                    " на заднем фоне экраны с видео контентом, высокое качество, широкий экран,"
                    " продолжительность видео 15 секунд.")
    with tab2:
        with st.container(width=400):
            st.image("img_out/v_gr.jpg")
    with tab3:
        with st.container(width=400):
            st.image("img_out/Vita_dict.jpg")
    with tab4:
        with st.container(width=800):
            video_file = open("video_out/Leading_video.mp4", "rb")
            video_bytes = video_file.read()
            st.video(video_bytes)

def run_9_7():
    st.markdown('#### 🐍 Создание видео из текстового запроса и изображения 🧠')
    tab1, tab2, tab3 , tab4 = (
        st.tabs(["Текстовый запрос", "Исходное изображение",  "Обработанное изображение",
                 "Итоговый видео файл"]))
    with tab1:
        with st.container(width=800):
            st.text("Оживите исходное изображение, "
                    "Используйте это фото в качестве начального кадра и последнего кадра сгенерированной сцены, "
                    "Анимация без резких движений, мимика лица живая как у телеведущей (в стиле 'говорящей головы'), "
                    "анимация без звука, Легкие и плавные жесты рук, Свет мягкий студийный. "
                    "Фон стабилен, камера неподвижна, лицо и композицию сохранить, "
                    "Продолжительность сгенерированного видео 16 секунд.")
    with tab2:
        with st.container(width=400):
            st.image("img_out/v_gr.jpg")
    with tab3:
        with st.container(width=400):
            st.image("img_out/Vita_dict.jpg")
    with tab4:
        with st.container(width=400):
            video_file = open("video_out/Vita_Video_Final.mp4", "rb")
            video_bytes = video_file.read()
            st.video(video_bytes)

def run_9_8():
    st.markdown('#### 🐍 Генерирование изображения из текста 🧠')
    tab1, tab2 = (
        st.tabs(["Текстовый запрос", "Итоговое изображение"]))
    with tab1:
        with st.container(width=400):
            st.text("Чашка кофе с молоком, на поверхности чашки с кофе сердечко из крошек шоколада.")
    with tab2:
        with st.container(width=800):
            st.image("img_out/Coffe.png")

def run_9_9():
    st.markdown('#### 🐍 Генерирование видео из изображения и текста 🧠')
    tab1, tab2, tab3 = (
        st.tabs(["Текстовый запрос", "Исходное изображение", "Итоговое видео"]))
    with tab1:
        with st.container(width=400):
            st.text("В чашку кофе на исходном изображении падает одна капля воды, "
                    "расходятся волны только в пределах чашки, шоколадное сердечко "
                    "трансформируется в улыбающегося котика из крошек шоколада, "
                    "на первом кадре чашка кофе из исходного изображения, "
                    "продолжительность видео 8 секунд.")
    with tab2:
        with st.container(width=800):
            st.image("img_out/Coffe.png")
    with tab3:
        with st.container(width=800):
            video_file = open("video_out/Coffe-cat.mp4", "rb")
            video_bytes = video_file.read()
            st.video(video_bytes)

def run_9_10():
    st.markdown('#### 🐍 Подготовка видео файлов для создания говорящих аватаров 🧠')
    with st.expander("🔍 Показать код 📋", expanded=True):
        path = 'pages/glava_9/Listing_9_1.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    tab1, tab2, tab3 = (
        st.tabs(["Исходный видео файл", "Реверсный видео файл", "Склеенный видео файл"]))
    with tab1:
        with st.container(width=800):
            video_file = open("video_inp/u_obr.mp4", "rb")
            video_bytes = video_file.read()
            st.video(video_bytes)
    with tab2:
        with st.container(width=800):
            video_file = open("video_inp/u_2.mp4", "rb")
            video_bytes = video_file.read()
            st.video(video_bytes)
    with tab3:
        with st.container(width=800):
            video_file = open("video_inp/u_1_2.mp4", "rb")
            video_bytes = video_file.read()
            st.video(video_bytes)

def run_9_11():
    st.markdown('#### 🐍 Озвучивание видео файла (склейка методом реверса)  🧠')
    with st.container(width=800):
        video_file = open("video_inp/u_4.mp4", "rb")
        video_bytes = video_file.read()
        st.video(video_bytes)

def run_9_12():
    st.markdown('#### 🐍 Подготовка видео файлов для создания говорящих аватаров 🧠')
    with st.expander("🔍 Показать код 📋", expanded=True):
        path = 'pages/glava_9/Listing_9_2.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)

    tab1, tab2, tab3 = (
        st.tabs(["Исходный видео файл", "Отраженный видео файл", "Склеенный видео файл"]))
    with tab1:
        with st.container(width=800):
            video_file = open("video_inp/m.mp4", "rb")
            video_bytes = video_file.read()
            st.video(video_bytes)
    with tab2:
        with st.container(width=800):
            video_file = open("video_inp/m_2.mp4", "rb")
            video_bytes = video_file.read()
            st.video(video_bytes)
    with tab3:
        with st.container(width=800):
            video_file = open("video_inp/m_1_2.mp4", "rb")
            video_bytes = video_file.read()
            st.video(video_bytes)

def run_9_13():
    st.markdown('#### 🐍 Пример видео доклада на конференции 🧠')
    with st.container(width=800):
        video_file = open("video_out/Dokl_2_VGA.mp4", "rb")
        video_bytes = video_file.read()
        st.video(video_bytes)

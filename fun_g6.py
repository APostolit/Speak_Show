import streamlit as st

def run_6_1():
    st.markdown('#### 🐍 Генерация изображений из текста 🧠')
    tab1, tab2, tab3 = (
        st.tabs(["Положительный запрос", "Отрицательный запрос",
                 "Итоговое изображение"]))
    with tab1:
        txt = "An image of a squirrel in Picasso style"
        with st.container(height=50):
            st.text(txt)
    with tab2:
        txt = "ugly, bad anatomy"
        with st.container(height=50):
            st.text(txt)
    with tab3:
        st.image("img_out/squirrel.jpg")

def run_6_2():
    st.markdown('#### 🐍 Генерация изображений из текста 🧠')
    tab1, tab2 = (
        st.tabs(["Положительный запрос", "Итоговое изображение"]))
    with tab1:
        txt = "A cat with striped fur and long whiskers, realistic photo."
        with st.container(height=50):
            st.text(txt)
    with tab2:
        st.image("img_out/cat.png")

def run_6_3():
    st.markdown('#### 🐍 Генерация изображений из текста 🧠')
    tab1, tab2 = (
        st.tabs(["Положительный запрос", "Итоговое изображение"]))
    with tab1:
        txt = "An image of a women in Picasso style"
        with st.container(height=50):
            st.text(txt)
    with tab2:
        st.image("img_out/w_picasso.jpg")

def run_6_4():
    st.markdown('#### 🐍 Генерация изображений из текста 🧠')
    tab1, tab2 = (
        st.tabs(["Положительный запрос", "Итоговое изображение"]))
    with tab1:
        txt = ("A very beautiful girl, smiling, а TV announcer, with long dark hair, "
               " background - a real city street,"
               " hyperrealistic photo, centered,"
               " serious look, rim lighting, looking at the camera")
        with st.container(height=100):
            st.text(txt)
    with tab2:
        st.image("img_out/dict_1.jpg")

def run_6_5():
    st.markdown('#### 🐍 Генерация изображений из текста 🧠')
    tab1, tab2 = (
        st.tabs(["Положительный запрос", "Итоговое изображение"]))
    with tab1:
        txt = "An image of a women in Picasso style"
        with st.container(height=50):
            st.text(txt)
    with tab2:
        st.image("img_out/pic_w.jpg")

def run_6_6():
    st.markdown('#### 🐍 Генерация изображений из изображения 🧠')
    tab1, tab2, tab3 = (
        st.tabs(["Исходное изображение", "Женщина - тигр", "Картина в стиле Пикассо"]))
    with tab1:
        st.text("Исходное изображение")
        st.image("img_inp/Vita.jpg")
    with tab2:
        with st.container(width=460):
            st.text("Turn the women into a tiger")
            st.image("img_out/vita_tiger.jpg")
    with tab3:
        with st.container(width=460):
            st.text("An image of a women in Picasso style")
            st.image("img_out/vita_pic.jpg")

def run_6_7():
    st.markdown('#### 🐍 Генерация изображений из текста 🧠')
    tab1, tab2 = (
        st.tabs(["Текстовый запрос", "Итоговое изображение"]))
    with tab1:
        with st.container(width=600):
            txt = ("A woman against the backdrop of beautiful mountains,"
                   " a beautiful landscape, a photo, high resolution.")
            with st.container(height=100):
                st.text(txt)
    with tab2:
        with st.container(width=600):
            st.image("img_out/vit_mountain.jpg")

def run_6_8():
    st.markdown('#### 🐍 Генерация изображений из текста 🧠')
    tab1, tab2 = (
        st.tabs(["Текстовый запрос", "Итоговое изображение"]))
    with tab1:
        with st.container(width=800):
            txt = ("A very beautiful Kazakh girl, a TV presenter, with short dark hair, "
                   " background - TV news studio, hyperrealistic digital avatar, centered,"
                   " serious look, rim lighting, studio lighting, looking at the camera")
            with st.container(height=100):
                st.text(txt)
    with tab2:
        with st.container(width=600):
            st.image("img_out/dict_diff_2.jpg")

def run_6_9():
    st.markdown('#### 🐍 Генерация изображений из текста 🧠')
    tab1, tab2, tab3, tab4, tab5 = (
        st.tabs(["Исходное фото", "Девочка", "Подросток",
                 "Средний возраст", "Бабушка"]))
    with tab1:
       with st.container(width=600):
           st.text("Исходное фото")
           st.image("img_inp/women.jpg")
    with tab2:
        with st.container(width=600):
            st.text("girl")
            st.image("img_out/txt_women_0.jpg")
    with tab3:
        with st.container(width=600):
            st.text("young woman")
            st.image("img_out/txt_women_1.jpg")
    with tab4:
        with st.container(width=600):
            st.text("thirty years old")
            st.image("img_out/txt_women_2.jpg")
    with tab5:
        with st.container(width=600):
            st.text("grandmother")
            st.image("img_out/txt_women_3.jpg")

if __name__ == '__main__':
    run_6_1()
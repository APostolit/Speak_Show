import streamlit as st

def run_7_1():
    st.markdown('#### 🐍 Быстрая стилизация изображений 🧠')
    tab1, tab2 = (
        st.tabs(["Исходное изображение", "Итоговое изображение"]))
    with tab1:
        st.image("img_inp/AV_500.jpg")
    with tab2:
        st.image("img_out/av_500.jpg")

def run_7_2():
    st.markdown('#### 🐍 Стилизация изображений с PyTorch 🧠')
    tab1, tab2 = (
        st.tabs(["Исходное изображение", "Итоговое изображение"]))
    with tab1:
        st.image("img_inp/AV_500.jpg")
    with tab2:
        st.image("img_out/av_style.jpg")

def run_7_4():
    st.markdown('#### 🐍 Стилизация изображений с PyTorch 🧠')
    tab1, tab2, tab3, tab4, tab5 = (
        st.tabs(["Исходное изображение", "Альфа маска", "Тримап",
                 "Передний план", "Задний план"]))
    with tab1:
        st.image("img_inp/volos.png")
    with tab2:
        st.image("img_out/volos_mask.png")
    with tab3:
        st.image("img_out/volos_trimap.png")
    with tab4:
        st.image("img_out/volos_fg.png")
    with tab5:
        st.image("img_out/volos_bg.png")

def run_7_5():
    st.markdown('#### 🐍 Стилизация изображений с PyTorch 🧠')
    tab1, tab2, tab3, tab4, tab5 = (
        st.tabs(["Изображение", "Образец", "Стилизация полная",
                 "Стилизация объекта", "Стилизация фона"]))
    with tab1:
        st.image("img_inp/volos.png")
    with tab2:
        with st.container(width=560):
            st.image("img_inp/mosaic_duck.jpg")
    with tab3:
        with st.container(width=560):
            st.image("img_out/volos_all.jpg")
    with tab4:
        with st.container(width=560):
            st.image("img_out/volos_pp.jpg")
    with tab5:
        with st.container(width=560):
            st.image("img_out/volos_fon.jpg")

def run_7_8():
    st.markdown('#### 🐍 Стилизация (гравировка) изображений 🧠')
    tab1, tab2 = (
        st.tabs(["Исходное изображение", "Итоговое изображение"]))
    with tab1:
        st.image("img_inp/AV_500.jpg")
    with tab2:
        st.image("img_out/av_gravure.jpg")

def run_7_9():
    st.markdown('#### 🐍 Цветное изображение из черно-белого  🧠')
    tab1, tab2 = (
        st.tabs(["Черно-белое изображение", "Цветное изображение"]))
    with tab1:
        st.image("img_inp/gray.jpg")
    with tab2:
        st.image("img_out/color.jpg")

def run_7_10():
    st.markdown('#### 🐍 Отделение объекта переднего плана от фона  🧠')
    tab1, tab2 = (
        st.tabs(["Исходное изображение", "Обработанное изображение"]))
    with tab1:
        st.image("img_inp/Boris.jpg")
    with tab2:
        st.image("img_out/no_bg.png")

def run_7_11():
    st.markdown('#### 🐍 Отделение объекта переднего плана от фона  🧠')
    tab1, tab2 = (
        st.tabs(["Исходное изображение", "Обработанное изображение"]))
    with tab1:
        st.image("img_inp/volos.png")
    with tab2:
        st.image("img_out/volos_no_bg.png")


if __name__ == '__main__':
    run_7_1()
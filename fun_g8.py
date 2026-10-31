import streamlit as st

def run_8_1():
    st.markdown('#### 🐍 Создание аватара из изображения 🧠')
    tab1, tab2, tab3 = (
        st.tabs(["Изображение аватара", "Аудио дорожка",
                 "Итоговый видео файл"]))
    with tab1:
        with st.container(width=400):
            st.image("img_inp/Vita.jpg")
    with tab2:
        audio_file = "audio_inp/ludk_a_lodk.wav"
        st.audio(audio_file, format="audio/mpeg")
    with tab3:
        with st.container(width=400):
            video_file = open("video_out/vita_ludk.mp4", "rb")
            video_bytes = video_file.read()
            st.video(video_bytes)

def run_8_2():
    st.markdown('#### 🐍 Создание аватара из изображения 🧠')
    tab1, tab2, tab3 = (
        st.tabs(["Видео с аватаром", "Аудио дорожка",
                 "Итоговый видео файл"]))
    with tab1:
        with st.container(width=600):
            video_file = open("video_inp/Smokt.mp4", "rb")
            video_bytes = video_file.read()
            st.video(video_bytes)
    with tab2:
        audio_file = "audio_inp/pacak.mp3"
        st.audio(audio_file, format="audio/mpeg")
    with tab3:
        with st.container(width=600):
            video_file = open("video_out/smok_pacak.mp4", "rb")
            video_bytes = video_file.read()
            st.video(video_bytes)

def run_8_3():
    st.markdown('#### 🐍 Создание аватара из изображения 🧠')
    tab1, tab2, tab3, tab4 = (
        st.tabs(["Фото аватара", "Управляющее видео",
                 "Итоговое видео", "Видео-сборка"]))
    with tab1:
        with st.container(width=600):
            st.image("img_inp/Puskin.png")
    with tab2:
        with st.container(width=600):
            video_file = open("video_inp/Moroz.mp4", "rb")
            video_bytes = video_file.read()
            st.video(video_bytes)
    with tab3:
        with st.container(width=600):
            video_file = open("video_out/Puskin--Moroz.mp4", "rb")
            video_bytes = video_file.read()
            st.video(video_bytes)
    with tab4:
        with st.container(width=800):
            video_file = open("video_out/Puskin--Moroz_concat.mp4", "rb")
            video_bytes = video_file.read()
            st.video(video_bytes)

if __name__ == '__main__':
    run_8_1()
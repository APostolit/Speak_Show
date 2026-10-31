import streamlit as st

def run_5_1():
    st.markdown('#### 🐍 Извлечение текста из аудио файла 🧠')
    tab1, tab2 = (
        st.tabs(["Исходный аудио файл", "Извлеченный текст"]))
    with tab1:
        audio_file = "audio_inp/levitan.wav"
        st.audio(audio_file, format="audio/mpeg")
    with tab2:
        txt_file = "text_out/levitan.txt"
        with open(txt_file, "r", encoding="utf-8") as file:
            text_content = file.read()
        with st.container(height=100):
            st.text(text_content)

def run_5_2():
    st.markdown('#### 🐍 Извлечение текста из видео файла 🧠')
    tab1, tab2, tab3= (
        st.tabs(["Исходный видео файл",
                 "Извлеченный аудио файл",
                 "Извлеченный текст"]))
    with tab1:
        video_file = open("video_inp/leonov.mp4", "rb")
        video_bytes = video_file.read()
        st.video(video_bytes)
    with tab2:
        audio_file = "audio_out/leonov.wav"
        st.audio(audio_file, format="audio/mpeg")
    with tab3:
        txt_file = "text_out/leonov.txt"
        with open(txt_file, "r", encoding="utf-8") as file:
            text_content = file.read()
        with st.container(height=100):
            st.text(text_content)

if __name__ == '__main__':
    run_5_1()
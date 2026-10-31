import streamlit as st

def run_3_1():
    st.markdown('#### 🐍 Параметры библиотеки gTTS 🧠')
    st.markdown("##### Список доступных языков")
    file_path = "text_out/languages_gtts.txt"
    with open(file_path, "r", encoding="utf-8") as file:
        text_content = file.read()
        with st.container(height=300):
            st.text(text_content)

def run_3_2():
    st.markdown('#### 🐍 Озвучивание текста на русском языке с gTTS 🧠')
    tab1, tab2 = st.tabs(["Исходный текст", "Аудио дорожка"])
    with tab1:
        txt_file = "text_inp/forum_2.txt"
        with open(txt_file, "r", encoding="utf-8") as file:
            text_content = file.read()
        with st.container(height=300):
            st.text(text_content)
    with tab2:
        audio_file = "audio_out/forum_2.mp3"
        st.audio(audio_file, format="audio/mpeg")

def run_3_3():
    st.markdown('#### 🐍 Озвучивание текста на английском языке с gTTS 🧠')
    tab1, tab2 = st.tabs(["Исходный текст", "Аудио дорожка"])
    with tab1:
        txt_file = "text_inp/forum_en.txt"
        with open(txt_file, "r", encoding="utf-8") as file:
            text_content = file.read()
        with st.container(height=300):
            st.text(text_content)
    with tab2:
        audio_file = "audio_out/forum_2_en.mp3"
        st.audio(audio_file, format="audio/mpeg")


if __name__ == '__main__':
    run_3_1()
import streamlit as st

def run_1_1():
    st.markdown('#### 🐍 Параметры нейронной сети')
    tab1, tab2 = st.tabs(["Список обученных моделей", "Список спикеров модели xtts_v2"])
    with tab1:
        file_path = "text_out/models_CoquiTTS.txt"
        with open(file_path, "r", encoding="utf-8") as file:
            text_content = file.read()
        with st.container(height=300):
            st.text(text_content)
    with tab2:
        file_path = "text_out/speakers_xtts_v2.txt"
        with open(file_path, "r", encoding="utf-8") as file:
            text_content = file.read()
        with st.container(height=300):
            st.text(text_content)

def run_1_2():
    st.markdown('#### 🐍 Трансформация текста в речь с Coqui TTS 🧠')
    tab1, tab2 = st.tabs(["Исходный текст", "Аудио файл"])
    with tab1:
        with st.container(height=100):
            text_content = ("Всем добрый день! Сегодня на наших компьютерных курсах "
                            "мы приступаем к изучению нейронных сетей, которые позволяют"
                            " текстовые данные трансформировать в аудио контент.")
            st.text(text_content)
    with tab2:
        audio_file = "audio_out/Tanja_Adelina.wav"
        st.audio(audio_file, format="audio/mpeg")

def run_1_3():
    st.markdown('#### 🐍 Трансформация текста в речь с Coqui TTS 🧠')
    tab1, tab2 = st.tabs(["Исходный текст", "Аудио файл"])
    with tab1:
        file_path = "text_inp/forum.txt"
        with open(file_path, "r", encoding="utf-8") as file:
            text_content = file.read()
        with st.container(height=300):
            st.text(text_content)
    with tab2:
        audio_file = "audio_out/forum.mp3"
        st.audio(audio_file, format="audio/mpeg")

def run_1_4():
    st.markdown('#### 🐍 Подмена голоса в аудио файле с Coqui TTS 🧠')
    tab1, tab2 = st.tabs(["Исходный аудио файл", " Итоговый аудио файл"])
    with tab1:
        audio_file = "audio_inp/Tanja_Adelina.wav"
        st.audio(audio_file, format="audio/mpeg")
    with tab2:
        audio_file = "audio_out/levitan.mp3"
        st.audio(audio_file, format="audio/mpeg")

def run_1_5():
    st.markdown('#### 🐍 Подмена голоса в аудио файле с Coqui TTS 🧠')
    tab1, tab2 = st.tabs(["Исходный аудио файл", " Итоговый аудио файл"])
    with tab1:
        audio_file = "audio_inp/Tanja_Adelina.wav"
        st.audio(audio_file, format="audio/mpeg")
    with tab2:
        audio_file = "audio_out/levitan.mp3"
        st.audio(audio_file, format="audio/mpeg")

if __name__ == '__main__':
    run_1_1()
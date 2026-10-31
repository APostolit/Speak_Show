import streamlit as st

def run_2_1():
    st.markdown('#### 🐍 Параметры нейронных сетей SileroTTS 🧠')
    st.markdown("##### Список обученных моделей")
    file_path = "text_out/models_SileroTTS.txt"
    with open(file_path, "r", encoding="utf-8") as file:
        text_content = file.read()
        with st.container(height=300):
            st.text(text_content)

def run_2_2():
    st.markdown('#### 🐍 Параметры нейронных сетей SileroTTS 🧠')
    tab1, tab2 = st.tabs(["Русский язык", "Английский язык"])
    with tab1:
        txt_file = "text_out/SileroTTS_ru.txt"
        with open(txt_file, "r", encoding="utf-8") as file:
            text_content = file.read()
        with st.container(height=300):
            st.text(text_content)
    with tab2:
        txt_file = "text_out/SileroTTS_en.txt"
        with open(txt_file, "r", encoding="utf-8") as file:
            text_content = file.read()
        with st.container(height=300):
            st.text(text_content)

def run_2_3():
    st.markdown('#### 🐍 Обработка текста моделью v5_ru 🧠')
    tab1, tab2, tab3 = st.tabs(["Текстовый файл",
                                "Мужской голос eugene",
                                "Женский голос baya"])
    with tab1:
        txt_file = "text_inp/forum.txt"
        with open(txt_file, "r", encoding="utf-8") as file:
            text_content = file.read()
        with st.container(height=300):
            st.text(text_content)
    with tab2:
        audio_file = "audio_out/eugene_ru.wav"
        st.audio(audio_file, format="audio/mpeg")
    with tab3:
        audio_file = "audio_out/baya_ru.wav"
        st.audio(audio_file, format="audio/mpeg")

def run_2_4():
    st.markdown('#### 🐍 Обработка текста моделью v3_en_indic 🧠')
    tab1, tab2, tab3 = st.tabs(["Текстовый файл",
                                "Мужской голос kannada_male",
                                "Женский голос kannada_female"])
    with tab1:
        txt_file = "text_inp/forum_en.txt"
        with open(txt_file, "r", encoding="utf-8") as file:
            text_content = file.read()
        with st.container(height=300):
            st.text(text_content)
    with tab2:
        audio_file = "audio_out/forum_en_male.wav"
        st.audio(audio_file, format="audio/mpeg")
    with tab3:
        audio_file = "audio_out/forum_en_female.wav"
        st.audio(audio_file, format="audio/mpeg")

def run_2_5():
    st.markdown('#### 🐍 Обработка текста c SSML-разметкой 🧠')
    tab1, tab2 = st.tabs(["Текст с разметкой",
                          "Женский голос xenia"])
    with tab1:
        txt_file = "text_inp/text_ssml.txt"
        with open(txt_file, "r", encoding="utf-8") as file:
            text_content = file.read()
        with st.container(height=300):
            st.text(text_content)
    with tab2:
        audio_file = "audio_out/xenia_ssml.mp3"
        st.audio(audio_file, format="audio/mpeg")

def run_2_6():
    st.markdown('#### 🐍 Обработка текста c SSML-разметкой 🧠')
    tab1, tab2, tab3 = st.tabs(["Текстовый файл",
                                "Мужской голос eugene",
                                "Женский голос xenia"])
    with tab1:
        txt_file = "text_inp/forum_p.txt"
        with open(txt_file, "r", encoding="utf-8") as file:
            text_content = file.read()
        with st.container(height=300):
            st.text(text_content)
    with tab2:
        audio_file = "audio_out/forum_p_eugene.mp3"
        st.audio(audio_file, format="audio/mpeg")
    with tab3:
        audio_file = "audio_out/forum_p_xenia.mp3"
        st.audio(audio_file, format="audio/mpeg")

def run_2_7():
    st.markdown('#### 🐍 Обработка длинного текста 🧠')
    tab1, tab2, tab3 = st.tabs(["Текстовый файл",
                                "Мужской голос eugene",
                                "Женский голос xenia"])
    with tab1:
        txt_file = "text_inp/forum_1.txt"
        with open(txt_file, "r", encoding="utf-8") as file:
            text_content = file.read()
        with st.container(height=300):
            st.text(text_content)
    with tab2:
        audio_file = "audio_out/forum_l_eugene.mp3"
        st.audio(audio_file, format="audio/mpeg")
    with tab3:
        audio_file = "audio_out/forum_l_xenia.mp3"
        st.audio(audio_file, format="audio/mpeg")

if __name__ == '__main__':
    run_2_1()
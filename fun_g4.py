import streamlit as st

def run_4_1():
    st.markdown('#### 🐍 Озвучивание текста с OmniVoice 🧠')
    tab1, tab2, tab3, tab4, tab5, tab6 = (
        st.tabs(["Исходный текст 1", "Аудио дорожка 1", "Аудио дорожка 2",
                 "Исходный текст 2", "Аудио дорожка 3", "Аудио дорожка 4"]))
    with tab1:
        text = ("Добрый день. Это образец аудио файла с параметрами по умолчанию."
                "Образец этого голоса можно использовать для озвучивания"
                " любых текстов на русском языке.")
        st.text(text)
    with tab2:
        audio_file = "audio_out/spiker_1.mp3"
        st.audio(audio_file, format="audio/mpeg")
    with tab3:
        audio_file = "audio_out/spiker_2.mp3"
        st.audio(audio_file, format="audio/mpeg")
    with tab4:
        text = ("Добрый день. Это образец аудио файла с параметрами по умолчанию."
                "Образец этого женского голоса можно использовать для озвучивания"
                " любых текстов на русском языке.")
        st.text(text)
    with tab5:
        audio_file = "audio_out/spiker_3.mp3"
        st.audio(audio_file, format="audio/mpeg")
    with tab6:
        audio_file = "audio_out/spiker_4.mp3"
        st.audio(audio_file, format="audio/mpeg")

def run_4_2():
    st.markdown('#### 🐍 Озвучивание текста с OmniVoice 🧠')
    tab1, tab2 = (
        st.tabs(["Исходный текст", "Аудио дорожка"]))
    with tab1:
        text = ("Добрый день. Это образец аудио файла с заданными параметрами: "
                "мужчина, средний возраст, низкий тембр, русский акцент."
                "Образец этого мужского голоса можно использовать для озвучивания"
                " любых текстов на русском языке.")
        st.text(text)
    with tab2:
        audio_file = "audio_out/spiker_m_ru.mp3"
        st.audio(audio_file, format="audio/mpeg")

def run_4_3():
    st.markdown('#### 🐍 Озвучивание текста с OmniVoice 🧠')
    tab1, tab2 = (
        st.tabs(["Исходный текст", "Аудио дорожка"]))
    with tab1:
        text = ("Добрый день. Это образец аудио файла с заданными параметрами: "
                "женщина, зрелый возраст, средний тембр, русский акцент."
                "Образец этого женского голоса можно использовать для озвучивания"
                " любых текстов на русском языке.")
        st.text(text)
    with tab2:
        audio_file = "audio_out/spiker_f_ru.mp3"
        st.audio(audio_file, format="audio/mpeg")

def run_4_4():
    st.markdown('#### 🐍 Озвучивание текста с OmniVoice 🧠')
    tab1, tab2 = (
        st.tabs(["Исходный текст", "Аудио дорожка"]))
    with tab1:
        text = ("Ходит осень в нашем парке. Дарит осень всем подарки. "
                "Фартук розовый — осинке. Бусы красные — рябинке. "
                "Образец этого детского голоса можно использовать для озвучивания"
                " любых детских стихов на русском языке.")
        st.text(text)
    with tab2:
        audio_file = "audio_out/spiker_c_ru.mp3"
        st.audio(audio_file, format="audio/mpeg")

def run_4_5():
    st.markdown('#### 🐍 Озвучивание текста с OmniVoice 🧠')
    tab1, tab2 = (
        st.tabs(["Исходный текст", "Аудио дорожка"]))
    with tab1:
        text = ("Good afternoon. This is a sample audio file with the specified parameters: "
                "female, middle age, medium timbre, English accent. "
                "This sample of a female voice can be used to voice any texts in English."
                )
        st.text(text)
    with tab2:
        audio_file = "audio_out/spiker_f_en.mp3"
        st.audio(audio_file, format="audio/mpeg")

def run_4_6():
    st.markdown('#### 🐍 Озвучивание текста с OmniVoice 🧠')
    tab1, tab2 = (
        st.tabs(["Исходный текст", "Аудио дорожка"]))
    with tab1:
        txt_file = "text_inp/forum.txt"
        with open(txt_file, "r", encoding="utf-8") as file:
            text_content = file.read()
        with st.container(height=300):
            st.text(text_content)
    with tab2:
        audio_file = "audio_out/forum_spiker_2.mp3"
        st.audio(audio_file, format="audio/mpeg")

def run_4_7():
    st.markdown('#### 🐍 Озвучивание текста с OmniVoice 🧠')
    tab1, tab2 = (
        st.tabs(["Исходный текст", "Аудио дорожка"]))
    with tab1:
        txt_file = "text_inp/forum.txt"
        with open(txt_file, "r", encoding="utf-8") as file:
            text_content = file.read()
        with st.container(height=300):
            st.text(text_content)
    with tab2:
        audio_file = "audio_out/forum_spiker_4.mp3"
        st.audio(audio_file, format="audio/mpeg")

def run_4_8():
    st.markdown('#### 🐍 Клонирование голоса с OmniVoice 🧠')
    tab1, tab2, tab3 = (
        st.tabs(["Исходный текст", "Образец голоса", "Итоговый аудио файл"]))
    with tab1:
        txt_file = "text_inp/student.txt"
        with open(txt_file, "r", encoding="utf-8") as file:
            text_content = file.read()
        with st.container(height=200):
            st.text(text_content)
    with tab2:
        audio_file = "audio_inp/student.mp3"
        st.audio(audio_file, format="audio/mpeg")
    with tab3:
        audio_file = "audio_out/student.mp3"
        st.audio(audio_file, format="audio/mpeg")

def run_4_9():
    st.markdown('#### 🐍 Озвучивание текста с OmniVoice 🧠')
    tab1, tab2 = (
        st.tabs(["Исходный текст", "Аудио дорожка"]))
    with tab1:
        txt_file = "text_inp/omograf.txt"
        with open(txt_file, "r", encoding="utf-8") as file:
            text_content = file.read()
        with st.container(height=300):
            st.text(text_content)
    with tab2:
        audio_file = "audio_out/omograf.mp3"
        st.audio(audio_file, format="audio/mpeg")

def run_4_10():
    st.markdown('#### 🐍 Озвучивание текста с OmniVoice 🧠')
    tab1, tab2, tab3, tab4 = (
        st.tabs(["Исходный текст", "Аудио по умолчанию",
                 "Аудио замедленное", "Аудио ускоренное"]))
    with tab1:
        txt_file = "text_inp/forum.txt"
        with open(txt_file, "r", encoding="utf-8") as file:
            text_content = file.read()
        with st.container(height=300):
            st.text(text_content)
    with tab2:
        audio_file = "audio_out/forum_norm.mp3"
        st.audio(audio_file, format="audio/mpeg")
    with tab3:
        audio_file = "audio_out/forum_slow.mp3"
        st.audio(audio_file, format="audio/mpeg")
    with tab4:
        audio_file = "audio_out/forum_fast.mp3"
        st.audio(audio_file, format="audio/mpeg")

if __name__ == '__main__':
    run_4_1()
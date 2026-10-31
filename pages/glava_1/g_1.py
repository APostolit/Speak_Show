import streamlit as st
import fun_g1

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 1", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

st.header("👩🏻‍💻Глава 1. Нейронные сети и библиотека CoquiTTS для генерации речи из текста🐍")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

with cont_1:
    # Раскрывающийся список
    options = st.selectbox(
        "🕵🏻‍♂️ Листинги главы 1",
        ("Листинг 1.1", "Листинг 1.2", "Листинг 1.3", "Листинг 1.4", "Листинг 1.5",
        ),
        index=None,
        placeholder="Выберите листинг..."
    )

# Контейнер
cont = st.container(width=800)

with cont:
    if options is None:
        st.write('Листинг не выбран')
        st.image("Python_Book.jpg", width=350)

    elif options == "Листинг 1.1":
        with st.expander("🔍 Показать код 📋", expanded=True):
            path = 'pages/glava_1/Listing_1_1.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат 💻"):
            fun_g1.run_1_1()

    elif options == "Листинг 1.2":
        with st.expander("🔍 Показать код 📋", expanded=True):
            path = 'pages/glava_1/Listing_1_2.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат 💻"):
            fun_g1.run_1_2()

    elif options == "Листинг 1.3":
        with st.expander("🔍 Показать код 📋", expanded=True):
            path = 'pages/glava_1/Listing_1_3.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат 💻"):
            fun_g1.run_1_3()

    elif options == "Листинг 1.4":
        with st.expander("🔍 Показать код 📋", expanded=True):
            path = 'pages/glava_1/Listing_1_4.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат 💻"):
            fun_g1.run_1_4()

    elif options == "Листинг 1.5":
        with st.expander("🔍 Показать код 📋", expanded=True):
            path = 'pages/glava_1/Listing_1_5.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат 💻"):
            fun_g1.run_1_4()
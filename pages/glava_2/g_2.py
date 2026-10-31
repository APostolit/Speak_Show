import streamlit as st
import fun_g2

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Тема 2", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="auto",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Глава 2. Библиотека SileroTTS и нейронные сети для генерации речи из текста🐍")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=800)

# Контейнер
with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги главы 2",
        ("Листинг 2.1", "Листинг 2.2", "Листинг 2.3", "Листинг 2.4", "Листинг 2.5",
         "Листинг 2.6", "Листинг 2.7",
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

    elif options == "Листинг 2.1":
        with st.expander("🔍 Показать код 📋", expanded=True):
            path = 'pages/glava_2/Listing_2_1.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат 💻"):
            fun_g2.run_2_1()

    elif options == "Листинг 2.2":
        with st.expander("🔍 Показать код 📋", expanded=True):
            path = 'pages/glava_2/Listing_2_2.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат 💻"):
            fun_g2.run_2_2()

    elif options == "Листинг 2.3":
        with st.expander("🔍 Показать код 📋", expanded=True):
            path = 'pages/glava_2/Listing_2_3.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат 💻"):
            fun_g2.run_2_3()

    elif options == "Листинг 2.4":
        with st.expander("🔍 Показать код 📋", expanded=True):
            path = 'pages/glava_2/Listing_2_4.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат 💻"):
            fun_g2.run_2_4()

    elif options == "Листинг 2.5":
        with st.expander("🔍 Показать код 📋", expanded=True):
            path = 'pages/glava_2/Listing_2_5.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат 💻"):
            fun_g2.run_2_5()

    elif options == "Листинг 2.6":
        with st.expander("🔍 Показать код 📋", expanded=True):
            path = 'pages/glava_2/Listing_2_6.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат 💻"):
            fun_g2.run_2_6()

    elif options == "Листинг 2.7":
        with st.expander("🔍 Показать код 📋", expanded=True):
            path = 'pages/glava_2/Listing_2_7.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат 💻"):
            fun_g2.run_2_7()

    elif options == "Листинг 2.8":
        with st.expander("🔍 Показать код 📋", expanded=True):
            path = 'pages/glava_2/Listing_2_8.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)

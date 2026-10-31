import streamlit as st
import fun_g7

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 7", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="auto",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Глава 7. Обработка изображений с использованием нейронных сетей🐍")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=800)

# Контейнер
with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги главы 7",
        ("Листинг 7.1", "Листинг 7.2", "Листинг 7.3", "Листинг 7.4","Листинг 7.5",
         "Листинг 7.6", "Листинг 7.7", "Листинг 7.8", "Листинг 7.9", "Листинг 7.10",
         "Листинг 7.11"),
        index=None,
        placeholder="Выберите листинг..."
    )

# Контейнер
cont = st.container(width=800)
with cont:
    if options is None:
        st.write('Листинг не выбран')
        st.image("Python_Book.jpg", width=350)

    elif options == "Листинг 7.1":
        with st.expander("🔍 Показать код 📋", expanded=True):
            path = 'pages/glava_7/Listing_7_1.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат 💻"):
            fun_g7.run_7_1()

    elif options == "Листинг 7.2":
        with st.expander("🔍 Показать код 📋", expanded=True):
            path = 'pages/glava_7/Listing_7_2.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат 💻"):
            fun_g7.run_7_2()

    elif options == "Листинг 7.3":
        with st.expander("🔍 Показать код 📋", expanded=True):
            path = 'pages/glava_7/Listing_7_3.py'
            file = open(path, 'r')
            code = file.read()
            with st.container(height=500):
               st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 7.4":
        with st.expander("🔍 Показать код 📋", expanded=True):
            path = 'pages/glava_7/Listing_7_4.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат 💻"):
            fun_g7.run_7_4()

    elif options == "Листинг 7.5":
        with st.expander("🔍 Показать код 📋", expanded=True):
            path = 'pages/glava_7/Listing_7_5.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат 💻"):
            fun_g7.run_7_5()

    elif options == "Листинг 7.6":
        with st.expander("🔍 Показать код 📋", expanded=True):
            path = 'pages/glava_7/Listing_7_6.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 7.7":
        with st.expander("🔍 Показать код 📋", expanded=True):
            path = 'pages/glava_7/Listing_7_7.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)

    elif options == "Листинг 7.8":
        with st.expander("🔍 Показать код 📋", expanded=True):
            path = 'pages/glava_7/Listing_7_8.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат 💻"):
            fun_g7.run_7_8()

    elif options == "Листинг 7.9":
        with st.expander("🔍 Показать код 📋", expanded=True):
            path = 'pages/glava_7/Listing_7_9.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат 💻"):
            fun_g7.run_7_9()

    elif options == "Листинг 7.10":
        with st.expander("🔍 Показать код 📋", expanded=True):
            path = 'pages/glava_7/Listing_7_10.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат 💻"):
            fun_g7.run_7_10()

    elif options == "Листинг 7.11":
        with st.expander("🔍 Показать код 📋", expanded=True):
            path = 'pages/glava_7/Listing_7_11.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат 💻"):
            fun_g7.run_7_11()
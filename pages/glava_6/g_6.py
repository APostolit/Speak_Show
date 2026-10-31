import streamlit as st
import fun_g6

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 6", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="auto",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Глава 6. Нейронные сети от Hugging Face🐍")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=800)

# Контейнер
with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги главы 5",
        ("Листинг 6.1", "Листинг 6.2", "Листинг 6.3", "Листинг 6.4","Листинг 6.5",
         "Листинг 6.6", "Листинг 6.7", "Листинг 6.8", "Листинг 6.9"),
        index=None,
        placeholder="Выберите листинг..."
    )

# Контейнер
cont = st.container(width=800)
with cont:
    if options is None:
        st.write('Листинг не выбран')
        st.image("Python_Book.jpg", width=350)

    elif options == "Листинг 6.1":
        with st.expander("🔍 Показать код 📋", expanded=True):
            path = 'pages/glava_6/Listing_6_1.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат 💻"):
            fun_g6.run_6_1()

    elif options == "Листинг 6.2":
        with st.expander("🔍 Показать код 📋", expanded=True):
            path = 'pages/glava_6/Listing_6_2.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат 💻"):
            fun_g6.run_6_2()

    elif options == "Листинг 6.3":
        with st.expander("🔍 Показать код 📋", expanded=True):
            path = 'pages/glava_6/Listing_6_3.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат 💻"):
            fun_g6.run_6_3()

    elif options == "Листинг 6.4":
        with st.expander("🔍 Показать код 📋", expanded=True):
            path = 'pages/glava_6/Listing_6_4.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат 💻"):
            fun_g6.run_6_4()

    elif options == "Листинг 6.5":
        with st.expander("🔍 Показать код 📋", expanded=True):
            path = 'pages/glava_6/Listing_6_5.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат 💻"):
            fun_g6.run_6_5()

    elif options == "Листинг 6.6":
        with st.expander("🔍 Показать код 📋", expanded=True):
            path = 'pages/glava_6/Listing_6_6.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат 💻"):
            fun_g6.run_6_6()

    elif options == "Листинг 6.7":
        with st.expander("🔍 Показать код 📋", expanded=True):
            path = 'pages/glava_6/Listing_6_7.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат 💻"):
            fun_g6.run_6_7()

    elif options == "Листинг 6.8":
        with st.expander("🔍 Показать код 📋", expanded=True):
            path = 'pages/glava_6/Listing_6_8.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат 💻"):
            fun_g6.run_6_8()

    elif options == "Листинг 6.9":
        with st.expander("🔍 Показать код 📋", expanded=True):
            path = 'pages/glava_6/Listing_6_9.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат 💻"):
            fun_g6.run_6_9()
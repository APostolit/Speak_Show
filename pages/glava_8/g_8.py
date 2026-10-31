import streamlit as st
import fun_g8

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 8", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="auto",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Глава 8. Нейронные сети для создания аватаров🐍")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=800)

# Контейнер
with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги главы 8",
        ("Листинг 8.1", "Листинг 8.2", "Листинг 8.3"),
        index=None,
        placeholder="Выберите листинг..."
    )

# Контейнер
cont = st.container(width=800)
with cont:
    if options is None:
        st.write('Листинг не выбран')
        st.image("Python_Book.jpg", width=350)

    elif options == "Листинг 8.1":
        with st.expander("🔍 Показать код 📋", expanded=True):
            path = 'pages/glava_8/Listing_8_1.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат 💻"):
            fun_g8.run_8_1()

    elif options == "Листинг 8.2":
        with st.expander("🔍 Показать код 📋", expanded=True):
            path = 'pages/glava_8/Listing_8_2.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат 💻"):
            fun_g8.run_8_2()

    elif options == "Листинг 8.3":
        with st.expander("🔍 Показать код 📋", expanded=True):
            path = 'pages/glava_8/Listing_8_3.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат 💻"):
            fun_g8.run_8_3()
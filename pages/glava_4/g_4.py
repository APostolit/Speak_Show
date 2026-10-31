import streamlit as st
import fun_g4

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 4", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="auto",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Глава 4. Модель для синтеза речи OmniVoice🐍")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=800)

# Контейнер
with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги главы 4",
        ("Листинг 4.1", "Листинг 4.2", "Листинг 4.3", "Листинг 4.4", "Листинг 4.5",
         "Листинг 4.6", "Листинг 4.7", "Листинг 4.8", "Листинг 4.9", "Листинг 4.10",
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

    elif options == "Листинг 4.1":
        with st.expander("🔍 Показать код 📋", expanded=True):
            path = 'pages/glava_4/Listing_4_1.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат 💻"):
            fun_g4.run_4_1()

    elif options == "Листинг 4.2":
        with st.expander("🔍 Показать код 📋", expanded=True):
            path = 'pages/glava_4/Listing_4_2.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат 💻"):
            fun_g4.run_4_2()

    elif options == "Листинг 4.3":
        with st.expander("🔍 Показать код 📋", expanded=True):
            path = 'pages/glava_4/Listing_4_3.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат 💻"):
            fun_g4.run_4_3()

    elif options == "Листинг 4.4":
        with st.expander("🔍 Показать код 📋", expanded=True):
            path = 'pages/glava_4/Listing_4_4.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат 💻"):
            fun_g4.run_4_4()

    elif options == "Листинг 4.5":
        with st.expander("🔍 Показать код 📋", expanded=True):
            path = 'pages/glava_4/Listing_4_5.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат 💻"):
            fun_g4.run_4_5()

    elif options == "Листинг 4.6":
        with st.expander("🔍 Показать код 📋", expanded=True):
            path = 'pages/glava_4/Listing_4_6.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат 💻"):
            fun_g4.run_4_6()

    elif options == "Листинг 4.7":
        with st.expander("🔍 Показать код 📋", expanded=True):
            path = 'pages/glava_4/Listing_4_7.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат 💻"):
            fun_g4.run_4_7()

    elif options == "Листинг 4.8":
        with st.expander("🔍 Показать код 📋", expanded=True):
            path = 'pages/glava_4/Listing_4_8.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат 💻"):
            fun_g4.run_4_8()

    elif options == "Листинг 4.9":
        with st.expander("🔍 Показать код 📋", expanded=True):
            path = 'pages/glava_4/Listing_4_9.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат 💻"):
            fun_g4.run_4_9()

    elif options == "Листинг 4.10":
        with st.expander("🔍 Показать код 📋", expanded=True):
            path = 'pages/glava_4/Listing_4_10.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат 💻"):
            fun_g4.run_4_10()
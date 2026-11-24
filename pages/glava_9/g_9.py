import streamlit as st
import fun_g9

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 9", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="auto",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Глава 9. Нейронные сети для создания видео файлов🐍")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=800)

# Контейнер
with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Примеры главы 9",
        ("Пример 9.1", "Пример 9.2", "Пример 9.3", "Пример 9.4", "Пример 9.5", "Пример 9.6",
         "Пример 9.7", "Пример 9.8", "Пример 9.9"),
        index=None,
        placeholder="Выберите пример..."
    )

# Контейнер
cont = st.container(width=800)
with cont:
    if options is None:
        st.write('Пример не выбран')
        st.image("Python_Book.jpg", width=400)

    elif options == "Пример 9.1":
        with st.expander("🔍 Показать результат работы нейросети 💻"):
            fun_g9.run_9_1()

    elif options == "Пример 9.2":
        with st.expander("🔍 Показать результат работы нейросети 💻"):
            fun_g9.run_9_2()

    elif options == "Пример 9.3":
        with st.expander("🔍 Показать результат работы нейросети 💻"):
            fun_g9.run_9_3()

    elif options == "Пример 9.4":
        with st.expander("🔍 Показать результат работы нейросети 💻"):
            fun_g9.run_9_4()

    elif options == "Пример 9.5":
        with st.expander("🔍 Показать результат работы нейросети 💻"):
            fun_g9.run_9_5()

    elif options == "Пример 9.6":
        with st.expander("🔍 Показать результат работы нейросети 💻"):
            fun_g9.run_9_6()

    elif options == "Пример 9.7":
        with st.expander("🔍 Показать результат работы нейросети 💻"):
            fun_g9.run_9_7()

    elif options == "Пример 9.8":
        with st.expander("🔍 Показать результат работы нейросети 💻"):
            fun_g9.run_9_8()

    elif options == "Пример 9.9":
        with st.expander("🔍 Показать результат работы нейросети 💻"):
            fun_g9.run_9_9()

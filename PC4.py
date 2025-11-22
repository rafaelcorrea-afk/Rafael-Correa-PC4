# Antes de ejecutar un script de Python en Streamlit debes definir la carpeta donde se encuentra tus archivos
# cd ruta_de_tu_carpeta 
# o abrimos el folder desde visual Studio Code 


# Primero creamos un entorno virtual para instalar Streamlit y otras librerías que necesitemos.
# python -m venv .venv  (primer paso)
# Esto nos permite crear un entorno virtual donde instalaremos Streamlit 
# y observaremos la página web que se está generando en este script.

# Luego activamos el entorno virtual.
# En Windows:
# .venv\Scripts\activate
# deactivate
# En MacOS/Linux:
# source .venv/bin/activate

# Acontinuación instalamos Streamlit 
# pip install Streamlit (segundo paso)

# Este código sirve para acceder una página web en tu navegador que te brinda información sobre Streamlit.
# Pero se ejecuta en la terminal Python de tu computadora, no en Jupyter Notebook.
# python -m streamlit hello

# Este comando sirve para ejecutar un script de Python en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.
# OJO: Debes antes tener instalado Streamlit en tu computadora, debes antes definir la ruta de tus archivos y 
##     tener un script de Python (your_script.py) que quieras ejecutar en Streamlit.
# python -m streamlit run PC4.py  (tercer paso)
#  your_script.py

# Este código sirve para hacer un primer programa en Streamlit.
import streamlit as st

# Generamos 3 páginas en la aplicación web de Streamlit.
# Generamos una página principal, otra donde contaran su experiencia aprendiendo a programar y una tercera donde presentarán sus gráficos.

# Creamos la lista de páginas
paginas = ['Bienvenido a mi Bitácora', 'Mi Camino con el Código', 'Visualizando Datos']

# Creamos botones de navegación tomando la lista de páginas
pagina_seleccionada = st.sidebar.selectbox('Selecciona la sección que deseas ver', paginas)

# Generamos condicionales para mostrar el contenido de cada página
if pagina_seleccionada == 'Bienvenido a mi Bitácora':

    # La función st.markdown permite centrar y agrandar la letra del título de la web en Streamlit.
    st.markdown("<h1 style='text-align: center;'>Bitácora Audiovisual 2.0 🚀</h1>", unsafe_allow_html=True)

    # <h1 style='text-align: center;'>Nombre de tu blog</h1>: Esto es una cadena de código HTML. 
    # La etiqueta <h1> se utiliza para el encabezado principal de una página web, y 
    # el atributo style se utiliza para agregar estilos CSS. 
    # En este caso, el texto está alineado al centro (text-align: center;). 
    # Pueden agregar emojis en el texto de Markdown utilizando códigos de emoji, por ejemplo:
    # <h1 style='text-align: center;'>Aquí escribe un nombre creativo para tu blog 📝</h1>
    # También pueden personalizar el color del texto utilizando el atributo style, por ejemplo:
    # <h1 style='text-align: center; color: blue;'>Nombre de tu blog</h1>
    # El texto dentro de las etiquetas <h1> ("Aquí escribe un nombre creativo para tu blog") es el contenido del encabezado.

    # unsafe_allow_html=True: Este es un argumento opcional en la función markdown. 
    # Por defecto, streamlit no permite HTML en el texto de Markdown.
    # Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.

    # Creamos dos columnas separadas para la imagen y el texto
    col1, col2 = st.columns(2)

    # col1, col2 = st.columns(2): Esta línea está creando dos columnas en la interfaz de usuario de la aplicación web. 
    # La función st.columns toma un número entero como argumento que especifica el número de columnas que se deben crear. 
    # Las columnas creadas se asignan a las variables col1 y col2.

    # En la primera columna colocamos la imagen de perfil
    col1.image("perfil.jpg", caption='Rafael Correa 😎', width=300)

    # col1.image("ellie.png", caption='Ellie', width=300): Esta línea está colocando una imagen en la primera columna (col1). 
    # La función image toma como primer argumento el nombre del archivo de la imagen que se desea mostrar. 
    # En este caso, la imagen es "ellie.png". 
    # El argumento caption se utiliza para proporcionar una etiqueta a la imagen, 
    # en este caso "Aquí puedes escribir una etiqueta debajo de la imagen". 
    # El argumento width se utiliza para especificar el ancho de la imagen, en este caso 300 píxeles.

    # En la segunda columna colocamos el texto: Debe contener una presentación de ustedes
    # Deben presentarse: ¿Quién eres?, ¿De dónde eres?, ¿Qué estudias?, ¿Qué te gusta de tu carrera?, 
    # ¿Qué te gustaría hacer en el futuro?, ¿Qué te gusta hacer en tu tiempo libre?

    texto = """
    Soy Rafael Correa 🥷, estudiante de Comunicación Audiovisual en Lima, Perú. Estoy completamente enamorado de la creatividad y de todo lo que se puede construir con una buena idea y una cámara. Me apasionan la dirección, la creación de contenido y ese proceso medio loco donde una chispa creativa termina convertida en algo real. En el futuro me veo liderando equipos como director de comunicaciones en una empresa minera, manejando mi propia agencia de comunicación o marketing, o incluso llevando alguno de mis guiones a la pantalla. En mi tiempo libre recargo energías leyendo, viendo películas y jugando en línea, ya sea una partida de Clash Royale o unas teamfights intensas en League of Legends.
    """

    # Las comillas triples (""") en Python se utilizan para definir cadenas multilínea.
    
    # Mostramos el texto
    col2.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>", unsafe_allow_html=True)

    # <div style='text-align: justify; font-size: 15px;'>{texto}</div>: Esta es una cadena de código HTML. 
    # La etiqueta <div> se utiliza para agrupar contenido en HTML. 
    # En este caso, el texto está justificado (text-align: justify;). 
    # El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
    # El texto dentro de las etiquetas <div> es la variable texto.
    # f"": Esto es un f-string en Python.
    # Permite insertar el valor de una variable directamente en la cadena. 
    # En este caso, {texto} se reemplaza por el valor de la variable texto.

elif  pagina_seleccionada == 'Mi Camino con el Código':

    # Agregamos un título
    st.markdown("<h1 style='text-align: center;'>De Comunicador a Creador de Código 💡</h1>", unsafe_allow_html=True)

    # En esta sección debes describir y comentar tu experiencia aprendiendo a programar
    # ¿Cómo te sentiste al principio?, 
    # ¿Qué te ha enseñado la programación?, ¿Qué te gusta de programar?, 
    # ¿Qué te gustaría hacer con la programación en el futuro? 

    # Agregar un  texto para la respuesta
    texto_2 = """
    Cuando empecé a programar, estaba genuinamente interesado, pero jamás pensé que, siendo comunicador, terminaría escribiendo código en Python 😅. Solo había visto concursos de programación en YouTube con estudiantes de ingeniería haciendo trabajos como el clásico piedra-papel-tijera, y nunca imaginé que un día yo mismo lo programaría. Con el tiempo descubrí que programar es crear: construir fórmulas, pensar en sistemas y usar un lenguaje único para que la computadora haga exactamente lo que tú imaginas. Lo que más me gusta es la libertad creativa que ofrece, con métodos y posibilidades casi infinitas ✨. En el futuro me gustaría usar lo aprendido para crear páginas web, blogs o herramientas que realmente ayuden a las personas a alcanzar sus metas o aprender algo nuevo 💡. 
    """

    # Mostramos el texto
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_2}</div>", unsafe_allow_html=True)

    # <div style='text-align: justify; font-size: 15px;'>{texto_2}</div>: Esta es una cadena de código HTML.
    # La etiqueta <div> se utiliza para agrupar contenido en HTML.
    # En este caso, el texto está justificado (text-align: justify;).
    # El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
    # El texto dentro de las etiquetas <div> es la variable texto_2.
    # f"": Esto es un f-string en Python.
    # Permite insertar el valor de una variable directamente en la cadena. 
    # En este caso, {texto_2} se reemplaza por el valor de la variable texto.

    # Agregamos un subtítulo para el video
    st.markdown("<h2 style='text-align: center;'>Tomando Decisiones con Python</h2>", unsafe_allow_html=True)
    
    # <h2 style='text-align: center;'>Aquí escribe un nombre creativo para presentar tu video</h2>: Esta es una cadena de código HTML.
    # La etiqueta <h2> se utiliza para un encabezado de segundo nivel en una página web.
    # El texto está centrado (text-align: center;).
    # El texto dentro de las etiquetas <h2> ("Aquí escribe un nombre creativo para presentar tu video") es el contenido del encabezado.
    # unsafe_allow_html=True: Este es un argumento opcional en la función markdown.
    # Por defecto, streamlit no permite HTML en el texto de Markdown.
    # Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.
    # Puedes agregar emojis en el texto de Markdown utilizando códigos de emoji.
    # Por ejemplo, puedes agregar un emoji de video 🎥 

    # Agregamos un video realizado en las practicas anteriores
    st.video("https://youtu.be/KSDK61SQLXs")
    st.markdown("<h2 style='text-align: center;'>Repitiendo con Propósito: for y while</h2>", unsafe_allow_html=True)
    st.video("https://youtu.be/HaCTSaE67zo")
    # st.video("https://www.youtube.com/watch?v=X_Z7d04x9-E"): Esta línea está mostrando un video en la aplicación web.
    # La función video toma como primer argumento la URL del video que se desea mostrar.
    # En este caso, la URL es "https://www.youtube.com/watch?v=X_Z7d04x9-E".
    # Puedes cambiar la URL por la de tu video en YouTube o en otra plataforma de video.

    # O creamos un botón para ir al enlace del video con button
    # st.markdown(f"<div style='text-align: center;'><a href='https://drive.google.com/file/d/1REvRXSu3GuGD73w8j44135MkRiezd0gP/view?usp=drive_link' target='_blank'><button>Ver video</button></a></div>", unsafe_allow_html=True) 

    # <div style='text-align: center;'><a href='https://drive.google.com/file/d/1REvRXSu3GuGD73w8j44135MkRiezd0gP/view?usp=drive_link' target='_blank'><button>Ver video</button></a></div>:
    # Esta es una cadena de código HTML.
    # La etiqueta <div> se utiliza para agrupar contenido en HTML.
    # En este caso, el contenido está centrado (text-align: center;).
    # La etiqueta <a> se utiliza para crear un enlace.
    # El atributo href especifica la URL a la que se dirige el enlace.
    # En este caso, la URL es 'https://drive.google.com/file/d/1REvRXSu3GuGD73w8j44135MkRiezd0gP/view?usp=drive_link'.
    # El atributo target='_blank' indica que el enlace se abrirá en una nueva pestaña del navegador.
    # La etiqueta <button> se utiliza para crear un botón.
    # El texto dentro de las etiquetas <button> ("Ver video") es el contenido del botón.
    # unsafe_allow_html=True: Este es un argumento opcional en la función markdown.
    # Por defecto, streamlit no permite HTML en el texto de Markdown.
    # Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.
    # Puedes cambiar la URL por la de tu video en YouTube o en otra plataforma de video.
    
else:

    # Agregamos un título para la página de gráficos
    st.markdown("<h1 style='text-align: center;'>Visualizando Datos</h1>", unsafe_allow_html=True)

    # Creamos una lista de gráficos
    graficos = ['Gráfico de barras: tarjetas rojas como local', 'Histogramas: frecuencia de goles anotados y recibidos por el Real Madrid (local y visitante)', 'Gráfico de pastel: resultados del Barcelona como local (Temporada 2024/2025)', 'Gráfico de pastel: resultados del Barcelona como visitante (Temporada 2024/2025)', 'Mapa interactivo: localizaciones de mis películas favoritas', 'Mapa interactivo: distribución de la familia lingüística quechua']

    # Creamos un cuadro de selección en la página de gráficos
    grafico_seleccionado = st.selectbox('Selecciona un gráfico', graficos)

    # El cuadro de selección se crea con la función selectbox.
    # El primer argumento es el texto que se muestra en el cuadro de selección.
    # El segundo argumento es una lista de opciones que se pueden seleccionar.
    # En este caso, las opciones son los elementos de la lista graficos.
    # La opción seleccionada se asigna a la variable grafico_seleccionado.
    # La variable grafico_seleccionado se utiliza para mostrar el gráfico correspondiente en la aplicación web.
    

    # Mostramos el gráfico seleccionado
    if grafico_seleccionado == 'Gráfico de barras: tarjetas rojas como local':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>El gráfico muestra que el Alavés es el equipo que más tarjetas rojas recibió jugando como local, lo que podría reflejar un estilo defensivo más agresivo o partidos más tensos en su estadio. En contraste, Barcelona, Osasuna y Real Madrid no registran ninguna tarjeta roja como locales, lo que sugiere un mayor control emocional o estrategias menos propensas al juego brusco. Esta diferencia revela que el comportamiento disciplinario varía bastante entre equipos, incluso cuando juegan en casa, donde normalmente se espera más calma y control.</div>", unsafe_allow_html=True)
        st.image("barras.png", caption='Gráfico de barras', width=500)
        pass
    elif grafico_seleccionado == 'Histogramas: frecuencia de goles anotados y recibidos por el Real Madrid (local y visitante)':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>Los histogramas permiten observar cómo se distribuyen los goles del Real Madrid en la temporada 2024/2025, diferenciando entre juegos como local y como visitante. En los gráficos de goles anotados, se puede identificar si el equipo mantiene un rendimiento ofensivo constante o si existe mayor variabilidad dependiendo del lugar donde juega. En los histogramas de goles recibidos, se aprecia si la defensa es más sólida en el Bernabéu o si concede más goles fuera de casa. En conjunto, los cuatro gráficos muestran patrones que ayudan a entender el equilibrio entre ataque y defensa del equipo a lo largo de la temporada.</div>", unsafe_allow_html=True)
        st.image("histograma.png", caption='Histogramas', width=500)
        pass
    elif grafico_seleccionado == 'Gráfico de pastel: resultados del Barcelona como local (Temporada 2024/2025)':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>El gráfico de pastel muestra que el Barcelona tiene un rendimiento claramente dominante en el Camp Nou, con 73.7% de partidos ganados como local. La proporción de derrotas (21.1%) es considerablemente menor, lo que indica que perder en casa es una excepción más que una regla. Finalmente, los empates representan solo el 5.3%, lo que sugiere que sus partidos en casa suelen definirse de manera clara, sin resultados intermedios. En conjunto, los datos reflejan un fuerte desempeño local y una marcada superioridad competitiva en su estadio.</div>", unsafe_allow_html=True)
        st.image("pastel.png", caption='Gráfico de pastel', width=500)
        pass
    elif grafico_seleccionado == 'Gráfico de pastel: resultados del Barcelona como visitante (Temporada 2024/2025)':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>El gráfico de pastel evidencia que el Barcelona mantiene un rendimiento sólido incluso fuera de casa, con 73.7% de partidos ganados como visitante. La proporción de derrotas (10.5%) es baja, lo que indica que el equipo rara vez cae cuando juega lejos del Camp Nou. Los empates (15.8%) muestran que en algunos encuentros el rival logra equilibrar el marcador, pero sin comprometer el dominio general del Barcelona. En conjunto, los datos confirman que el equipo sostiene su alta calidad deportiva tanto de local como de visitante.</div>", unsafe_allow_html=True)
        st.image("pastel_2_visitante.png", caption='Gráfico de pastel', width=500)
        pass
    elif grafico_seleccionado == 'Mapa interactivo: localizaciones de mis películas favoritas':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>El mapa interactivo presenta las principales ciudades donde fueron grabadas mis películas favoritas, permitiendo visualizar cómo estas producciones se distribuyen geográficamente en distintos continentes. Cada marcador ofrece información básica y ayuda a entender la diversidad cultural y estética detrás de cada obra. Esta representación espacial facilita interpretar cómo las locaciones influyen en el tono, la atmósfera y la narrativa cinematográfica. En conjunto, el mapa convierte una lista de películas en una experiencia visual y exploratoria más dinámica.</div>", unsafe_allow_html=True)
        # Si "mapa_cusco.html" es un archivo HTML (no una imagen), debes mostrarlo con st.components.v1.html
        import streamlit.components.v1 as components
        with open("mapa_peliculas.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        components.html(html_content, height=500)
        pass
    elif grafico_seleccionado == 'Mapa interactivo: distribución de la familia lingüística quechua':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>El mapa interactivo muestra la presencia geográfica de las lenguas quechuas, evidenciando que su mayor concentración se encuentra en el Perú, donde la familia lingüística tiene su núcleo histórico y demográfico. También se observa una expansión significativa hacia Ecuador, lo que confirma su relevancia cultural en la región andina. En Colombia aparece con menor presencia, reflejando una influencia más limitada pero aún existente. En conjunto, el mapa permite visualizar de forma clara cómo esta familia lingüística se distribuye a lo largo de los Andes y cómo varía su intensidad según el país.</div>", unsafe_allow_html=True)
        # Si "mapa_cusco.html" es un archivo HTML (no una imagen), debes mostrarlo con st.components.v1.html
        import streamlit.components.v1 as components
        with open("mapa_lenguas.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        components.html(html_content, height=500)

    # if grafico_seleccionado == 'Gráfico de barras verticales de lenguas aisladas':
    # st.markdown("<div style='text-align: justify; font-size: 20px;'>Aquí debe ir una breve interpretación de tu gráfico</div>", unsafe_allow_html=True)
    # st.image("aisladas_base_datos.png", caption='Gráfico de lenguas aisladas', width=500): Esta línea está mostrando una imagen en la aplicación web.
    # La función image toma como primer argumento el nombre del archivo de la imagen que se desea mostrar.
    # En este caso, la imagen es "aisladas_base_datos.png".
    # El argumento caption se utiliza para proporcionar una etiqueta a la imagen,
    # en este caso "Gráfico de lenguas aisladas".
    # El argumento width se utiliza para especificar el ancho de la imagen, en este caso 500 píxeles.

    # elif grafico_seleccionado == 'mapa_cusco':
    # import streamlit.components.v1 as components
    # with open("mapa_cusco.html", "r", encoding="utf-8") as f:
    #     html_content = f.read()
    # components.html(html_content, height=500): Esta línea está mostrando un archivo HTML en la aplicación web.
    # La función components.html toma como primer argumento el contenido HTML que se desea mostrar.
    # En este caso, el contenido HTML se lee desde el archivo "mapa_cusco.html".
    # El argumento height se utiliza para especificar la altura del contenido HTML, en este caso 500 píxeles.
    
    # Si no tenemos el archivo HTML, podemos agregar el código para crear el mapa de Cusco directamente en Streamlit.
    # Primero debes crear el diccionario de coordenadas del mapa de Cusco.
    # Luego debes crear el mapa utilizando la librería folium y streamlit-folium.
    # pip install folium
    # pip install streamlit-folium
        #import folium
        #from streamlit_folium import st_folium

        # Mostrar el mapa en Streamlit
        #st_folium(mapa_cusco, width=700, height=500)
    
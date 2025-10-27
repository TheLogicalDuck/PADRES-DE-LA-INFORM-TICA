👨💻 MANUAL DE USUARIO
1. Objetivo
Este programa permite visualizar videos educativos sobre los pioneros de la informática,
mostrando sus aportes de forma interactiva y sencilla.
2. Instrucciones de instalación
1. Asegúrate de tener Python 3.10 o superior instalado.
2. Instala las dependencias necesarias:
3. pip install flet flet-video
4. Descarga todos los videos (.mp4) en la carpeta:
5. src/assets/
6. Ejecuta el programa con:
7. python main.py
3. Interfaz principal
Al iniciar el programa, verás:
 Un video del personaje actual.
 Su nombre y una breve descripción.
 Dos botones:
o ⯇ Anterior: muestra el personaje anterior.
o Siguiente ⯈: pasa al siguiente personaje.
4. Navegación
 Usa los botones “⯇ Anterior” y “Siguiente ⯈” para recorrer los distintos videos.
 Cada video se reproduce automáticamente.
 Puedes pausar o adelantar usando los controles del video.
5. Cierre del programa
Para cerrar, simplemente presiona la X de la ventana o detén la ejecución en la terminal (Ctrl +
C).
6. Mantenimiento
 Puedes agregar nuevos personajes añadiendo un nuevo diccionario al arreglo videos:
 {
 "titulo": "Nuevo personaje",
 "descripcion": "Descripción breve...",
 "video": "src/assets/NUEVO.mp4"
 }
 Asegúrate de que el video esté en la carpeta src/assets.


MANUAL TÉCNICO
1. Información general
Nombre del programa: Padres de la Informática
Lenguaje: Python
Bibliotecas utilizadas:
 flet: para la interfaz gráfica
 flet_video: para la reproducción de videos
Versión recomendada:
 Python 3.10 o superior
 Flet 0.23.2 o superior
 flet-video 0.4.0 o superior
2. Descripción general
Este programa muestra una interfaz gráfica que permite visualizar videos informativos
sobre los principales pioneros de la informática.
Incluye botones para avanzar y retroceder entre los diferentes personajes.
3. Estructura del código
3.1. Importaciones
import flet as ft
import flet_video as fv
 flet: Crea la ventana, botones, textos y contenedores.
 flet_video: Permite reproducir archivos de video (.mp4).
3.2. Función principal
def main(page: ft.Page):
Configura la página principal (page), estableciendo título, fondo y contenido inicial.
3.3. Lista de videos
videos = [
{"titulo": "...", "descripcion": "...", "video":
"src/assets/CHARLES.mp4"},
 ...
]
Contiene la información de cada científico: título, descripción y ruta del video.
3.4. Controles principales
 contenedor: área donde se muestra el video y la descripción.
 boton_anterior y boton_siguiente: permiten cambiar entre los videos.
3.5. Función mostrar_video()
Renderiza el contenido en pantalla.
Incluye:
 Reproductor de video (fv.Video)
 Textos con título y descripción
 Fila de botones para navegar
3.6. Funciones de navegación
def anterior_click(e):
 indice_actual[0] = (indice_actual[0] - 1) % len(videos)
 mostrar_video()
def siguiente_click(e):
 indice_actual[0] = (indice_actual[0] + 1) % len(videos)
 mostrar_video()
Actualizan el índice actual (indice_actual) y refrescan el contenido mostrado.
3.7. Inicialización de la aplicación
ft.app(target=main)
Inicia la aplicación de Flet ejecutando la función main.
4. Requisitos del sistema
Hardware mínimo:
 CPU: Dual-core 2.0 GHz
 RAM: 4 GB
 Almacenamiento: 500 MB libres
 Resolución: 1280x720 o superior
Software:
 Windows 10+, macOS 12+ o Linux Ubuntu 20.04+
 Python 3.10+
 Flet y flet_video instalados
Instalación de dependencias:
pip install flet flet-video

<img width="340" height="216" alt="image" src="https://github.com/user-attachments/assets/a3b7c37b-8641-4439-b4b0-5efe6354f1e7" />

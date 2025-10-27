import flet as ft
import flet_video as fv

def main(page: ft.Page):
    page.title = "Padres de la Informática"
    page.bgcolor = "#0A0A0A"
    page.window_width = 900
    page.window_height = 750
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    fuente_mono = "Consolas"

    videos = [
        {"titulo": "Charles Babbage", "descripcion": "Conocido como el padre de la computadora. Ideó la Máquina Analítica, precursora de los ordenadores modernos.", "video": "src/assets/CHARLES.mp4"},
        {"titulo": "Ada Lovelace", "descripcion": "Reconocida como la primera programadora del mundo. Escribió el primer algoritmo pensado para ser procesado por una máquina.", "video": "src/assets/ADA.mp4"},
        {"titulo": "Blaise Pascal", "descripcion": "Matemático, físico y filósofo francés. Inventó la Pascalina, una de las primeras calculadoras mecánicas.", "video": "src/assets/PASCAL.mp4"},
        {"titulo": "Alan Turing", "descripcion": "Padre de la computación moderna. Descifró el código Enigma y sentó las bases de la inteligencia artificial.", "video": "src/assets/TURING.mp4"},
        {"titulo": "John Von Neumann", "descripcion": "Desarrolló el modelo de arquitectura que aún usan las computadoras actuales.", "video": "src/assets/JOHN.mp4"},
        {"titulo": "Konrad Zuse", "descripcion": "Construyó la primera computadora programable (Z3) en 1941, un verdadero pionero alemán de la informática.", "video": "src/assets/KONRAD.mp4"},
    ]

    indice_actual = [0]

    # ELEMENTOS DE TEXTO
    titulo = ft.Text("", size=28, weight=ft.FontWeight.BOLD, color="#00FF9C", font_family=fuente_mono)
    descripcion = ft.Text("", size=17, color="#B0F8E6", italic=True, text_align=ft.TextAlign.CENTER, width=600, font_family=fuente_mono)
    texto_sistema = ft.Text("", color="#00FF9C", size=14, font_family=fuente_mono, italic=True)

    # CONTENEDOR DONDE SE MOSTRARÁ EL VIDEO
    contenedor_video = ft.Container(width=650, height=360)

    # FUNCIONES
    def mostrar_video():
        vid = videos[indice_actual[0]]
        titulo.value = vid["titulo"]
        descripcion.value = vid["descripcion"]
        texto_sistema.value = f"💾 Cargando archivo histórico: {vid['titulo']}..."

        # Reemplazamos el contenido del contenedor con un nuevo objeto Video
        contenedor_video.content = fv.Video(
            expand=True,
            width=650,
            height=360,
            autoplay=True,
            show_controls=True,
            playlist=[fv.VideoMedia(vid["video"])]
        )

        page.update()

    def anterior_click(e):
        indice_actual[0] = (indice_actual[0] - 1) % len(videos)
        mostrar_video()

    def siguiente_click(e):
        indice_actual[0] = (indice_actual[0] + 1) % len(videos)
        mostrar_video()

    # BOTONES
    boton_anterior = ft.ElevatedButton(
        "⯇ Anterior",
        on_click=anterior_click,
        bgcolor="#112C24",
        color="#00FF9C",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), padding=20, overlay_color="#00FF9C20")
    )

    boton_siguiente = ft.ElevatedButton(
        "Siguiente ⯈",
        on_click=siguiente_click,
        bgcolor="#112C24",
        color="#00FF9C",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), padding=20, overlay_color="#00FF9C20")
    )

    # INTERFAZ PRINCIPAL
    interfaz = ft.Column(
        [
            ft.Text("🧠 PROYECTO: PADRES DE LA INFORMÁTICA", size=32, color="#00FF9C", font_family=fuente_mono, weight=ft.FontWeight.BOLD),
            ft.Divider(color="#00FF9C", height=2),
            contenedor_video,
            titulo,
            descripcion,
            ft.Row([boton_anterior, boton_siguiente], alignment=ft.MainAxisAlignment.CENTER, spacing=60),
            ft.Divider(color="#00FF9C", height=2),
            texto_sistema,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15,
    )

    page.add(interfaz)
    mostrar_video()

ft.app(target=main)

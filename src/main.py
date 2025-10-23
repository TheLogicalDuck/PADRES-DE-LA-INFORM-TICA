import flet as ft
import flet_video as fv

def main(page: ft.Page):
    page.title = "Padres de la informática"
    page.bgcolor = ft.Colors.BLACK87

    videos = [
    {
        "titulo": "Charles Babbage",
        "descripcion": "Conocido como el padre de la computadora...",
        "video": "src/assets/CHARLES.mp4"
    },
    {
        "titulo": "Ada Lovelace",
        "descripcion": "Ada Lovelace fue reconocida como la primera programadora.",
        "video": "src/assets/ADA.mp4"
    },
    {
        "titulo": "Blaise Pascal",
        "descripcion": "Blaise Pascal fue matemático, físico y filósofo francés...",
        "video": "src/assets/PASCAL.mp4"
    },
    {
        "titulo": "Alan Turing",
        "descripcion": "Alan Mathison Turing fue un matemático, criptógrafo.​​​​ Es considerado como uno de los padres de la ciencia de la computación y precursor de la informática moderna.",
        "video": "src/assets/TURING.mp4"
    },
    {
        "titulo": "John Von",
        "descripcion": "John von Neumann fue un matemático y polimata húngaro-estadounidense que realizó contribuciones fundamentales en computación",
        "video": "src/assets/JOHN.mp4"
    },
    {
        "titulo": "Konrad Zuse",
        "descripcion": "Konrad Zuse fue un ingeniero alemán y un pionero de la computación. Su logro más destacado fue terminar la primera computadora controlada por programas que funcionaban, la Z3 en 1941.​",
        "video": "src/assets/KONRAD.mp4"
    }

]

    indice_actual = [0]
    contenedor = ft.Container(width=700, height=600)

    boton_anterior = ft.ElevatedButton("⯇ Anterior", width=150)
    boton_siguiente = ft.ElevatedButton("Siguiente ⯈", width=150)

    def mostrar_video():
        vid = videos[indice_actual[0]]
        contenedor.content = ft.Column(
            [
                fv.Video(
                    expand=True,
                    playlist=[fv.VideoMedia(vid["video"])],  # usamos VideoMedia
                    width=600,
                    height=350,
                    autoplay=True,
                    show_controls=True,
                ),
                ft.Text(vid["titulo"], size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                ft.Text(vid["descripcion"], size=16, italic=True, text_align=ft.TextAlign.CENTER, color=ft.Colors.WHITE70),
                ft.Row([boton_anterior, boton_siguiente],
                       alignment=ft.MainAxisAlignment.CENTER,
                       spacing=40)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        )
        page.update()

    def anterior_click(e):
        indice_actual[0] = (indice_actual[0] - 1) % len(videos)
        mostrar_video()

    def siguiente_click(e):
        indice_actual[0] = (indice_actual[0] + 1) % len(videos)
        mostrar_video()

    boton_anterior.on_click = anterior_click
    boton_siguiente.on_click = siguiente_click

    page.add(ft.Container(expand=True, alignment=ft.alignment.center, content=contenedor))
    mostrar_video()

ft.app(target=main)
#trying to push
import flet as ft
import flet_video as fv

def main(page: ft.Page):
    page.title = "Padres de la informática"
    page.bgcolor = ft.Colors.BLACK87

    videos = [
    {
        "titulo": "Charles Babbage",
        "descripcion": "Conocido como el padre de la computadora...",
        "video": "https://drive.google.com/uc?export=download&id=11quy5gjxoZLasWd2SvL-PSynA4JWY209"
    },
    {
        "titulo": "Ada Lovelace",
        "descripcion": "Ada Lovelace fue reconocida como la primera programadora.",
        "video": "https://drive.google.com/uc?export=download&id=1evn_myd6_yyNuXtXHt5r6eqJ4H2QjgU6"
    },
    {
        "titulo": "Blaise Pascal",
        "descripcion": "Blaise Pascal fue matemático, físico y filósofo francés...",
        "video": "https://drive.google.com/uc?export=download&id=1_fHCHd_vKIYKlZvf0XVChWRyD1i-HoRG"
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

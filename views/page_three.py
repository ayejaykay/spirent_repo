import flet as ft

def PageThree(page, ft=ft):
    content=ft.Column(
        [
        ft.Container(
            content=ft.Row(
            [
                ft.Column(
                    [
                    ft.Image(src="..\\assets\\icons\\imageBottom.png", height=600, width=600)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            ),
        # bgcolor="red",
        height=page.window_height,
        width=page.window_width*2,
        expand=True,
        ),
        ],
    )
    return content
    
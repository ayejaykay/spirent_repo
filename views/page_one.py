import flet as ft

def PageOne(page, ft=ft):
    content=ft.Column(
        [
        ft.Container(
            content=ft.Row(
            [
                ft.Column(
                    [
                    # ft.Text("This is Page One"),
                    # ft.Image(src="..\\logo.png", height=600, width=600)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            ),
        # bgcolor="orange",
        height=page.window_height,
        width=page.window_width*2,
        expand=True
        ),
        ],
    )
    return content
    
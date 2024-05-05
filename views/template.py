import flet as ft


def template_func(page):
    content=ft.Column(
        [
        ft.Container(
            content=ft.Row(
            [
                ft.Column(
                    [
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            ),
        # bgcolor="orange",
        height=page.window_height,
        width=page.window_width,
        ),
        ],
    )
    return content
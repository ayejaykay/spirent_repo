import flet as ft

import data.global_vars

FIRST_TEST, \
SECOND_TEST, \
= range(2)

class ImagePage:

    def __init__(self, page, rlMain) -> None:
        self.page = page
        self.rlMain = rlMain
        self.product_image = "..\\assets\\product_images\\nt108tx_stock.jpg"
        self.num_ports = 6
        self.status_bubbles = []
        self.port_status = ft.Row(self.fill_bubble_arr(), spacing=10,)
        self.images = ft.Row(expand=True, scroll="always", alignment=ft.MainAxisAlignment.CENTER)
        self.imgs_arr = data.global_vars.img_arr_1
        for i in self.imgs_arr:
            self.images.controls.append(ft.Image(src=i, fit=ft.ImageFit.CONTAIN))

    
    def ProductImagePage(self):
        content=ft.Column(
            [
            ft.Container(
                content=ft.Column(
                [
                    ft.Container(
                        content=ft.Row(
                            [
                                ft.Container(
                                    # content = self.images,
                                    content=ft.Column(
                                        [
                                            ft.Container(
                                                content=ft.Column(
                                                    [
                                                        self.images,
                                                    ],
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                ),
                                            height=self.page.window_height,
                                            width=self.page.window_width,
                                            bgcolor="orange",
                                            expand=True,
                                            ),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                height=self.page.window_height*2,
                                width=self.page.window_width,
                                expand=True,
                                bgcolor="purple",
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        height=self.page.window_height*2,
                        bgcolor="green",
                        expand=True,
                    ),
                    ft.Container(
                        content=ft.Row(
                            [
                                ft.Text("Connect spirent cables as shown in photos above.  Start test once all bubbles are green.", size=25, weight=ft.FontWeight.BOLD),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        padding=5,
                        # expand=True,
                    ),
                    ft.Container(
                        content=ft.Row(
                            [
                                self.port_status,
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        padding=20,
                        # expand=True
                    ),
                    ft.Container(
                        content=ft.Row(
                            [
                                ft.ElevatedButton(
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=10),
                                        bgcolor={
                                            ft.MaterialState.DEFAULT: ft.colors.RED_50,
                                            ft.MaterialState.HOVERED: ft.colors.RED_800,
                                            ft.MaterialState.FOCUSED: ft.colors.RED_800,
                                        },
                                        color={
                                            ft.MaterialState.DEFAULT: ft.colors.RED,
                                            ft.MaterialState.HOVERED: ft.colors.WHITE,
                                        },
                                        side={
                                            ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.RED_800),
                                        },
                                        padding=20,
                                    ),
                                    text="Start Spirent Test",
                                    height=50,
                                    width = 200,
                                    on_click=self.start_rl_page,
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        padding=5,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                ),
            # bgcolor="orange",
            height=self.page.window_height,
            width=self.page.window_width*2,
            expand=True,
            ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
        return content

    def fill_bubble_arr(self):
        for i in range(self.num_ports):
            self.status_bubbles.append(ft.Icon(name=ft.icons.CIRCLE_OUTLINED, color=ft.colors.BLACK, size=20))
        return self.status_bubbles

    def generate_images(self, opcode):
        if opcode == FIRST_TEST:
            self.imgs_arr = data.global_vars.img_arr_1
        if opcode == SECOND_TEST:
            self.imgs_arr = data.global_vars.img_arr_2
        for i in self.imgs_arr:
            self.images.controls.append(ft.Image(src=i, fit=ft.ImageFit.CONTAIN, border_radius=5))

    def start_rl_page(self, e):
        self.page.go("/rl")
        self.rlMain.print_results()


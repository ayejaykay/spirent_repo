import time
import flet as ft
import data.global_vars
from views.ascii_rl_logo import *


class RLMainPage:

    def __init__(self, page) -> None:
        self.page = page
        self.lv = ft.ListView(expand=True, spacing=0, padding=1, auto_scroll=True)

    def RLPage(self):
        content=ft.Row(
                    [
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Container(
                                        content=ft.Row(
                                            controls=[
                                                ft.Image(src="..\\assets\\icons\\RL_Logo_Full_Color.png", fit=ft.ImageFit.CONTAIN, expand=True)
                                            ],
                                        ),
                                        # bgcolor="orange",
                                    ),
                                    ft.Container(
                                        content=ft.Row(
                                            controls=[
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
                                                        }
                                                    ),
                                                    text="Test New Module",
                                                    height=50,
                                                    width = 200,
                                                    on_click=self.go_to_sn_page,
                                                ),
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
                                                        }
                                                    ),
                                                    text="Cancel Test",
                                                    height=50,
                                                    width = 200,
                                                    on_click=self.go_to_sn_page,
                                                ),
                                            ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        ),
                                    # bgcolor="purple",
                                    ),
                                ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            ),
                        # bgcolor="blue",
                        height=self.page.window_height*1.25,
                        width=self.page.window_width/2,
                        padding=5,
                        expand=True,
                        ), 
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    self.lv,
                                ],
                            ),
                        # bgcolor="green",
                        height=self.page.window_height*1.25,
                        width=self.page.window_width/2,
                        border=ft.border.all(1,ft.colors.RED_800),
                        border_radius=5,
                        padding=20,
                        expand=True,
                        ),
                    ],
                ) 
        return content



    def print_results(self):
        label_arr = ["Serial Number:\t\t", "Model:\t\t", "Test File:\t\t", "Physical Ports:\t\t", "Test Ports:\t\t", "Programmed:\t\t", "Number of Tests:\t\t", "Number of Fibers:\t\t", "Fiber Type:\t\t"]
        data_arr = [data.global_vars.serial_number, data.global_vars.model, data.global_vars.test_file, data.global_vars.physical_ports, data.global_vars.ports_for_file, data.global_vars.programmed, data.global_vars.num_tests, data.global_vars.fibers, data.global_vars.fiber_type]
        self.lv.controls.append(ft.Text(size=17, spans=[ft.TextSpan(data.global_vars.hostname, ft.TextStyle(color=ft.colors.GREEN_800, weight=ft.FontWeight.BOLD)), ft.TextSpan("@", ft.TextStyle(color=ft.colors.BLACK, weight=ft.FontWeight.NORMAL)), ft.TextSpan("10.11.1.45", ft.TextStyle(color=ft.colors.GREEN_800, weight=ft.FontWeight.BOLD))]))
        self.lv.controls.append(ft.Text(("-"*40), color=ft.colors.BLACK, weight=ft.FontWeight.NORMAL))
        for i in range(len(label_arr)):
            line = ft.TextSpan(label_arr[i], ft.TextStyle(color=ft.colors.BLACK54, weight=ft.FontWeight.BOLD))
            line1 = ft.TextSpan(data_arr[i], ft.TextStyle(color=ft.colors.BLACK, weight=ft.FontWeight.NORMAL))
            self.lv.controls.append(ft.Text(size=17, spans=[line, line1]))
            self.page.update()
            time.sleep(0.1)

    def go_to_sn_page(self,e):
        self.page.go("/sn")
        self.lv.controls.clear()
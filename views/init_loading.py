import flet as ft
import time

class LoadingPage:

    def __init__(self, page) -> None:
        self.page = page
        self.progress_text = ft.Text("Testing Text Writing", theme_style=ft.TextThemeStyle.TITLE_MEDIUM, color=ft.colors.RED_800)
        self.progress_percent = 0
        self.progress_bar = ft.Text(f"| {(chr(9601))*(40)} | [{self.progress_percent}%]", color=ft.colors.BLACK45, weight=ft.FontWeight.NORMAL)
        self.loading_bars = {
            0: 9603,
            1: 9606,
            2: 9608,
        }
        

    def LoadPage(self):
        content=ft.Column(
            [
            ft.Container(
                content=ft.Row(
                [
                    ft.Column(
                        [
                            self.progress_text,
                            self.progress_bar,
                            # ft.ProgressBar(width=400, color="red"),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
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
        )
        return content

    def InitLoadingPage(self, myRouter):
        self.page.go("/")
        time.sleep(0.5)
        myRouter.animate_opacity()
        time.sleep(1)
        myRouter.animate_opacity()
        self.page.go("/pa")
        time.sleep(3)
        myRouter.animate_opacity()
        time.sleep(3)
        myRouter.animate_opacity()
        self.page.go("/pb")
        time.sleep(3)
        myRouter.animate_opacity()
        time.sleep(3)
        myRouter.animate_opacity()
        self.page.go("/load")
        self.load_progress_bar()
        time.sleep(1.5)
        myRouter.animate_opacity()
        time.sleep(1.5)
        myRouter.set_opacity()
        self.page.go("/sn")


    def set_progress_text(self, text):
        self.progress_text.value = text
        self.page.update()

    def load_progress_bar(self):
        progress_txt_arr = ["Configuring Spirent", "Setting Environment", "Gathering Data"]
        for i in range(50):
            self.progress_percent = round((i / 49) * 100, 2)
            num_hastags = i
            self.progress_text.value = progress_txt_arr[(i//10)%3]
            self.progress_bar.value = ""
            self.progress_bar.value = f"| {chr(9608)*num_hastags}{(chr(9601))*(49-num_hastags)} | {chr(self.loading_bars[i%3])}{chr(self.loading_bars[(i+1)%3])}{chr(self.loading_bars[(i+2)%3])}{chr(self.loading_bars[(i+1)%3])} [{self.progress_percent}%]"
            self.page.update()
            time.sleep(0.1)


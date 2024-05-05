import flet as ft

from views.page_one import PageOne
from views.page_two import PageTwo
from views.page_three import PageThree
from views.serial_num_page import SerialNumberPage

class Router:

    def __init__(self, page, loadingPage, serialNumPage, img_page, rlMain, ft):
        self.page = page
        self.ft = ft
        self.routes = {
            "/": PageOne(page),
            "/pa": PageTwo(page),
            "/pb": PageThree(page),
            "/load": loadingPage.LoadPage(),
            "/sn": serialNumPage.SerNumPage(),
            "/img": img_page.ProductImagePage(),
            "/rl": rlMain.RLPage(),
        }
        self.body = ft.Container(content=self.routes["/"], expand=True, animate_opacity=ft.animation.Animation(duration=1000, curve="linear"))
        self.body.opacity = 1

    def route_change(self, route):
        self.body.content = self.routes[route.route]
        self.body.update()
    
    def animate_opacity(self):
        self.body.opacity = 0 if self.body.opacity == 1 else 1
        self.body.update()

    def set_opacity(self):
        self.body.opacity = 1
        self.body.update()

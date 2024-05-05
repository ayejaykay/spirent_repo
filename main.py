import data.global_vars
import flet as ft
import time

from src.RedlionSQL import RedlionSQL
from src.Globals import *

from views.Router import Router
from views.serial_num_page import SerialNumberPage
from views.init_loading import LoadingPage
from views.rl_main_page import RLMainPage
from views.module_image_page import ImagePage

data.global_vars.init()
data.global_vars.unit()
configure_spirent()

def main(page: ft.Page):

    ## Init Modules ##
    sql_ref = RedlionSQL("Test_Engineering_NTRON", "SpirentTester")

    ## Init Pages ##
    rlMain = RLMainPage(page)
    img_page = ImagePage(page, rlMain)
    serialNumPage = SerialNumberPage(page, sql_ref, img_page)
    loadingPage = LoadingPage(page)
    myRouter = Router(page, loadingPage, serialNumPage, img_page, rlMain, ft)

    page.on_route_change = myRouter.route_change

    page.add(
        myRouter.body
    )

    loadingPage.InitLoadingPage(myRouter)
  

if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")

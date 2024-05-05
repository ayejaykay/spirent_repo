import flet as ft
import data.global_vars
import data.dict

from src.Globals import *


SERIAL_BLANK,   \
SERIAL_DNE,     \
= range(2)

class SerialNumberPage:

    def __init__(self, page, sql_ref, image_page) -> None:
        self.page = page
        self.sql_ref = sql_ref
        self.image_page = image_page
        self.serial_num_field = ft.TextField(label="Scan Product Serial Number", hint_text="Patch X", height=100, width=500, border_color=ft.colors.RED_800)
        self.alert_flag = False
        self.error_dialog = ft.AlertDialog(
            title=ft.Text("INVALID SERIAL NUMBER!"),
            content=ft.Text("Serial number does not exist in database. Please enter a valid serial number into the textbox."),
            actions=[
                ft.TextButton("OK", on_click=self.close_dialog),
            ],
        )

    def SerNumPage(self):
        content=ft.Column(
            [
            ft.Container(
                content=ft.Column(
                [
                    ft.Row(
                        [
                            self.serial_num_field,
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row(
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
                                    }
                                ),
                                text="Start Spirent Test",
                                height=50,
                                width = 200,
                                on_click=self.start_image_page,
                            ),
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
    
    def open_dialog(self, opcode):

        if opcode == SERIAL_BLANK:
            self.error_dialog.title = ft.Text("ENTER SERIAL NUMBER")
            self.error_dialog.content = ft.Text("Enter a valid serial number to continue to the Spirent Test")

        if opcode == SERIAL_DNE:
            self.error_dialog.title = ft.Text("INVALID SERIAL NUMBER!")
            self.error_dialog.content = ft.Text("Serial number does not exist in database. Please enter a valid serial number into the textbox.")

        self.page.dialog = self.error_dialog
        self.error_dialog.open = True
        self.alert_flag = True
        self.page.update()

    def close_dialog(self, e):
        self.error_dialog.open = False
        self.alert_flag = False
        self.page.update()
    
    def wait_for_user(self):
        while(self.alert_flag):
            pass

    def valid_serial(self, serial_num):
        if serial_num == "":
            print("No serial number entered. Stopping test")
            serial_num = ""
            self.open_dialog(SERIAL_BLANK)
            self.wait_for_user()
            return False
        print(f"Serial number: {serial_num}")

        if not self.sql_ref.select_param_equal('UUT_SERIAL_NUMBER', 'UUT_SERIAL_NUMBER', serial_num).fetchval() == serial_num:
            print("Serial number does not exist in database")
            serial_num = ""
            self.open_dialog(SERIAL_DNE)
            self.wait_for_user()
            return False
        print(f"Serial number {serial_num} exists in database")
        return True

    def start_image_page(self, e):
        serial_num = self.serial_num_field.value

        if not self.valid_serial(serial_num):
            return
        
        model = self.sql_ref.get_model_from_serial_number(serial_num)
        data.global_vars.serial_number = serial_num
        data.global_vars.model = model
        data.global_vars.test_file = data.dict.product[model]['port_file']
        data.global_vars.ports_for_file = data.dict.file_num_ports[data.global_vars.test_file]
        data.global_vars.physical_ports = data.dict.product[model]['num_ports']
        data.global_vars.programmed = self.sql_ref.serial_is_programed(serial_num)

        num_ports_module = data.dict.product[model]['num_ports']
        num_spirent_ports = data.dict.file_num_ports[product[model]['port_file']]
        num_tests = num_ports_module // num_spirent_ports # This should mean the user would only have to enter the number of ports on the module and not the number of tests.
        if num_ports_module % num_spirent_ports:
            num_tests += 1 # This should take care of tests that aren't perfectly divisible by the number of spirent ports to the total ports.  ex is 10 ports on module using 8 spirent ports.  quotient is 1 but there is a remainder which means we need 2 tests

        data.global_vars.num_tests = num_tests
        data.global_vars.img_arr_1 = data.dict.product[model]['first_setup_image_path']
        data.global_vars.img_arr_2 = data.dict.product[model]['second_setup_image_path']
        data.global_vars.fibers = data.dict.product[model]['fibers']['num_fibers']
        data.global_vars.fiber_type = data.dict.product[model]['fibers']['fiber_type']

        test_func()

        self.page.go("/img")
        self.serial_num_field.value = ""
        self.image_page.generate_images(0)
        self.page.update()
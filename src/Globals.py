import data.global_vars
from data.dict import *
import os

def configure_spirent():
    os.system("hostname > hostname.txt")
    with open("hostname.txt", "r") as fp:
        file_data = fp.readlines()[0]
        file_data = file_data[:file_data.find("\\n")]
    data.global_vars.hostname = file_data
    os.remove("hostname.txt")
    os.system("netsh interface ip show config name=\"Spirent\" | findstr \"IP Address:\" > spirent_ip.txt")
    with open("spirent_ip.txt", "r") as fp:
        file_data = fp.readline()
        ip_arr = str(file_data).split(" ")
        ip_str = ip_arr[-1]
        spirent_ip = ip_str[:ip_str.find("\\n")]
    os.remove("spirent_ip.txt")
    print(spirent_ip)
    data.global_vars.hostname_ip = spirent_ip

def test_func():
    print(f"Hostname: {data.global_vars.hostname}")
    print(f"Hostname IP: {data.global_vars.hostname_ip}")
    print(f"Module Data for {data.global_vars.serial_number}: ")
    print(f"Serial Number: {data.global_vars.serial_number}")
    print(f"Model: {data.global_vars.model}")
    print(f"Number of Ports: {data.global_vars.physical_ports}")
    print(f"Test File: {data.global_vars.test_file}")
    print(f"Programmed: {data.global_vars.programmed}")
    print(f"Number of Tests: {data.global_vars.num_tests}")
    print(f"Images for Module (First Setup): {data.global_vars.img_arr_1}")
    print(f"Images for Module(Second Setup): {data.global_vars.img_arr_2}")
    print(f"Number of Fibers: {data.global_vars.fibers}")
    print(f"Fiber Type: {data.global_vars.fiber_type}")
    
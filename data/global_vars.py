def init():
    global kill_flag
    global restart_flag
    global ports_online
    global ps
    global online_ports_write
    global linking_killed
    global cancel_test_flag
    global hostname
    global hostname_ip
    kill_flag = False
    restart_flag = False
    ports_online = []
    online_ports_write = False
    linking_killed = False
    cancel_test_flag = False
    hostname = ""
    hostname_ip = ""

def unit():
    global serial_number
    global model 
    global test_file
    global physical_ports
    global ports_for_file
    global fibers
    global fiber_type
    global programmed
    global num_tests
    global img_arr_1
    global img_arr_2
    serial_number = ""
    model = ""
    test_file = ""
    physical_ports = 0
    ports_for_file = 0
    fibers = ""
    fiber_type = ""
    programmed = ""
    num_tests = 0
    img_arr_1 = []
    img_arr_2 = []


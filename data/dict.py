product = {
        'NT-1005TX-0000': {
            'port_file': '5Port_1000M_Burst',
            'num_ports': 5,
            'image_path': '',
        },
        'NT-1008TX-0000': {
            'port_file': '8Port_1000M_Burst',
            'num_ports': 8,
            'image_path': '',
        },
        'NT-104TX-0000': {
            'port_file': '4Port_100M_Burst',
            'num_ports': 4,
            'image_path': '',
        },
        'NT-105TX-0000': {
            'port_file': '5Port_100M_Burst',
            'num_ports': 5,
            'image_path': '',
        },
        'NT-108TX-0000': {
            'port_file': '8Port_100M_Burst',
            'num_ports': 8,
            'image_path': 'assets\\nt108tx_stock.jpg',
        },
        'NT-116TX-0000': {
            'port_file': '8Port_100M_Burst',
            'num_ports': 16,
            'image_path': 'assets\\nt116tx_stock.jpg',
        },
        '110FX2-ST': {
            'port_file': '8Port_100M_Burst',
            'num_ports': 10,
            'first_setup_image_path': ['..\\assets\\product_images\\110fx2\\apply_power.png', '..\\assets\\product_images\\110fx2\\port_numbers.png', '..\\assets\\product_images\\110fx2\\ports_connected.png'],
            'second_setup_image_path': ['..\\assets\\product_images\\110fx2\\fibers_connected_to_system.png', '..\\assets\\product_images\\110fx2\\fibers_connected_to_module.png'],
            'fibers': {
                'num_fibers': 2,
                'fiber_type': 'ST',
            }
        },
}

file_num_ports = {
        '3Port_100M_Burst': 3,
        '4Port_100M_Burst': 4,
        '5Port_100M_Burst': 5,
        '6Port_100M_Burst': 6,
        '8Port_100M_Burst': 8,
        '3Port_1000M_Burst': 3,
        '4Port_1000M_Burst': 4,
        '5Port_1000M_Burst': 5,
        '6Port_1000M_Burst': 6,
        '8Port_1000M_Burst': 8,
}

patch_id = {
        '10.11.1.31': 'A',
        '10.11.1.45': 'B',
        '10.11.1.15': 'C',
        '10.11.1.11': 'D', 
        '10.11.1.19': 'E',
        '10.11.1.79': 'F',
}

patch = {
    'A':
    [
        {"port_id": "//10.11.1.3/1/1", "port_num": 0},
        {"port_id": "//10.11.1.3/1/2", "port_num": 1},
        {"port_id": "//10.11.1.3/1/3", "port_num": 2},
        {"port_id": "//10.11.1.3/1/4", "port_num": 3},
        {"port_id": "//10.11.1.3/1/5", "port_num": 4},
        {"port_id": "//10.11.1.3/1/6", "port_num": 5},
        {"port_id": "//10.11.1.3/1/7", "port_num": 6},
        {"port_id": "//10.11.1.3/1/8", "port_num": 7},
    ],
    'B':
    [
        {"port_id": "//10.11.1.3/3/9", "port_num": 0},
        {"port_id": "//10.11.1.3/3/10", "port_num": 1},
        {"port_id": "//10.11.1.3/3/11", "port_num": 2},
        {"port_id": "//10.11.1.3/3/12", "port_num": 3},
        {"port_id": "//10.11.1.3/4/1", "port_num": 4},
        {"port_id": "//10.11.1.3/4/2", "port_num": 5},
        {"port_id": "//10.11.1.3/4/3", "port_num": 6},
        {"port_id": "//10.11.1.3/4/4", "port_num": 7},
    ],
    'C':
    [
        {"port_id": "//10.11.1.3/2/1", "port_num": 0},
        {"port_id": "//10.11.1.3/2/2", "port_num": 1},
        {"port_id": "//10.11.1.3/2/3", "port_num": 2},
        {"port_id": "//10.11.1.3/2/4", "port_num": 3},
        {"port_id": "//10.11.1.3/2/5", "port_num": 4},
        {"port_id": "//10.11.1.3/2/6", "port_num": 5},
        {"port_id": "//10.11.1.3/2/7", "port_num": 6},
        {"port_id": "//10.11.1.3/2/8", "port_num": 7},
    ],
    'D':
    [
        {"port_id": "//10.11.1.3/1/9", "port_num": 0},
        {"port_id": "//10.11.1.3/1/10", "port_num": 1},
        {"port_id": "//10.11.1.3/1/11", "port_num": 2},
        {"port_id": "//10.11.1.3/1/12", "port_num": 3},
        {"port_id": "//10.11.1.3/2/9", "port_num": 4},
        {"port_id": "//10.11.1.3/2/10", "port_num": 5},
        {"port_id": "//10.11.1.3/2/11", "port_num": 6},
        {"port_id": "//10.11.1.3/2/12", "port_num": 7},
    ],
    'E':
    [
        {"port_id": "//10.11.1.3/3/1", "port_num": 0},
        {"port_id": "//10.11.1.3/3/2", "port_num": 1},
        {"port_id": "//10.11.1.3/3/3", "port_num": 2},
        {"port_id": "//10.11.1.3/3/4", "port_num": 3},
        {"port_id": "//10.11.1.3/3/5", "port_num": 4},
        {"port_id": "//10.11.1.3/3/6", "port_num": 5},
        {"port_id": "//10.11.1.3/3/7", "port_num": 6},
        {"port_id": "//10.11.1.3/3/8", "port_num": 7},
    ],
    'F':
    [
        {"port_id": "//10.11.1.3/5/1", "port_num": 0},
        {"port_id": "//10.11.1.3/5/2", "port_num": 1},
        {"port_id": "//10.11.1.3/5/3", "port_num": 2},
        {"port_id": "//10.11.1.3/5/4", "port_num": 3},
        {"port_id": "//10.11.1.3/5/5", "port_num": 4},
        {"port_id": "//10.11.1.3/5/6", "port_num": 5},
        {"port_id": "//10.11.1.3/5/7", "port_num": 6},
        {"port_id": "//10.11.1.3/5/8", "port_num": 7},
    ],
}

# 08DEC237026TX$09    
# Format is always <7 char date><model>$<num>
#   - We should look to parse out the model

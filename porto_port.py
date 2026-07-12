import socket

ascii_banner = '''
 ████  ███   ███  █   █    █   █ █   █    ████   ███  ████  █████      ████    
█ ░░░░█ ░░░ █ ░░█ ██  █░   ██ ██░ █ █ ░   █░░░█ █ ░░█ █░░░█  ░█░░░   █ █░░░█   
 ███░░█░ ░░░█████░█░█ █░░  █░█ █░░ █ ░ ░  ████░░█░ ░█░████░░  █░░░░   ░████░░  
  ░░█ █░░   █░░░█░█░░██░░  █░░░█░░ █░ ░   █░░░░ █░░ █░█░░█░ ░ █░░    █ █░░░░ ░ 
████░░ ███  █░░░█░█░░ █░░  █░░ █░░ █░░    █░░░░░ ███ ░█░░░█░  █░░     ░█░░░░░  
 ░░░░ ░ ░░░  ░░  ░░░░  ░░   ░░  ░░  ░░     ░░     ░░░ ░░░  ░   ░░      ░░░     
  ░░░░   ░░░  ░   ░ ░   ░    ░   ░   ░      ░      ░░░  ░   ░   ░        ░     
'''
print(ascii_banner)
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        sock.close()
        return port if result == 0 else None
    except:
        return None

def scan_ports(ip, start_port, end_port):
    open_ports = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(scan_port, ip, port) for port in range(start_port, end_port + 1)]
        for future in futures:
            result = future.result()
            if result:
                open_ports.append(result)
    return open_ports

target_ip = ""
open_ports = scan_ports(target_ip, 1, 99999)
print(f"Open ports:

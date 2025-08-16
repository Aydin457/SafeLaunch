import socket
from utils import save_results

def run(url: str):
    print(f"\n[PORT] Scanning common ports for {url}...")
    hostname = url.replace("https://", "").replace("http://", "").split('/')[0]
    open_ports = []
    for port in [21, 22, 80, 443, 3306]:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            if sock.connect_ex((hostname, port)) == 0:
                print(f"  ✅ Port {port} is open")
                open_ports.append(port)
            sock.close()
        except Exception:
            continue
    save_results({"target": url, "open_ports": open_ports}, "port_scan")

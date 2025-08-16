import ssl
import socket
from utils import save_results

def run(url: str):
    print(f"\n[SSL] Checking SSL/TLS for {url}...")
    hostname = url.replace("https://", "").replace("http://", "").split('/')[0]
    context = ssl.create_default_context()
    try:
        with socket.create_connection((hostname, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                print(f"  ✅ SSL certificate is valid. Issuer: {cert.get('issuer')}")
                save_results({"target": url, "ssl_cert": cert}, "ssl_check")
    except Exception as e:
        print(f"  ⚠ SSL check failed: {e}")
        save_results({"target": url, "error": str(e)}, "ssl_check")

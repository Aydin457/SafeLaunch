import requests
from utils import save_results

def run(url: str):
    print(f"\n[AUTH] Checking login/register endpoints for {url}...")
    endpoints = ["/login", "/register"]
    found = []
    for ep in endpoints:
        try:
            r = requests.get(url + ep, timeout=5)
            if r.status_code < 400:
                print(f"  ✅ Endpoint exists: {ep}")
                found.append(ep)
        except:
            continue
    save_results({"target": url, "auth_endpoints": found}, "auth_check")

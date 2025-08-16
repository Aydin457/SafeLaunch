import requests
from utils import save_results

def run(url: str):
    print(f"\n[PATHS] Checking sensitive paths for {url}...")
    sensitive_paths = ["/admin", "/login", "/config.php", "/.env"]
    found = []
    for path in sensitive_paths:
        try:
            r = requests.get(url + path, timeout=3)
            if r.status_code < 400:
                print(f"  ⚠ Sensitive path found: {path}")
                found.append(path)
        except:
            continue
    save_results({"target": url, "sensitive_paths": found}, "paths")

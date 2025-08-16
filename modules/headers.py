import requests
from utils import save_results

def run(url: str):
    print(f"\n[HEADERS] Checking security headers for {url}...")
    try:
        response = requests.get(url, timeout=5)
        headers = response.headers

        required_headers = ["Content-Security-Policy", "Strict-Transport-Security", "X-Content-Type-Options", "X-Frame-Options", "Referrer-Policy"]
        missing = [h for h in required_headers if h not in headers]

        if missing:
            print(f"  ⚠ Missing important headers: {', '.join(missing)}")
        else:
            print("  ✅ All critical headers present.")

        result = {
            "target": url,
            "all_headers": dict(headers),
            "missing_headers": missing
        }
        save_results(result, "headers")
    except requests.RequestException as e:
        print(f"[-] Error: {e}")
        save_results({"target": url, "error": str(e)}, "headers")

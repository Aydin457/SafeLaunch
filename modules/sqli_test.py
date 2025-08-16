import requests
from utils import save_results

def run(url: str):
    print(f"\n[SQLi] Performing basic SQL injection test on {url}...")
    test_param = "?id=1' OR '1'='1"
    try:
        r = requests.get(url + test_param, timeout=5)
        vuln = "sql" in r.text.lower() or "error" in r.text.lower()
        print("  ⚠ SQLi vulnerability detected!" if vuln else "  ✅ No SQLi detected")
        save_results({"target": url, "sqli_vuln": vuln}, "sqli_test")
    except Exception as e:
        print(f"  ⚠ SQLi test failed: {e}")
        save_results({"target": url, "error": str(e)}, "sqli_test")

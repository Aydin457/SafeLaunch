import requests
from utils import save_results

def run(url: str):
    print(f"\n[XSS] Performing basic XSS test on {url}...")
    test_param = "?q=<script>alert(1)</script>"
    try:
        r = requests.get(url + test_param, timeout=5)
        vuln = "<script>alert(1)</script>" in r.text
        print("  ⚠ XSS vulnerability detected!" if vuln else "  ✅ No XSS detected")
        save_results({"target": url, "xss_vuln": vuln}, "xss_test")
    except Exception as e:
        print(f"  ⚠ XSS test failed: {e}")
        save_results({"target": url, "error": str(e)}, "xss_test")

import requests
from utils import save_results
import re

def run(url: str):
    print(f"\n[JS LEAK] Checking JS files for potential leaks on {url}...")
    try:
        r = requests.get(url, timeout=5)
        js_files = re.findall(r'<script src="(.*?)"', r.text)
        leak_found = [js for js in js_files if "key" in js.lower() or "token" in js.lower()]
        print(f"  ⚠ Potential leaks found in JS: {leak_found}" if leak_found else "  ✅ No JS leaks detected")
        save_results({"target": url, "js_leak": leak_found}, "js_leak")
    except Exception as e:
        print(f"  ⚠ JS check failed: {e}")
        save_results({"target": url, "error": str(e)}, "js_leak")

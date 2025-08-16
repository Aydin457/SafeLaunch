import requests
from utils import save_results

def run(url: str):
    print(f"\n[DEPS] Checking dependencies for {url}...")
    try:
        r = requests.get(url + "/package.json", timeout=5)
        vulnerable = []

        if r.status_code == 200 and r.text.strip():
            try:
                deps = r.json().get("dependencies", {})
                for dep in deps:
                    if "old" in dep.lower():
                        vulnerable.append(dep)
            except ValueError:
                print("  ⚠ JSON parse error: response not valid JSON")
        else:
            print("  ⚠ package.json not found or empty")

        print(f"  ⚠ Vulnerable dependencies: {vulnerable}" if vulnerable else "  ✅ No vulnerable dependencies found")
        save_results({"target": url, "vulnerable_deps": vulnerable}, "deps_check")
    except Exception as e:
        print(f"  ⚠ Dependency check failed: {e}")
        save_results({"target": url, "error": str(e)}, "deps_check")

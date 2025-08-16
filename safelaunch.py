#!/usr/bin/env python3
import argparse
import sys
from modules import headers, ssl_check, port_scan, paths, xss_test, sqli_test, traversal, auth_check, js_leak, deps_check

def banner():
    print("""
   ███████╗ █████╗ ███████╗███████╗██╗      █████╗ ██╗   ██╗███╗   ██╗ ██████╗██╗  ██╗
   ██╔════╝██╔══██╗██╔════╝██╔════╝██║     ██╔══██╗██║   ██║████╗  ██║██╔════╝██║  ██║
   ███████╗███████║███████╗█████╗  ██║     ███████║██║   ██║██╔██╗ ██║██║     ███████║
   ╚════██║██╔══██║██╔════╝██╔══╝  ██║     ██╔══██║██║   ██║██║╚██╗██║██║     ██╔══██║
   ███████║██║  ██║██╚╗    ███████╗███████╗██║  ██║╚██████╔╝██║ ╚████║╚██████╗██║  ██║
   ╚══════╝╚═╝  ╚═╝╚══╝    ╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝
                               SafeLaunch v1.0
                     Author: Aydın Yasinov
                     GitHub: https://github.com/Aydin457/SafeLaunch
    """)

def main():
    parser = argparse.ArgumentParser(
        description="SafeLaunch - Pre-deploy security scanner for developers.\n\n"
                    "This tool allows developers to perform basic security checks on their platforms before deployment.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "-u", "--url",
        help="Target URL to scan (e.g., https://example.com)",
        required=True
    )
    parser.add_argument(
        "-m", "--module",
        help=("Module to run. Options:\n"
              "  headers     - Check HTTP security headers\n"
              "  ssl         - Check SSL/TLS configuration\n"
              "  port        - Scan open ports\n"
              "  paths       - Detect sensitive paths/files\n"
              "  xss         - Basic XSS test\n"
              "  sqli        - Basic SQL Injection test\n"
              "  traversal   - Path traversal test\n"
              "  auth        - Authentication endpoint analysis\n"
              "  js          - JS files data leak check\n"
              "  deps        - Dependency vulnerability scan\n"
              "  all         - Run all modules"),
        required=True
    )
    args = parser.parse_args()

    url = args.url.strip()
    module = args.module.strip().lower()

    modules_map = {
        "headers": headers,
        "ssl": ssl_check,
        "port": port_scan,
        "paths": paths,
        "xss": xss_test,
        "sqli": sqli_test,
        "traversal": traversal,
        "auth": auth_check,
        "js": js_leak,
        "deps": deps_check
    }

    if module == "all":
        print(f"[+] Running all modules on {url}...\n")
        for mod_name, mod in modules_map.items():
            print(f"[INFO] Running {mod_name} module...")
            mod.run(url)
    elif module in modules_map:
        print(f"[+] Running {module} module on {url}...\n")
        modules_map[module].run(url)
    else:
        print("[-] Unknown module. Use --help for options.")

if __name__ == "__main__":
    try:
        banner()
        main()
    except KeyboardInterrupt:
        sys.exit("\n❌ Aborted by user.")

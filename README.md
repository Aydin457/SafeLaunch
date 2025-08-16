# 🛡️ SafeLaunch

**SafeLaunch** is a **modular, terminal-based pre-deploy security scanner** built for developers. It helps quickly check web platforms for common security issues before going live.

---

## ✨ Features

- 🔒 HTTP Security Headers Check
- 🔐 SSL/TLS Configuration Analysis
- 🌐 Open Port Scanning
- 📁 Sensitive Paths/Files Detection
- 🧪 Basic XSS Testing
- 💉 Basic SQL Injection Testing
- 🔄 Path Traversal Testing
- 👤 Authentication Endpoint Analysis
- 📜 JavaScript Data Leak Detection
- ⚠ Dependency Vulnerability Scanning

---

## 🛠️ Installation

```bash
git clone https://github.com/Aydin457/SafeLaunch.git
cd SafeLaunch
pip install -r requirements.txt
```
Requires Python 3.9 or higher.

## 🚀 Usage

Each module can be run independently:
```bash
python safelaunch.py -u https://example.com -m headers
python safelaunch.py -u https://example.com -m ssl
python safelaunch.py -u https://example.com -m port
python safelaunch.py -u https://example.com -m paths
python safelaunch.py -u https://example.com -m xss
python safelaunch.py -u https://example.com -m sqli
python safelaunch.py -u https://example.com -m traversal
python safelaunch.py -u https://example.com -m auth
python safelaunch.py -u https://example.com -m js
python safelaunch.py -u https://example.com -m deps
python safelaunch.py -u https://example.com -m all
```

Don’t forget to specify the target URL with the -u flag.

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

## 👨‍💻 Author

Developed by [Aydın Yasinov](https://github.com/Aydin457)

## ⚠️ Disclaimer

This tool is intended only for use on platforms you own or have explicit permission to test. Unauthorized use is strictly prohibited and is the sole responsibility of the user.

## 📬 Contact

## 📧 Email: yasinovaydin@gmail.com

🔗 Linkedin: [linkedin.com/in/aydın-yasinov](https://www.linkedin.com/in/aydın-yasinov/)


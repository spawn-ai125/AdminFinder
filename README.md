<div align="center">

<!-- Proje Logosu ve Havalı Başlık -->
<h1>⚡ AdminFinder v1.0.0 ⚡</h1>
<p align="center">
  <img src="https://shields.io" alt="Python Version">
  <img src="https://shields.io" alt="Security Tool">
  <img src="https://shields.io" alt="License">
</p>

<p><b>An ultra-clean, stealthy, and lightweight directory brute-forcing tool designed for cyber security enthusiasts and penetration testers.</b></p>

---
</div>

## 🎯 About The Project

**AdminFinder** is a professional command-line utility built in Python that automates the process of discovering hidden admin panels and login directories on target websites. By leveraging a customizable wordlist, it systematically probes web servers while remaining resilient against connection drops and timeouts.

### ✨ Key Features
* 🛡️ **Stealth Mode Enabled:** Suppresses cluttering "404 Not Found" errors to keep your terminal perfectly clean.
* 🤖 **Smart Error Handling:** Powered by robust `try-except` shields to survive network disconnects and slow server response times without crashing.
* 📂 **Dynamic Wordlist Support:** Reads thousands of payloads effortlessly from an external `wordlist.txt` file.
* 🎨 **Hacker-Style UI:** Features a custom ASCII banner upon startup to welcome you into your terminal auditing environment.

---

## 🚀 Getting Started

Follow these quick steps to deploy AdminFinder on your local penetration testing machine.

### 📋 Prerequisites
Make sure you have Python installed and the `requests` library configured:
```bash
pip install requests
```

### ⌨️ Installation & Setup
1. Clone the repository or download the files into a workspace directory.
2. Create a file named `wordlist.txt` in the exact same folder.
3. Populate your `wordlist.txt` with directories (e.g., `admin`, `login`, `wp-admin`, `dashboard`).

### 🎮 How to Run
Execute the script using your terminal:
```bash
python adminfinder.py
```
Simply enter your target URL when prompted (e.g., `https://example.com`) and let the tool audit the directory structure dynamically.

---

## 🛠️ Code Architecture Preview

The backend logic gracefully coordinates nested connection wrappers for maximum stability:

```text
       [ Start Tool ]
             │
      ( Load Banner )
             │
     [ Input Target URL ]
             │
    ┌────────┴────────┐
    ▼                 ▼
(Read wordlist)   (FileNotFound?) ──► [ Error Display & Exit ]
    │
    ▼
[ Loop Over Payloads ]
    │
    ├─► ( Append Path to URL )
    │
    ├─► [ Send HTTP GET Request ] ──► ( Timeout/Drop? ) ──► [ Pass Silently ]
    │
    └─► ( Status Code == 200? ) ──► 🟢 [ DISPLAY SUCCESS ]
```

---



---
<div align="center">
  <p><i>Disclaimer: This tool is intended for educational purposes and authorized penetration testing only. Do not use it against systems without explicit permission.</i></p>
</div>

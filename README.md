# 🕸️ Nexus-OSINT

<p align="center">
  <a href="#-english-documentation">🇬🇧 English Documentation</a> | 
  <a href="#-türkçe-dokümantasyon">🇹🇷 Türkçe Dokümantasyon</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Python 3.8+">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
  <img src="https://img.shields.io/badge/platform-Linux%20|%20macOS%20|%20Windows-lightgrey.svg" alt="Platform">
</p>

---

## 🇬🇧 English Documentation

**Nexus-OSINT** is a next-generation, terminal-based intelligence gathering and reporting assistant developed by **Existanyalist** for Cyber Threat Intelligence (CTI) analysts, penetration testers, and OSINT researchers.

Instead of getting lost in traditional browser tabs, it brings the massive database of the OSINT Framework, active target reporting, and instant IP analysis directly to your terminal under a single, modern TUI (Terminal User Interface).

### 🚀 Key Features
* **Advanced TUI:** A readable, colorful, and modern intelligence panel powered by the `Rich` library.
* **Active Intelligence (Shodan Integration):** Scans the target IP address for open ports, vulnerabilities (CVEs), and hostnames in seconds without requiring an API key.
* **Target Profiling & Reporting:** Take notes for the target (company/person) you are researching without leaving the terminal. The system automatically generates a timestamped `.txt` report.
* **Offline Mode (Cache):** Even if your internet connection drops or you are in an air-gapped network, continue browsing the tools using the locally cached database.
* **Favorites System:** Add your frequently used OSINT tools to your bookmarks and access your arsenal with a single keystroke.

### 🛠️ Installation & Setup
The tool is fully compatible with Linux (Kali, Parrot, Ubuntu), macOS, and Windows. Ensure you have **Python 3.8+** installed.

```bash
# 1. Clone the repository
git clone [https://github.com/existanyalist/NEXUS-OSINT-Framework.git](https://github.com/existanyalist/NEXUS-OSINT-Framework.git)

# 2. Navigate to the directory
cd NEXUS-OSINT-Framework

# 3. Install required dependencies 
pip install -r requirements.txt --break-system-packages

# 4. Run the engine
python osint_master.py

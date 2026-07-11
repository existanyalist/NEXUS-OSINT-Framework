<div align="center">

# 🕸️ NEXUS-OSINT

### *Next-Generation Terminal-Based Open Source Intelligence & CTI Framework*

<p align="center">
  <img src="https://img.shields.io/badge/Version-1.0.0-cyberpunk?style=for-the-badge&labelColor=111111&color=00ff66" alt="Version">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&labelColor=111111&color=007acc" alt="Python">
  <img src="https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey?style=for-the-badge&labelColor=111111&color=888888" alt="Platform">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge&labelColor=111111&color=ffcc00" alt="License">
</p>

---

[🇹🇷 Türkçe Dokümantasyon İçin Buraya Tıklayın](#-türkçe-dokümantasyon)

---

<!-- ANIMATED TERMINAL GIF AREA -->
<img src="https://raw.githubusercontent.com/existanyalist/NEXUS-OSINT-Framework/main/assets/terminal_demo.gif" alt="Nexus-OSINT Terminal Demo" width="800" style="max-width:100%; border-radius: 8px;">

</div>

---

## 🚀 Key Features

*   **⚡ Advanced TUI:** A responsive, highly readable, and colorful terminal user interface powered by the `Rich` engine.
*   **📡 Active Intelligence:** Instantly query Shodan InternetDB to extract open ports, vulnerabilities (CVEs), and hostnames without an API key.
*   **📝 Automated Reporting:** Take real-time notes on targets and export structured, timestamped intelligence reports effortlessly.
*   **🔌 Offline Mode (Cache):** Continue working inside air-gapped networks or during outages using the locally cached database layout.
*   **⭐ Bookmarks Engine:** Save your high-priority OSINT assets to a centralized favorites panel for single-keystroke execution.

---

## ❓ Why Nexus?

Traditional threat intelligence workflows often result in browser tab clutter and unorganized local text files. **Nexus-OSINT** bridges the gap by housing the entire structured OSINT Framework tree inside an optimized, offline-capable terminal architecture. It keeps your eyes on the terminal, your targets mapped, and your evidence logs automatically formatted.

---

## 🏗️ Architecture & Core Components

### 1. Active Intelligence (Shodan Integration)
Queries the target network peripheral infrastructure dynamically using asynchronous endpoint lookups. It strips out noise and maps exposure levels.

### 2. Reporting Engine
A systematic session logger that streams targeted outputs, automated findings, and manual operator notes straight into `<target>_OSINT_Raporu.txt`.

### 3. Offline Cache Layer
Maintains structural operational stability. If external networks drop, the engine rolls over to a local JSON abstraction layer.

### 4. Favorites Manager
A volatile state management engine that tracks highly utilized security nodes across the framework hierarchy for rapid tactical deployment.

---

## 🛠️ Installation

Ensure you have **Python 3.8+** deployed on your architecture.

```bash
# Clone the core repository
git clone [https://github.com/existanyalist/NEXUS-OSINT-Framework.git](https://github.com/existanyalist/NEXUS-OSINT-Framework.git)

# Navigate into the deployment folder
cd NEXUS-OSINT-Framework

# Deploy missing runtime dependencies
pip install -r requirements.txt --break-system-packages

# Launch the engine
python osint_master.py
⌨️ Usage & Keyboard Shortcuts
When initialization completes, you can globally hook a active target profile or bypass straight to database navigation.

[A] Active Intelligence Mode: Triggers automated Shodan exposure mapping on specified target IP vectors.

[T] Change Target: Hot-swaps the current intelligence scope to a separate infrastructure entity.

[N] Inject Note: Appends manual operator intelligence notes straight to the active target artifact file.

[F] Favorites Arsenal: Instantly populates the customized interface listing your bookmarked utilities.

[2] Bookmark Node: Pressing 2 while inspecting any asset appends it to your quick-access favorites menu.

[0] Escape / Back: Gracefully drops back one structural layer or kills the active process execution loop.

📸 Screenshots
📂 Folder Structure
Plaintext
NEXUS-OSINT-Framework/
├── assets/                  # Documentation graphics and terminal demos
├── osint_master.py          # Main application core logic engine
├── osint_cache.json         # Offline local database layer
├── requirements.txt         # Package execution dependencies
├── .gitignore               # Deployment file exclusion criteria
└── README.md                # System documentation framework
🗺️ Roadmap
[x] Core TUI Dashboard Integration via Rich Engine

[x] Global Shodan Passive API Recon Node

[ ] Active Threat Intel Feed Stripping (AlienVault/OTX)

[ ] Automated HTML Web Reporting Template Generator

[ ] Multi-threaded Target Infrastructure Validation

🤝 Contributing
Fork the framework distribution vector.

Initialize your local branch configuration (git checkout -b feature/AmazingFeature).

Commit your optimization modifications (git commit -m 'Add some AmazingFeature').

Push directly into your upstream origin dal (git push origin feature/AmazingFeature).

Open an official Pull Request for validation.

💬 FAQ
Q: Do I require paid API integrations for Shodan mapping?

A: No, the system routes queries through the unauthenticated InternetDB pipeline for lightning-fast port checks.

Q: Where are my evidence files saved?

A: Everything is rendered locally inside the exact operational directory where osint_master.py resides.

⚠️ Disclaimer
This deployment is engineered strictly for authorized academic research, offensive/defensive security auditing, and certified penetration testing protocols. The developer assumes absolutely zero legal liability or responsibility for unauthorized infrastructural damage, illicit surveillance, or malicious misuse of this open-source application framework.

📄 License
Distributed entirely under the conditions of the MIT License. Check out LICENSE for structural context.

🇹🇷 Türkçe Dokümantasyon
Terminal Tabanlı Yeni Nesil Açık Kaynak İstihbaratı & CTI Çerçevesi
Nexus-OSINT, Siber Tehdit İstihbaratı (CTI) analistleri, sızma testi uzmanları ve OSINT araştırmacıları için Existanyalist tarafından özel olarak optimize edilmiş, gelişmiş bir terminal terminal arayüzüdür. Tarayıcı sekmelerinde kaybolmak yerine tüm operasyonel bilgi akışını tek ekran üzerinden yönetmenizi sağlar.

⚙️ Temel Kabiliyetler
API anahtarı olmadan Shodan üzerinden zafiyet (CVE) ve açık port analizi.

Canlı hedef takibi ve otomatik tarih damgalı istihbarat raporlaması.

İnternet kesintilerinde devreye giren yerel JSON önbellek mimarisi.

2 tuşu ile ağaç yapısındaki herhangi bir aracı favori cephaneliğinize ekleme lüksü.

🚀 Hızlı Kurulum
Bash
git clone [https://github.com/existanyalist/NEXUS-OSINT-Framework.git](https://github.com/existanyalist/NEXUS-OSINT-Framework.git)
cd NEXUS-OSINT-Framework
pip install -r requirements.txt --break-system-packages
python osint_master.py
⌨️ Kısayol Matrisi
[A] Active Intel: Hedef IP adresinin güvenlik açıklıklarını listeler.

[T] Hedef Değiştir: Operasyonel odağı başka bir profile kaydırır.

[N] Not Ekle: İnceleme altındaki hedefe anlık analiz girdisi yazar.

[F] Favoriler: Sık kullanılan araçları tek ekranda toplar.

[0] Geri / Çıkış: Üst menü katmanına döner veya uygulamayı kapatır.

Developed with 🖤 by Existanyalist

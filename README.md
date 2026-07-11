# 🕸️ Nexus-OSINT

🇬🇧 English Documentation | 🇹🇷 Türkçe Dokümantasyon

---

## English Documentation

Nexus-OSINT is a next-generation, terminal-based intelligence gathering and reporting assistant developed by Existanyalist for Cyber Threat Intelligence (CTI) analysts, penetration testers, and OSINT researchers.

Instead of getting lost in traditional browser tabs, it brings the massive database of the OSINT Framework, active target reporting, and instant IP analysis directly to your terminal under a single, modern TUI (Terminal User Interface).

### 🚀 Key Features

* Advanced TUI: A readable, colorful, and modern intelligence panel powered by the Rich library.
* Active Intelligence (Shodan Integration): Scans the target IP address for open ports, vulnerabilities (CVEs), and hostnames in seconds without requiring an API key.
* Target Profiling & Reporting: Take notes for the target (company/person) you are researching without leaving the terminal. The system automatically generates a timestamped .txt report.
* Offline Mode (Cache): Even if your internet connection drops or you are in an air-gapped network, continue browsing the tools using the locally cached database.
* Favorites System: Add your frequently used OSINT tools to your bookmarks and access your arsenal with a single keystroke.

### 🛠️ Installation & Setup

The tool is fully compatible with Linux (Kali, Parrot, Ubuntu), macOS, and Windows. Ensure you have Python 3.8+ installed.

git clone https://github.com/existanyalist/NEXUS-OSINT-Framework.git
cd NEXUS-OSINT-Framework
pip install -r requirements.txt --break-system-packages
python osint_master.py

### ⌨️ Usage & Shortcuts

When you launch Nexus-OSINT, you can optionally set a "Research Target". Once a target is set, the reporting engine becomes active.

* [A] Active Intelligence: Scans a target IP address via Shodan InternetDB for free. You can append the results directly to your target report.
* [T] Set New Target: Change your focus to another entity during your research.
* [N] Add Note to Target: Quickly log information about the tool or data you are viewing. Saved to <target_name>_OSINT_Raporu.txt.
* [F] My Favorite Tools: Displays a list of tools you have bookmarked using the 2 key.
* [0] Go Back / Exit: Navigate to the upper menu or exit the application.

### ⚠️ Disclaimer

This software is developed open-source solely for academic research, defensive cybersecurity operations, and authorized penetration testing. The legal responsibility for the intelligence gathered and the data queried using this tool lies entirely with the end-user. The developer assumes no legal or criminal liability.

---

## 🇹🇷 Türkçe Dokümantasyon

Nexus-OSINT, siber istihbarat (CTI) analistleri, sızma testi uzmanları ve OSINT araştırmacıları için Existanyalist tarafından geliştirilmiş yeni nesil, terminal tabanlı bir bilgi toplama ve raporlama asistanıdır.

Geleneksel tarayıcı sekmelerinde kaybolmak yerine; OSINT Framework'ün devasa veritabanını, aktif hedef raporlamasını ve anlık IP analizini tek bir TUI (Terminal User Interface) altında toplar.

### 🚀 Öne Çıkan Özellikler

* Gelişmiş TUI: Rich kütüphanesi ile güçlendirilmiş, okunabilir, renkli ve modern bir istihbarat paneli.
* Aktif İstihbarat (Shodan Entegrasyonu): Hedef IP adresinin açık portlarını, zafiyetlerini (CVE) ve host isimlerini API anahtarı gerektirmeden saniyeler içinde tarar.
* Hedef Profilliği & Raporlama: Araştırdığınız hedef (şirket/kişi) için terminalden çıkmadan notlar alın. Sistem size otomatik olarak tarih damgalı bir .txt raporu sunar.
* Çevrimdışı Önbellek: İnternet bağlantınız kopsa veya izole bir ağda olsanız bile, önbelleğe alınmış yerel veritabanı ile araçlar arasında gezinmeye devam edin.
* Favoriler Sistemi: Sık kullandığınız OSINT araçlarını yer imlerine ekleyin ve cephaneliğinize tek tuşla erişin.

### 🛠️ Kurulum ve Çalıştırma

Araç; Linux (Kali, Parrot, Ubuntu), macOS ve Windows ortamlarında tam uyumlu çalışır. Sisteminize Python 3.8 veya üzeri bir sürümün yüklü olduğundan emin olun.

git clone https://github.com/existanyalist/NEXUS-OSINT-Framework.git
cd NEXUS-OSINT-Framework
pip install -r requirements.txt --break-system-packages
python osint_master.py

### ⌨️ Kullanım Kılavuzu ve Kısayollar

Nexus-OSINT'i başlattığınızda sistem opsiyonel olarak bir "Araştırma Hedefi" belirlemenizi ister. Hedef belirlediğiniz an raporlama motoru aktifleşir.

* [A] Aktif İstihbarat: Hedef IP adresini Shodan InternetDB üzerinden ücretsiz tarar. Sonucu doğrudan hedef raporunuza ekleyebilirsiniz.
* [T] Yeni Hedef Belirle: Araştırmanızın ortasında odağınızı başka bir varlığa kaydırmak isterseniz kullanılır.
* [N] Hedefe Not Ekle: İncelediğiniz bir araç hakkında hızlıca not almak için kullanılır. Notlar <hedef_adi>_OSINT_Raporu.txt dosyasına kaydedilir.
* [F] Favori Araçlarım: OSINT Framework menülerinde gezerken 2 tuşuyla favorilerinize eklediğiniz araçları tek bir listede gösterir.
* [0] Geri Dön / Çıkış: Hangi derinlikte olursanız olun bir üst menüye dönmenizi sağlar.

### ⚠️ Yasal Uyarı

Bu yazılım yalnızca akademik araştırma, savunma amaçlı siber gelecek operasyonları ve yetkili sızma testleri için açık kaynak kodlu olarak geliştirilmiştir. Bu araç kullanılarak elde edilen istihbaratın ve sorgulanan verilerin yasal sorumluluğu tamamen aracı kullanan son kullanıcıya aittir. Geliştirici hiçbir hukuki veya cezai yükümlülük kabul etmez.

---
Developed with 🖤 by Existanyalist

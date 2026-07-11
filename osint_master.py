import os
import sys
import json
import webbrowser
import requests
from datetime import datetime

try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.prompt import Prompt
    from rich import print as rprint
except ImportError:
    print("[-] Lütfen gerekli kütüphaneleri yükleyin: pip install requests rich")
    sys.exit(1)

console = Console()

CACHE_FILE = "osint_cache.json"
FAVS_FILE = "favorites.json"
URL = "https://raw.githubusercontent.com/lockfale/OSINT-Framework/master/public/arf.json"

target_name = ""
favorites = []

def load_data():
    if os.path.exists(CACHE_FILE):
        console.print(f"[bold yellow][*] {CACHE_FILE} önbellek dosyası bulundu. Kontrol ediliyor...[/bold yellow]")
        
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept": "application/json"
    }
    
    try:
        response = requests.get(URL, headers=headers, timeout=5)
        response.raise_for_status()
        data = response.json()

        with open(CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f)
        console.print("[bold green][+] Veriler GitHub'dan başarıyla çekildi ve önbelleğe kaydedildi.[/bold green]")
        return data
    except Exception as e:
        console.print(f"[bold red][-] Bağlantı hatası: {e}[/bold red]")
        if os.path.exists(CACHE_FILE):
            console.print("[bold green][+] İnternet bağlantısı yok. Çevrimdışı önbellek modu başlatılıyor...[/bold green]")
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        else:
            console.print("[bold red][!] Önbellek dosyası yok ve internete bağlanılamıyor. Çıkış yapılıyor.[/bold red]")
            sys.exit(1)

def load_favorites():
    global favorites
    if os.path.exists(FAVS_FILE):
        with open(FAVS_FILE, "r", encoding="utf-8") as f:
            favorites = json.load(f)

def save_favorites():
    with open(FAVS_FILE, "w", encoding="utf-8") as f:
        json.dump(favorites, f, indent=4)

def add_to_favorites(name, url):
    if not any(f['url'] == url for f in favorites):
        favorites.append({"name": name, "url": url})
        save_favorites()
        console.print(f"[bold green][+] '{name}' favorilere eklendi![/bold green]")
    else:
        console.print("[bold yellow][!] Bu araç zaten favorilerinizde.[/bold yellow]")

def display_favorites():
    if not favorites:
        console.print("[bold yellow][!] Henüz favori aracınız yok.[/bold yellow]")
        input("\nDevam etmek için ENTER...")
        return
    
    table = Table(title="Favori Araçlarım", style="cyan")
    table.add_column("No", style="magenta", justify="center")
    table.add_column("Araç Adı", style="green")
    table.add_column("URL", style="blue")
    
    for idx, fav in enumerate(favorites, 1):
        table.add_row(str(idx), fav['name'], fav['url'])
        
    console.print(table)
    input("\nDevam etmek için ENTER...")

def add_note():
    if not target_name:
        console.print("[bold red][-] Aktif bir hedef profili yok. Lütfen ana menüden bir hedef belirleyin.[/bold red]")
        return
    
    note = Prompt.ask(f"[bold cyan]'{target_name}' için notunuzu girin[/bold cyan]")
    filename = f"{target_name}_OSINT_Raporu.txt"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] - {note}\n")
    console.print(f"[bold green][+] Not '{filename}' dosyasına kaydedildi![/bold green]")

def active_intelligence():
    console.clear()
    panel = Panel("[bold cyan]Aktif İstihbarat Modülü (Shodan InternetDB API)[/bold cyan]\nBu modül hedef IP adresinin açık portlarını ve host isimlerini ücretsiz sorgular.", style="green")
    console.print(panel)
    
    ip_address = Prompt.ask("\n[bold yellow]Hedef IP Adresini Girin (Çıkmak için 0)[/bold yellow]")
    if ip_address == '0': return

    try:
        console.print("[bold blue][*] Shodan üzerinden sorgulanıyor...[/bold blue]")
        res = requests.get(f"https://internetdb.shodan.io/{ip_address}", timeout=10)
        
        if res.status_code == 404:
            console.print("[bold red][-] Bu IP için Shodan veritabanında kayıt bulunamadı.[/bold red]")
        elif res.status_code == 200:
            data = res.json()
            table = Table(title=f"IP Analiz Sonucu: {ip_address}", style="magenta")
            table.add_column("Özellik", style="cyan", justify="right")
            table.add_column("Değer", style="green")
            
            table.add_row("Host İsimleri", ", ".join(data.get("hostnames", ["Yok"])))
            table.add_row("Açık Portlar", ", ".join(map(str, data.get("ports", ["Yok"]))))
            table.add_row("Zafiyetler (CVE)", ", ".join(data.get("vulns", ["Bulunamadı"])))
            table.add_row("Etiketler", ", ".join(data.get("tags", ["Yok"])))
            
            console.print(table)
            
            if target_name:
                save_opt = Prompt.ask("[bold yellow]Bu sonucu rapora kaydetmek ister misin? (e/h)[/bold yellow]").lower()
                if save_opt == 'e':
                    filename = f"{target_name}_OSINT_Raporu.txt"
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(f"\n--- IP TARAMASI: {ip_address} ---\nAçık Portlar: {data.get('ports')}\nHostlar: {data.get('hostnames')}\n")
                    console.print("[bold green][+] Rapora eklendi![/bold green]")
        else:
            console.print(f"[bold red][-] API Hatası: {res.status_code}[/bold red]")
            
    except Exception as e:
        console.print(f"[bold red][-] Sorgu sırasında hata oluştu: {e}[/bold red]")
        
    input("\nDevam etmek için ENTER...")

def handle_url_node(node):
    while True:
        console.clear()
        panel = Panel(f"[bold white]URL:[/bold white] [bold blue]{node.get('url')}[/bold blue]", title=f"[bold green]Araç: {node.get('name')}[/bold green]", style="cyan")
        console.print(panel)
        
        console.print("[bold yellow]1.[/bold yellow] Tarayıcıda Aç")
        console.print("[bold yellow]2.[/bold yellow] Favorilere Ekle")
        console.print("[bold yellow]3.[/bold yellow] Hedef Raporuna Not Ekle")
        console.print("[bold red]0.[/bold red] Geri Dön")
        
        choice = Prompt.ask("\n[bold cyan]İşlem[/bold cyan]")
        
        if choice == '1':
            console.print("[*] Tarayıcı açılıyor...")
            webbrowser.open(node.get('url'))
        elif choice == '2':
            add_to_favorites(node.get('name'), node.get('url'))
            input("\nDevam etmek için ENTER...")
        elif choice == '3':
            add_note()
            input("\nDevam etmek için ENTER...")
        elif choice == '0':
            return

def display_menu(node, path=[]):
    global target_name

    while True:
        console.clear()
        current_path = " > ".join(path) if path else "Kök Dizin"

        header_text = f"[bold white]Hedef Profil:[/bold white] [bold red]{target_name if target_name else 'BELİRLENMEDİ'}[/bold red] | [bold white]Konum:[/bold white] [bold cyan]{current_path}[/bold cyan]"
        console.print(Panel(header_text, title="[bold magenta]Exist-OSINT FRAMEWORK TERMINAL[/bold magenta]"))

        children = node.get("children", [])
        
        if not children:
            if node.get("type") == "url":
                handle_url_node(node)
                return
            else:
                console.print("[bold yellow][-] Bu kategoride içerik bulunamadı.[/bold yellow]")
                input("\nGeri dönmek için ENTER...")
                return

        table = Table(show_header=False, box=None)
        table.add_column("No", style="yellow")
        table.add_column("Tip", style="cyan")
        table.add_column("Adı", style="white")

        for idx, child in enumerate(children, 1):
            icon = "📁" if "children" in child else "🔗"
            table.add_row(f"[{idx}]", icon, child.get('name'))
            
        console.print(table)
        console.print("-" * 50)
        
        if not path:
            console.print("[bold green][F][/bold green] Favori Araçlarımı Göster")
            console.print("[bold green][A][/bold green] Aktif İstihbarat (IP Tarama)")
            console.print("[bold green][T][/bold green] Yeni Hedef Belirle")
            console.print("[bold green][N][/bold green] Hedefe Not Ekle")
            
        console.print("[bold red][0][/bold red] Geri Dön / Çıkış")
        
        choice = Prompt.ask("\n[bold cyan]Seçiminiz[/bold cyan]").strip().upper()
        
        if choice == '0':
            return
        elif choice == 'F' and not path:
            display_favorites()
        elif choice == 'A' and not path:
            active_intelligence()
        elif choice == 'T' and not path:
            target_name = Prompt.ask("[bold yellow]Hedefin adını veya takma adını girin[/bold yellow]")
            console.print(f"[bold green][+] Hedef '{target_name}' olarak ayarlandı. Raporlama aktif.[/bold green]")
            input("\nDevam etmek için ENTER...")
        elif choice == 'N' and not path:
            add_note()
            input("\nDevam etmek için ENTER...")
        else:
            try:
                choice_idx = int(choice)
                if 1 <= choice_idx <= len(children):
                    selected_node = children[choice_idx - 1]
                    new_path = path + [selected_node.get("name")]
                    
                    if "children" not in selected_node and selected_node.get("type") == "url":
                        handle_url_node(selected_node)
                    else:
                        display_menu(selected_node, new_path)
            except ValueError:
                pass
if __name__ == "__main__":
    import pyfiglet
    console.clear()
    ascii_art = pyfiglet.figlet_format("Existanyalist", font="slant")
    console.print(f"[bold magenta]{ascii_art}[/bold magenta]")
    console.print(Panel("[bold cyan]NEXUS-OSINT CORE ENGINE v1.0[/bold cyan]\n[white]Developed by Existanyalist[/white]", style="magenta"))
    console.print("\n")
    load_favorites()
    data_tree = load_data()
    target_opt = Prompt.ask("\n[bold cyan]Bir araştırma hedefi belirlemek ister misiniz? (İsim girin veya boş geçmek için ENTER)[/bold cyan]")
    if target_opt.strip():
        target_name = target_opt.strip()
    
    display_menu(data_tree)
    console.print("\n[bold green][+] Oturum kapatıldı. Raporlarınız ve önbelleğiniz kaydedildi. İyi avlar, Existanyalist![/bold green]")

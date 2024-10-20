import requests
from bs4 import BeautifulSoup
import os

def ascii_sanat():
    print("""
\033[94m  _______________________\033[0m
\033[94m /                        \033[0m
\033[94m|  \033[96mBAXREN SEARCH TERMINAL\033[94m  \033[0m
\033[94m \\_______________________/\033[0m
\033[94m  _______________________\033[0m
\033[94m /                        \033[0m
\033[94m|  \033[96mARA    |  KEŞFET    \033[94m\033[0m
\033[94m \\_______________________/\033[0m
""")

def arama_motoru():
    ascii_sanat()
    arama_kismi = input("\033[96mArama yapın veya site URL'sini girin: \033[0m")

    if arama_kismi.startswith("http"):
        url = arama_kismi
    else:
        url = "https://www.google.com/search?q=" + arama_kismi

    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(response.text, "html.parser")

    sonuçlar = soup.find_all("div", class_="g")
    for i, sonuç in enumerate(sonuçlar):
        print(f"\033[96m{i+1}. {sonuç.find('h3').text}\033[0m")
    seçim = input("\033[96mSeçim yapın (1-{}): \033[0m".format(len(sonuçlar)))
    if seçim.isdigit() and 1 <= int(seçim) <= len(sonuçlar):
        url = sonuçlar[int(seçim)-1].find("a")["href"]
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.text, "html.parser")
        print(soup.get_text())
    else:
        print("\033[91mGeçersiz seçim.\033[0m")

    sayfa_tarihi = []
    sayfa_tarihi.append(soup.get_text())

    while True:
        komut = input("\033[96mKomut girin (h: yardım, q: çıkış, n: önceki sayfa, e: sonraki sayfa, g: git, m: menü): \033[0m")
        if komut == "h":
            print("\033[96mYardım:\033[0m")
            print("\033[96m  h: Yardım\033[0m")
            print("\033[96m  q: Çıkış\033[0m")
            print("\033[96m  n: Önceki sayfa\033[0m")
            print("\033[96m  e: Sonraki sayfa\033[0m")
            print("\033[96m  g: Git\033[0m")
            print("\033[96m  m: Menü\033[0m")
        elif komut == "q":
            break
        elif komut == "n":
            # Önceki sayfa
            if len(sayfa_tarihi) > 1:
                sayfa_tarihi.pop()
                print(sayfa_tarihi[-1])
            else:
                print("\033[91mÖnceki sayfa yok.\033[0m")
        elif komut == "e":
            # Sonraki sayfa
            if "next" in [a.text for a in soup.find_all("a")]:
                next_url = [a for a in soup.find_all("a") if a.text == "Sonraki"][0]["href"]
                response = requests.get(next_url, headers={'User-Agent': 'Mozilla/5.0'})
                soup = BeautifulSoup(response.text, "html.parser")
                sayfa_tarihi.append(soup.get_text())
                print(soup.get_text())
            else:
                print("\033[91mSonraki sayfa yok.\033[0m")
        elif komut == "g":
            # Git
            git_url = input("\033[96mGitmek istediğiniz URL'yi girin: \033[0m")
            response = requests.get(git_url, headers={'User-Agent': 'Mozilla/5.0'})
            soup = BeautifulSoup(response.text, "html.parser")
            sayfa_tarihi.append(soup.get_text())
            print(soup.get_text())
        elif komut == "m":
            # Menü
            print("\033[96mMenü:\033[0m")
            print("\033[96m  h: Yardım\033[0m")
            print("\033[96m  q: Çıkış\033[0m")
            print("\033[96m  n: Önceki sayfa\033[0m")
            print("\033[96m  e: Sonraki sayfa\033[0m")
            print("\033[96m  g: Git\033[0m")
            print("\033[96m  m: Menü\033[0m")
        else:
            print("\033[91mGeçersiz komut.\033[0m")

if __name__ == "__main__":
    arama_motoru()
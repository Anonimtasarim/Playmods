import webbrowser

def yönlendir(mesaj):
    url = f"http://www.{mesaj}.com"
    print(f"{url} adresine yönlendiriliyor...")
    webbrowser.open(url)

while True:
    mesaj = input("Arama yap (çıkmak için 'q' ya bas): ")
    if mesaj.lower() == "q":
        print("Çıkılıyor...")
        break
    yönlendir(mesaj)


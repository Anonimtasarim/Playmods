def toplama(a, b):
    return a + b

def cikarma(a, b):
    return a - b

def carpma(a, b):
    return a * b

def bolme(a, b):
    if b == 0:
        return "Hata: Sıfıra bölme tanımsızdır."
    return a / b

def ust_alma(a, b):
    return a ** b

def hesap_makinesi():
    print("Hesap Makinesi")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("5. Üst Alma")

    while True:
        try:
            secim = int(input("Bir işlem seçin (1/2/3/4/5): "))
            if secim not in [1, 2, 3, 4, 5]:
                print("Geçersiz seçim! Tekrar deneyin.")
                continue

            sayi1 = float(input("Birinci sayıyı girin: "))
            sayi2 = float(input("İkinci sayıyı girin: "))

            if secim == 1:
                print(f"Sonuç: {toplama(sayi1, sayi2)}")
            elif secim == 2:
                print(f"Sonuç: {cikarma(sayi1, sayi2)}")
            elif secim == 3:
                print(f"Sonuç: {carpma(sayi1, sayi2)}")
            elif secim == 4:
                print(f"Sonuç: {bolme(sayi1, sayi2)}")
            elif secim == 5:
                print(f"Sonuç: {ust_alma(sayi1, sayi2)}")
            
            devam = input("Başka bir işlem yapmak ister misiniz? (E/H): ").lower()
            if devam != 'e':
                print("Hesap makinesi kapatılıyor...")
                break

        except ValueError:
            print("Hatalı giriş yaptınız, lütfen sayı girin.")

# Hesap makinesini çalıştır
hesap_makinesi()








        






    


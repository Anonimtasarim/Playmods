 
def carp(*args):
    carpim = 1
    for arg in args:
        carpim *= arg
    return carpim

print("ÜRETİŞİ İFLAS ETMİŞTİR SAYI GİRME GİRECEKSENDE (virgülle ayırı)")
print("LÜFEN 'Çıkış'YAS BİDAHKİNE BU KADAR KİBAR OLMAM!")
while True:
    try:
        # Kullanıcıdan giriş al
        sayilar = input("NEDEN İFLAS ETDİGİNİ SORMA!: ")

        # Eğer kullanıcı 'nasılsın' derse cevap ver
        if sayilar.lower() == "neden iflas etdin":
            print("kardeşim sana sorma demedimi şeytana uyduk tutmadı! hadi sen bir çıkış yas hadi")
            continue
            

        # Eğer kullanıcı çıkmak isterse döngüden çık
        if sayilar.lower() == "çıkış":
            print("Çıkış yaptıgınıs için üretici firma teşekür eder. İyi günler!")
            break

        # Listeye çevir ve sayıları al
        sayi_listesi = [int(x) for x in sayilar.split(",")]

        # Sonucu hesapla ve yazdır
        sonuc = carp(*sayi_listesi)
        print(f"BEN SANA 'Çıkış' Yas demedimi Yeter!: {sonuc}")

    except ValueError:
        print("SANA SAYI GİRME DEMEDİMİ EROR! EROR! EROR! EROR EROR! EROR SENİN YÜSÜNDEN")
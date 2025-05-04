from datetime import datetime
import time
import locale
import random

def gün_sabah():
    sabah = [
        "Hava çok güzel, koşu yapmaya ne dersin?",
        "Bence bugün evde kalıp dinlenmelisin.",
        "Bugün proje geliştirmeye ne dersin?",
        "Dışarı çıkıp hava almaya ne dersin?",
        "Sıkıcı bir hava var, dinlensen iyi olur.",
        "Bence bugün evde kalıp kafanı dinlemelisin.",
        "bugün sabahdan akşama kadar proje geliştirmek için çokel bir gün"
    ]
    return random.choice(sabah)  

def gün_öglen():
    öglen = [
        "Gün ortasına özel bir merhaba! ",
        "Öğlen molası sizin için hazır! ",
        "Günün en enerjik saatine hoş geldiniz! ",
        "Öğlen güneşi gibi parlak bir karşılama! ",
        "Öğlen vakti, yeni fikirler için harika bir zaman! ",
        "Günün yarısını tamamladın, tebrikler! ",
        "Öğlen molanızı dinlenme vakti! ",
        "Gün ortasına özel bir merhaba! ",
        "Öğlen güneşi sizi karşılıyor! "
    ]
    return random.choice(öglen)  

def akşam_mesaj():
    akşam = [
        "Akşam oldu, basit bir proje geliştirip eğlenmelisin bence! ",
        "Gün batımı sizi karşılıyor! ",
        "Akşam vakti, dinlenme zamanı! ",
        "Huzur dolu bir akşam sizi bekliyor! ",
        "Günün yorgunluğunu atmaya hazır mısınız? ",
        "Akşamın keyfini çıkarın! ",
        "Gün batımı eşliğinde hoş geldiniz! ",
        "Akşamın sessizliği sizi bekliyor! ",
        "Günün sonuna geldin, tebrikler! ",
        "Günün yorgunluğunu atmanın tam zamanı! "
        "filimlemenin tam zamanı"
    ]
    return random.choice(akşam)  


def açılış():
    hour = datetime.now().hour
    if 6 <= hour < 12:
        return gün_sabah()
    elif 12 <= hour < 18:
        return gün_öglen()
    else:
        return akşam_mesaj()
  
def gün():
    # Windows türkçe local ayarı 
    locale.setlocale(locale.LC_ALL, 'Turkish_Turkey.1254')
    simdi = datetime.now()  # Şu anki tarih ve saat bilgisini al
    gun_adi = simdi.strftime("%A")  # Tam gün ismi 
    return (f"günleden {gun_adi}")

# Ana program
def main():
    while True:
        print(f"{gün()}, {açılış()}")  
        time.sleep(3600)  

if __name__ == "__main__":
    main()


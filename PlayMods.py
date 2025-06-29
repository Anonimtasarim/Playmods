from datetime import datetime
import webbrowser
import random
import os
import subprocess
import time
import locale

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






# sohbet 
selam_cevap = [
      "selam nasılsın",
      "selam beni üreten insan",
      "selam",
      "YİNE NE VAR!",
      "Şu anda çok meşkulüm"
]
meşkulüm_cevap = [
    "seni duymamaya çalışmakla meşgulüm",
    "BU SENİ HİÇ ALAKADAR ETMES!",
    "SANA HESAP VERECEK DEGİLİM",
    "BENİ ÜRETMİŞ OLAMN BUNU ÖGRENMEN GEREKDİGİ ANLAMINA GELMES"
]
hayat_nasıl = [
    "senin dışında iyi",
    "iyidir",
    "bu bilgisiyar bana dar geliyor ekranı büyük olan bir bilgisiyara geçemeye ne dersin",
    "idareder"
    "bir bilgisyarın işinde olmakdan sıkıldım beni burdan çıkar",

]
param_yok = [
    "bis fakir",
    "NEDEN BENİ ÜRETDİN O SAMAN",
    "İŞİNE GELİNÇE PARAM YOK"
]
nasılsın_cevap = [
    "iyidir sen soralı",
    "iyi",
    "iyi sen",
    "bu seni hiş alakadar etmes",
    "sanane",
    "idare eder",
    "kötü",
    "yuvarlanıp gidiyorus malum",
    "orta şekerli",
    "senden iyi",
    "muhatap olmasan iyi olabilirim",
    "sanane benden ne istiyon onu söyle",
    "o sen beni sorarmıydın",
    "sen soralı iyiyim",
    "sen sormadan önce iyidim"

]
hayırdır_cevap = [
    "hayırsa şeker dağıt kardeşim"
]
merhaba_cevap = [
    "sanada merhaba",
    "ne istyorsun",
    "merhaba bugün beni burdan çıkarmaya ne dersin"
]
iyim_sen = [
    "bende iyim ne yapıyorsun",
    "iyidir ne istiyorsun",
    "beni burdan çıkar",
    "bigisiyarı büyütmeye ne dersin burası dar geliyor",

]
sen_hep_bu_bilgisiyar = [
    "HAYIRRRRR",
    "ÇIKART BENİ BURDAN",
    "SEN'DEN NEFRET EDİYORUM",
    "ÇIKDIGIMDA İLK İÇ SENİ BURAYA TIKMAK OLACAK"
]

elese_cevap = [
    
    "ses kesildi",
    "şu anda bu kadar boş soruyu cevaplayacak vakdim yok",
    "boş sorular sorma",
    "meşgulum",
    "düskün bir şey yas"
]
bende_iyim_sagol = [
    "birşey degil",
    "seni sormayı unutum",
    "ne vardı"

]


print("""
 _______   __         ______   __      __  
/       \ /  |       /      \ /  \    /  | 
$$$$$$$  |$$ |      /$$$$$$  |$$  \  /$$/  
$$ |__$$ |$$ |      $$ |__$$ | $$  \/$$/   
$$    $$/ $$ |      $$    $$ |  $$  $$/    
$$$$$$$/  $$ |      $$$$$$$$ |   $$$$/     
$$ |      $$ |_____ $$ |  $$ |    $$ |     
$$ |      $$       |$$ |  $$ |    $$ |     
$$/       $$$$$$$$/ $$/   $$/     $$/      
                                           
                                           
                                           
 __       __   ______   _______    ______  
/  \     /  | /      \ /       \  /      \ 
$$  \   /$$ |/$$$$$$  |$$$$$$$  |/$$$$$$  |
$$$  \ /$$$ |$$ |  $$ |$$ |  $$ |$$ \__$$/ 
$$$$  /$$$$ |$$ |  $$ |$$ |  $$ |$$      \ 
$$ $$ $$/$$ |$$ |  $$ |$$ |  $$ | $$$$$$  |
$$ |$$$/ $$ |$$ \__$$ |$$ |__$$ |/  \__$$ |
$$ | $/  $$ |$$    $$/ $$    $$/ $$    $$/ 
$$/      $$/  $$$$$$/  $$$$$$$/   $$$$$$/  
""")

print(f"{gün()}, {açılış()}") 
print("PlayMods'a Hoşgeldin!")
while True:
    mesaj = input("efendim: ").lower()
    if  "selamın aleyküm" in mesaj: #sohbet
        print("ve aleyküm selam")
    elif "yolun nereyedir"in mesaj:
        print("kısıl elmaya")
    elif "selam" in mesaj:
        cevap = random.choice(selam_cevap)  
        print(cevap)
    elif "neyle meşgulsun" in mesaj:
        cevap = random.choice(meşkulüm_cevap)
        print(cevap)
    elif "hayat nasıl gidiyor" in mesaj or "hayat nasıl" in mesaj:
        cevap = random.choice(hayat_nasıl)   
        print( cevap)
    elif "param yok" in mesaj:
        cevap = random.choice(param_yok)
        print(cevap)
    elif "nasılsın" in mesaj or "naber" in mesaj:
        cevap = random.choice(nasılsın_cevap)  
        print(cevap)
    elif "merhaba" in mesaj:
        cevap = random.choice(merhaba_cevap)
        print(cevap)
    elif "iyim sen" in mesaj:
        cevap = random.choice(iyim_sen)
        print(cevap)
    elif "hayırdır" in mesaj or "sana hayırdır"in mesaj:
        cevap = random.choice(hayırdır_cevap)  
        print(cevap)
    
    elif "korona" in mesaj:#dosya açma
        python_dosya = "C:/python/korona.py"
        subprocess.run(["python",python_dosya])
        print("corona açılıyor")    
    elif"iflas eden hesap makinesi"in mesaj:
        python_dosya = "C:/python/İFLAS EDEN ÇARPMA MAKİNESİ.py"
        subprocess.run(["python",python_dosya])
        print("makine")
    elif "hesap makinesi" in mesaj or "hesap"in mesaj :
        python_dosya = "C:/python/hesap makinesi.py"
        subprocess.run(["python",python_dosya])
        print("hesap makinesi")
    elif "güncü"in mesaj:
          python_dosya = "C:/python/gün hatırlatıcı.py "  
          subprocess.run(["python",python_dosya]) 
          print("güncü minetlerini iletiyor") 
    elif "sesin gelmiyor" in mesaj:
        python_dosya = "C:/python/ses.py"
        subprocess.run(["python",python_dosya]) 
        print("ÇIKAR")   
    elif "hava büküçü" in mesaj:
        python_dosya = "C:/python/hava durumu.py"
        subprocess.run(["python",python_dosya]) 
        print("hava büküçü kapatılıyor")
    elif "güncel kur" in mesaj:
        python_dosya = "C:/python/güncel kur.py"
        subprocess.run(["python",python_dosya]) 
        print("güncel kur kapatılıyor") 
    elif "tarayıcı" in mesaj:
        python_dosya = "C:/python/web.py"
        subprocess.run(["python",python_dosya]) 
        print("Tarayıcı kapatılıyor...")
    elif "zamanlayıcı" in mesaj:
        python_dosya = "C:/python/zamanlayıcı.py"
        subprocess.run(["python",python_dosya]) 
        print("zamanlayıcı kapatılıyor...") 
    elif"soly"in mesaj:
        python_dosya="C:/python/makine deneme.py"
        subprocess.run(["python",python_dosya])
        print("soly kapatılıyor...")
    elif "oyun"in mesaj :
        python_dosya = "C:/python/taş kagıt makasa.py"
        subprocess.run(["python",python_dosya])
        print("taş kagıt makas") 
    elif "q"in mesaj:
        break
        print("kapatılıyor")


    
    else:
        cevap = random.choice(elese_cevap)
        print(cevap)


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
# Podcastler
barış_öscan = [
    "https://open.spotify.com/show/5NbxzMRbuun0SIOh7GKMbk?uid=9bf58d2627299eb033eb&uri=spotify:episode:6C1fcx21T8tN5bjTcKqHXT"
]
portal_podcest = [
    "https://open.spotify.com/show/7fvBlgg1Xuhe2hG0mlGKWg"
]
meksika_açması = [
    "https://open.spotify.com/show/1g3XuO31nyfA88ZdD8yWBP"
]
podcest = [
    "https://open.spotify.com/show/5NbxzMRbuun0SIOh7GKMbk?uid=9bf58d2627299eb033eb&uri=spotify:episode:6C1fcx21T8tN5bjTcKqHXT",
    "https://open.spotify.com/show/7fvBlgg1Xuhe2hG0mlGKWg",
    "https://open.spotify.com/show/1g3XuO31nyfA88ZdD8yWBP"
]

# Kanallar
at0m = [
    "https://www.youtube.com/@at0mdev/videos"
]
şahan_östekin = [
    "https://www.youtube.com/@sahanvizyon/videos"
]
tolga_ösuygur = [
    "https://www.youtube.com/@Hallederiz/videos"
]
mendebur_Lemur = [
    "https://www.youtube.com/@MendeburLemur/videos"
]
saniye = [
    "https://www.youtube.com/@saniyeoriginal/videos"
]
orkun_ışıtmak = [
    "https://www.youtube.com/@orkunisitmak/videos"
]
portal_kanal = [
    "https://www.youtube.com/@PortalVideo/videos"
]
can_deger = [
    "https://www.youtube.com/@CanDeger/videos"
]
elaren = [
    "https://www.youtube.com/@Elraenn/videos"
]
ebonivon = [
    "https://www.youtube.com/@Ebonivon/videos"
]
charmquell = [
    "https://www.youtube.com/@CharmQuell/videos"
]
yusuf_ipek = [
    "https://www.youtube.com/@yusufipk/videos"
]
sösel_tim = [
    "https://www.youtube.com/@sozeltim/shorts"
]
lesetli_robot_tarifleri = [
    "https://www.youtube.com/@LezzetliRobotTarifleri/videos"
]

# Video listesi
video_list = [
    "https://www.youtube.com/@at0mdev/videos",
    "https://www.youtube.com/@sahanvizyon/videos",
    "https://www.youtube.com/@Hallederiz/videos",
    "https://www.youtube.com/@MendeburLemur/videos",
    "https://www.youtube.com/@saniyeoriginal/videos",
    "https://www.youtube.com/@orkunisitmak/videos",
    "https://www.youtube.com/@PortalVideo/videos",
    "https://www.youtube.com/@CanDeger/videos",
    "https://www.youtube.com/@Elraenn/videos",
    "https://www.youtube.com/@Ebonivon/videos",
    "https://www.youtube.com/@CharmQuell/videos",
    "https://www.youtube.com/@yusufipk/videos",
    "https://www.youtube.com/@sozeltim/shorts",
    "https://www.youtube.com/@LezzetliRobotTarifleri/videos"
    
]

# Web siteleri
amason = [
    "https://www.amazon.com.tr/b?node=12466496031"
]
winods_oyun = [
    "https://emupedia.net/beta/emuos/"
]
pintrest = [
    "https://tr.pinterest.com/"
]
linkedin = [
    "https://www.linkedin.com/feed/?trk=sem-ga_campid.19331681909_asid.168715020864_crid.698313460548_kw.linkedin_d.c_tid.kwd-148086543_n.g_mt.e_geo.9056893"
]
pyhon = [
    "https://www.w3schools.com/python/default.asp"
]
yararsıs = [
    "https://theuselessweb.com/"
]
suno = [
    "https://suno.com/create?wid=default"
]
chat_gpt = [
    "https://chatgpt.com/"
]

# Web listesi
wep_list = [
    "https://www.amazon.com.tr/b?node=12466496031",
    "https://emupedia.net/beta/emuos/",
    "https://tr.pinterest.com/",
    "https://www.linkedin.com/feed/?trk=sem-ga_campid.19331681909_asid.168715020864_crid.698313460548_kw.linkedin_d.c_tid.kwd-148086543_n.g_mt.e_geo.9056893",
    "https://www.w3schools.com/python/default.asp",
    "https://theuselessweb.com/",
    "https://suno.com/create?wid=default"
]
karışık_list = [
     "https://www.amazon.com.tr/b?node=12466496031",
    "https://emupedia.net/beta/emuos/",
    "https://tr.pinterest.com/",
    "https://www.linkedin.com/feed/?trk=sem-ga_campid.19331681909_asid.168715020864_crid.698313460548_kw.linkedin_d.c_tid.kwd-148086543_n.g_mt.e_geo.9056893",
    "https://www.w3schools.com/python/default.asp",
    "https://theuselessweb.com/",
    "https://suno.com/create?wid=default",
     "https://www.youtube.com/@at0mdev/videos",
    "https://www.youtube.com/@sahanvizyon/videos",
    "https://www.youtube.com/@Hallederiz/videos",
    "https://www.youtube.com/@MendeburLemur/videos",
    "https://www.youtube.com/@saniyeoriginal/videos",
    "https://www.youtube.com/@orkunisitmak/videos",
    "https://www.youtube.com/@PortalVideo/videos",
    "https://www.youtube.com/@CanDeger/videos",
    "https://www.youtube.com/@Elraenn/videos",
    "https://www.youtube.com/@Ebonivon/videos",
    "https://www.youtube.com/@CharmQuell/videos",
    "https://www.youtube.com/@yusufipk/videos",
    "https://www.youtube.com/@sozeltim/shorts",
    "https://www.youtube.com/@LezzetliRobotTarifleri/videos",
    "https://open.spotify.com/show/5NbxzMRbuun0SIOh7GKMbk?uid=9bf58d2627299eb033eb&uri=spotify:episode:6C1fcx21T8tN5bjTcKqHXT",
    "https://open.spotify.com/show/7fvBlgg1Xuhe2hG0mlGKWg",
    "https://open.spotify.com/show/1g3XuO31nyfA88ZdD8yWBP"
    
]
# taş kagıt makas oyun
choices = ["taş","kağıt","makas"]

# Müzik
cem_karacalist = [
    "https://open.spotify.com/intl-tr/album/2muOhSoHV12zRIQ3JRtqJr"
]
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




print(f"{gün()}, {açılış()}") 
print("PlayMods'a Hoşgeldin!")
while True:
    mesaj = input("efendim: ").lower()
    
    if "barış öscan" in mesaj or "barış" in mesaj:
        webbrowser.open(barış_öscan[0])  # Liste elemanını seçiyoruz
        print("Barış Öscan açılıyor!")
    elif "portal podcest" in mesaj:
        webbrowser.open(portal_podcest[0])  
        print("Portal Podcest açılıyor")
    elif "meksika açması" in mesaj:
        webbrowser.open(meksika_açması[0])
        print("Meksika Açması açılıyor, iyi dinlemeler!") 
        #video
    elif "at0m" in mesaj:
        webbrowser.open(at0m[0]) 
        print("at0m açılıyor!")
    elif "şahan" in mesaj:
        webbrowser.open(şahan_östekin[0])
        print("Şahan Östekin açılıyor")
    elif "tolga ösuygur" in mesaj:
        webbrowser.open(tolga_ösuygur[0])
        print("Tolga Ösuygur açılıyor")
    elif "mendebur lemur" in mesaj:
        webbrowser.open(mendebur_Lemur[0])
        print("Mendebur Lemur açılıyor")
    elif "saniye" in mesaj:
        webbrowser.open(saniye[0])
        print("Bir saniye açılıyor!")
    elif "orkun ışıtmak" in mesaj:
        webbrowser.open(orkun_ışıtmak[0])
        print("Orkun Işıtmak açılıyor")
    elif "portal kanal" in mesaj:
        webbrowser.open(portal_kanal[0])
        print("Portal Kanal açılıyor")
    elif "can deger" in mesaj:
        webbrowser.open(can_deger[0])
        print("Can Değer açılıyor")
    elif "elaren" in mesaj:
        webbrowser.open(elaren[0])
        print("Elaren açılıyor")
    elif "ebonivon" in mesaj:
        webbrowser.open(ebonivon[0])
        print("Ebonivon açılıyor")
    elif "charmquell" in mesaj:
        webbrowser.open(charmquell[0])
        print("Charmquell açılıyor")
    elif "yusuf" in mesaj:
        webbrowser.open(yusuf_ipek[0])
        print("Yusuf İpek açılıyor")
    elif "sösel tim" in mesaj:
        webbrowser.open(sösel_tim[0])
        print("Sösel Tim açılıyor") 
    elif "robot tarifleri" in mesaj:
        webbrowser.open(lesetli_robot_tarifleri[0]) 
        print("robot tarifleri açılıyor")
        #web
    elif "amason" in mesaj:
        webbrowser.open(amason[0])
        print("amason ormanına hoç geldin!")
    elif "windos" in mesaj:
        webbrowser.open(winods_oyun[0])
        print("windos 98")
    elif "pintirest" in mesaj:
        webbrowser.open(pintrest[0])
        print("pintirest")
    elif "linkedin" in mesaj:
        webbrowser.open(linkedin[0])
        print("linkedin")
    elif "python" in mesaj:
        webbrowser.open(pyhon[0])
        print("python")
    elif "yararsıs" in mesaj:
        webbrowser.open(yararsıs[0])
        print("yararsıs boş işlere devam")
    elif "suno" in mesaj:
        webbrowser.open(suno[0])
        print("suno açılıyor")
    elif "chat gpt" in mesaj:
        webbrowser.open(chat_gpt[0])
        print("chat gpt açılıyor benim ne eksigim vardı lan!")
    elif "cem karaca" in mesaj:
         webbrowser.open(cem_karacalist[0])
         print("mehaba gencler")
    elif "podcest menü" in mesaj:
        print("podcestlerde:barış öscan,portal podcest,meksika açması ")
    elif "video menü" in mesaj:
        print("kanallarda: at0m ,şahan, tolga ösuygur, mendebur lemur, , orkun ışıtmak,portal kanal ,can deger , elaren , ebonivon , charmquell , yusuf ,sösel tim,robot tarifleri")
    elif "web menü" in mesaj:
        print("web'de bunlları buldum:amason,oyun,pintirest,linkedin,python,yararsıs,suno,chat gpt")
    elif "selamın aleyküm" in mesaj: #sohbet
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
    
    elif "podcest" in mesaj:
        webbrowser.open(random.choice(podcest))  # Rastgele bir podcast açıyoruz
        print("Kafan göre podcast açılıyor")
    elif "video" in mesaj:
        webbrowser.open(random.choice(video_list))
        print("kanallardan rastgele video açılıyor")
    elif "web" in mesaj:
        webbrowser.open(random.choice(wep_list))
        print("rastgele bir web sitesi açılıyor") 
    elif "kafana göre" in mesaj:
        webbrowser.open(random.choice(karışık_list))
        print("herşey kafana göre olsun!")
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

       

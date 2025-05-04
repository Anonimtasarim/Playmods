import urllib.request
import json

def hava_durumu():
    try:
        konum = input("Şehir: ").strip()
        # User-Agent header ekleyerek bot engelini aştım
        req = urllib.request.Request(
            f"http://wttr.in/{konum}?format=j1",
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        with urllib.request.urlopen(req) as response:
            data = json.load(response)
            weather = data['current_condition'][0]
            return (
                f"Sıcaklık: {weather['temp_C']}°C\n"
                f"Hissedilen: {weather['FeelsLikeC']}°C\n"
                f"Durum: {weather['weatherDesc'][0]['value']}"
            )
    except Exception as e:
        return f"Weather API error: {str(e)}"

while True:
    print("hava bükücüye hoç geldin")
    print("\n" + hava_durumu())
    if input("Devam? (E/H): ").upper() != 'E':
        break
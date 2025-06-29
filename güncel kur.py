import urllib.request
import json

EXCHANGE_URL = "https://api.exchangerate-api.com/v4/latest/USD"

def get_exchange_rates(currency):
    """Dolar ve Euro kurlarını getirir ve ekrana yazdırır."""
    try:
        with urllib.request.urlopen(EXCHANGE_URL) as response:
            data = json.loads(response.read().decode())
            if currency.lower() == "dolar":
                usd_try = data["rates"].get("TRY", "Veri yok")
                print(f"💵 Dolar: {usd_try} TL")
            elif currency.lower() == "euro":
                eur_try = data["rates"].get("TRY", "Veri yok") / data["rates"].get("EUR", 1)
                print(f"💶 Euro: {eur_try:.2f} TL")
            else:
                print("⚠ Geçersiz seçim! Sadece 'dolar' veya 'euro' girin.")
    except Exception as e:
        print("Hata:", e)


while True:
    print("güncel kur")
    print("\n🔄 Dolar veya Euro kuru görmek için 'dolar' veya 'euro' yazın.")
    print("Çıkmak için 'q' yazın.")

    choice = input("\nSeçiminizi yapın: ").lower()

    if choice == "dolar":
        get_exchange_rates("dolar")
    elif choice == "euro":
        get_exchange_rates("euro")
    elif choice == "q":
        print("🚪 Çıkılıyor...")
        break 
    else:
        print("⚠ Lütfen 'dolar', 'euro' veya 'çıkış' yazın.")






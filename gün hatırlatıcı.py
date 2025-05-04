import datetime
import json
import os

# Kaydedilecek dosyanın adı
filename = 'important_days.json'

# Önemli günlerin yükleneceği sözlük
important_days = {}

# JSON dosyasından önemli günleri yükleme
def load_data():
    global important_days
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            important_days = json.load(file)

# JSON dosyasına önemli günleri kaydetme
def save_data():
    with open(filename, 'w') as file:
        json.dump(important_days, file)

# Kullanıcıdan tarih ve açıklama alarak kaydetme
def add_important_day():
    date_input = input("Önemli günün tarihini (GÜN-AY-YIL) formatında girin: ")
    day_description = input("Bu günün  ne var olduğunu açıklayın: ")
    
    try:
        # Kullanıcı tarafından girilen tarihi datetime formatına dönüştürme
        date = datetime.datetime.strptime(date_input, "%d-%m-%Y").date()
        important_days[str(date)] = day_description
        save_data()
        print(f"{date} tarihi kaydedildi.")
    except ValueError:
        print("Geçersiz tarih formatı. Lütfen GÜN-AY-YIL formatında girin.")

# Bugünün tarihini kontrol edip, önemli bir gün var mı diye kontrol etme
def check_important_day():
    today = datetime.date.today()
    if str(today) in important_days:
        print(f"Bugün {today} ve bu günün önemi: {important_days[str(today)]}")
    else:
        print(f"Bugün önemli bir şey yok.!")

# Ana uygulama döngüsü
def main():
    load_data()  # Uygulama başladığında verileri yükle
    print("GÜNCÜ'YÜ KULANDIGIN İÇİN GÜNÇÜ SANA MİNETDAR")
    while True:
        print("\n1. Önemli gün ekle")
        print("2. Bugün ne önemli gün var?")
        print("3. Çıkış")
        choice = input("Seçiminizi yapın (1/2/3): ")
        
        if choice == '1':
            add_important_day()
        elif choice == '2':
            check_important_day()
        elif choice == '3':
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
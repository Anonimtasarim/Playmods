import random

# Seçenekler
choices = ["taş", "kağıt", "makas"]

while True:
    # Oyuncunun seçimi
    player = input("Taş, Kağıt veya Makas seçin (çıkmak için 'q'): ").lower()
    if player == 'q':
        print("Oyun bitti. Çıkılıyor...")
        break

    if player not in choices:
        print("düsgün oyna.")
        continue

    # Bilgisayarın seçimi
    computer = random.choice(choices)
    print(f"Bilgisayarın seçimi: {computer}")

    # Kazananı belirle
    if player == computer:
        print("Berabere!")
    elif (player == "taş" and computer == "makas") or \
         (player == "kağıt" and computer == "taş") or \
         (player == "makas" and computer == "kağıt"):
        print("Kazandın!")
    else:
        print("kaybedin!")

    print("-------------------")

import random

options = ["حجر", "ورقة", "مقص"]

print("مرحبا بك في لعبة حجر ورقة مقص!")
print("اختر: حجر، ورقة، مقص")

while True:
    user_choice = input("اختيارك: ").strip()
    if user_choice not in options:
        print("اختيار غير صالح. حاول مرة أخرى.")
        continue

    computer_choice = random.choice(options)
    print(f"اختيار الكمبيوتر: {computer_choice}")

    if user_choice == computer_choice:
        print("تعادل!")
    elif (user_choice == "حجر" and computer_choice == "مقص") or \
         (user_choice == "ورقة" and computer_choice == "حجر") or \
         (user_choice == "مقص" and computer_choice == "ورقة"):
        print("فزت! 🎉")
    else:
        print("خسرت 😢")

    play_again = input("هل تريد اللعب مرة أخرى؟ (نعم/لا): ").strip().lower()
    if play_again != "نعم":
        print("شكرا للعب! 👋")
        break

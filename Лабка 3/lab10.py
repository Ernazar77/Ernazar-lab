tg_5 = 0
tg_10 = 0
tg_50 = 0
tg_5 = int(input("5 тг: "))
tg_10 = int(input("10 тг: "))
tg_50 = int(input("50тг: "))

total_amount = (tg_5 * 5) + (tg_10 * 10) + (tg_50 * 50)

if total_amount == 100:
    print("u won")
elif total_amount < 100:
    print("none")
else:
    print("none")
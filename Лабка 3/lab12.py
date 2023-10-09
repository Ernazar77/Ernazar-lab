price = 99

quantity = int(input("Введите количество приобретенных пакетов: "))

sale = 0

if quantity >= 10 and quantity <= 19:
    sale = 10
elif quantity >= 20 and quantity <= 49:
    sale = 20
elif quantity >= 50 and quantity <= 99:
    sale = 30
elif quantity >= 100:
    sale = 40

total = quantity * price * (1 - sale / 100)

print(f"Вы получили скидку {sale}%.")
print(f"Общая стоимость покупки: ${total:.2f}")





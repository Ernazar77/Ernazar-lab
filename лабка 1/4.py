n = 5
sum = 0
tax = 0
while n > 0:
    price = input("Введите цену товара: ")
    n -= 1
    sum += int(price)
    tax = float(sum) * 0.07
    print("Цена товаров: ", sum, "Пошлина: ", tax)

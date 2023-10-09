total = float(input("Прошу пользователя ввести величину покупки: "))
taxF = total*0.05
taxL = total*0.025
tax = taxF+taxL
s = total+tax
print("Федеральный налог: ", taxF, "\nРегиональный налог: ", taxL, "\nОбщий налог:", tax, "\nОбщая сумма продажи: ",s)
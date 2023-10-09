food = float(input("Введите стоимость еды: "))
tip = food * 0.18
tax = food * 0.07
total = food+tip+tax
print("Чаевые: ", tip, "\nПошлина: ", tax, "\nВ общем: ", total)

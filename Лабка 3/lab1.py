day_number = int(input("Пищиц): "))

if day_number == 1:
    day_name = "пон"
elif day_number == 2:
    day_name = "вт"
elif day_number == 3:
    day_name = "ср"
elif day_number == 4:
    day_name = "чт"
elif day_number == 5:
    day_name = "пт"
elif day_number == 6:
    day_name = "сб"
elif day_number == 7:
    day_name = "вск"
else:
    day_name = " нету такого дня"

print(f"День номер {day_number} - это {day_name}.")





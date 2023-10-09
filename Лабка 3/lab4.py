prosto_chislo = int(input("ПИШИ:"))

if prosto_chislo == 1:
    rim = "I"
elif prosto_chislo == 2:
    rim = "II"
elif prosto_chislo == 3:
    rim = "III"
elif prosto_chislo == 4:
    rim = "IV"
elif prosto_chislo == 5:
    rim = "V"
elif prosto_chislo == 6:
    rim = "VI"
elif prosto_chislo == 7:
    rim = "VII"
elif prosto_chislo == 8:
    rim = "VIII"
elif prosto_chislo == 9:
    rim = "IX"
elif prosto_chislo == 10:
    rim = "X"
else:
    rim = "piwi ot 1 do 10"

print(f"Твое число{prosto_chislo} - это {rim}")
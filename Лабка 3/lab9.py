number = int(input("Ведите число (0-36): "))

if 0 <= number <= 36:
    if number == 0:
        color = "green"
    elif 1 <= number <= 10:
        color = "red" if number % 2 == 0 else "black"
    elif 11 <= number <= 18:
        color = "black" if number % 2 == 0 else "red"
    elif 19 <= number <= 28:
        color = "red" if number % 2 == 0 else "black"
    elif 29 <=number <= 36:
        color = "black" if number % 2 == 0 else "red"
else:
    color = "undefinde"

if color == "undefinde color":
    print("pls write a number 0-36")
else:
    print(f"{number} sc {color} color.")
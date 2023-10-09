def feet_to_inches(feet):
    inches = feet * 12
    return inches

def main():
    feet = float(input("Введите количество футов: "))
    inches = feet_to_inches(feet)
    print(f"{feet} футов равно {inches} дюймам")

if __name__ == "__main__":
    main()
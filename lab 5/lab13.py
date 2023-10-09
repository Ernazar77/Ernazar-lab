def max(a, b):
    return a if a > b else b

def main():
    num1 = int(input("Введите первое целочисленное значение: "))
    num2 = int(input("Введите второе целочисленное значение: "))
    result = max(num1, num2)
    print(result)

if __name__ == "__main__":
    main()
import random

def math_test():
    num1 = random.randint(1, 1000)
    num2 = random.randint(1, 1000)
    correct_answer = num1 + num2
    user_answer = int(input(f"{num1}\n+ {num2}\nВведите ответ: "))
    if user_answer == correct_answer:
        print("Поздравляем, ответ верный!")
    else:
        print(f"Неправильно. Правильный ответ: {correct_answer}")

def main():
    while True:
        math_test()
        another_test = input("Хотите провести еще один тест? (да/нет): ")
        if another_test.lower() != 'да':
            break

if __name__ == "__main__":
    main()
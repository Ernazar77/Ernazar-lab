def calculate_calories_from_fat(fat_grams):
    calories_from_fat = fat_grams * 9
    return calories_from_fat

def calculate_calories_from_carbs(carb_grams):
    calories_from_carbs = carb_grams * 4
    return calories_from_carbs

def main():
    fat_grams = float(input("Введите количество граммов жиров: "))
    carb_grams = float(input("Введите количество граммов углеводов: "))

    calories_from_fat = calculate_calories_from_fat(fat_grams)
    calories_from_carbs = calculate_calories_from_carbs(carb_grams)

    print(f"Калории от жиров: {calories_from_fat} калорий")
    print(f"Калории от углеводов: {calories_from_carbs} калорий")

if __name__ == "__main__":
    main()
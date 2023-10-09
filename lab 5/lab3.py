def calculate_insurance_coverage(building_value):
    min_coverage = building_value * 0.8
    return min_coverage


def main():
    building_value = float(input("Введите стоимость строения: "))


    min_coverage = calculate_insurance_coverage(building_value)


    print(f"Минимальная страховая сумма: {min_coverage} долларов")

if __name__ == "__main__":
    main()
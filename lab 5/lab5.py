def calculate_property_tax(actual_value):
    assessment_value = actual_value * 0.6
    tax_rate = 0.72
    property_tax = (assessment_value / 100) * tax_rate
    return assessment_value, property_tax


def main():
    actual_value = float(input("Введите фактическую стоимость недвижимого имущества: "))

    assessment_value, property_tax = calculate_property_tax(actual_value)


    print(f"Оценочная стоимость недвижимого имущества: {assessment_value:.2f} долларов")
    print(f"Налог на имущество: {property_tax:.2f} долларов")

if __name__ == "__main__":
    main()
def calculate_hours(area):
    hours_per_sqm = 8
    hours = (area / 10) * hours_per_sqm
    return hours


def main():
    wall_area = float(input("Введите площадь "))
    paint_price_per_can = float(input("Введите цену  "))

    paint_cans = calculate_paint_cans(wall_area)
    hours = calculate_hours(wall_area)
    paint_cost = paint_cans * paint_price_per_can
    labor_cost = hours * 2000
    total_cost = paint_cost + labor_cost

    print(f"Количество требующихся емкостей краски: {paint_cans:.2f} емкостей")
    print(f"Количество требующихся рабочих часов: {hours:.2f} часов")
    print(f"Стоимость краски: {paint_cost:.2f} тенге")
    print(f"Стоимость работы: {labor_cost:.2f} тенге")
    print(f"Общая стоимость малярных работ: {total_cost:.2f} тенге")

if __name__ == "__main__":
    main()
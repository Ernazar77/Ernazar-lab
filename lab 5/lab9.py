def calculate_municipal_tax(sales):
    municipal_tax_rate = 0.025
    municipal_tax = sales * municipal_tax_rate
    return municipal_tax


def calculate_federal_tax(sales):
    federal_tax_rate = 0.05
    federal_tax = sales * federal_tax_rate
    return federal_tax


def main():
    sales = float(input("Введите общий объем продаж за месяц: "))

    municipal_tax = calculate_municipal_tax(sales)

    federal_tax = calculate_federal_tax(sales)

    total_tax = municipal_tax + federal_tax

    print(f"Сумма муниципального налога с продаж: {municipal_tax:.2f} долларов")
    print(f"Сумма федерального налога с продаж: {federal_tax:.2f} долларов")
    print(f"Общий налог с продаж: {total_tax:.2f} долларов")

if __name__ == "__main__":
    main()

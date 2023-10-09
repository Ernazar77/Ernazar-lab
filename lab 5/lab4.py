def calculate_annual_cost(monthly_cost):
    return monthly_cost * 12

def main():
    loan_payment = float(input("Введите платеж по кредиту в месяц: "))
    insurance = float(input("Введите расходы на страховку в месяц: "))
    gasoline = float(input("Введите расходы на бензин в месяц: "))
    oil = float(input("Введите расходы на машинное масло в месяц: "))
    tires = float(input("Введите расходы на шины в месяц: "))
    maintenance = float(input("Введите расходы на техобслуживание в месяц: "))


    total_monthly_cost = (
        loan_payment + insurance + gasoline + oil + tires + maintenance
    )


    total_annual_cost = calculate_annual_cost(total_monthly_cost)


    print(f"Общая месячная стоимость: {total_monthly_cost} долларов")
    print(f"Общая годовая стоимость: {total_annual_cost} долларов")

if __name__ == "__main__":
    main()
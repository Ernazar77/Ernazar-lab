def calculate_total_income(ticket_count_A, ticket_count_B, ticket_count_C):
    ticket_price_A = 20
    ticket_price_B = 15
    ticket_price_C = 10
    total_income = (ticket_count_A * ticket_price_A) + (ticket_count_B * ticket_price_B) + (ticket_count_C * ticket_price_C)
    return total_income

def main():
    ticket_count_A = int(input("Введите количество билетов класса A: "))
    ticket_count_B = int(input("Введите количество билетов класса B: "))
    ticket_count_C = int(input("Введите количество билетов класса C: "))

    total_income = calculate_total_income(ticket_count_A, ticket_count_B, ticket_count_C)

    print(f"Сумма дохода от продажи билетов: {total_income} долларов")

if __name__ == "__main__":
    main()
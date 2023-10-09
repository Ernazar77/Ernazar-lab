
def federal_tax(purchase_amount):
    federal_rate = 0.05  # 5%
    return purchase_amount * federal_rate

def regional_tax(purchase_amount):
    regional_rate = 0.025  # 2.5%
    return purchase_amount * regional_rate

def main():

    purchase_amount = float(input("Введите сумму покупки: "))


    federal = federal_tax(purchase_amount)
    regional = regional_tax(purchase_amount)


    total_tax = federal + regional
    total_payment = purchase_amount + total_tax


    print(f"Федеральный налог: {federal} ")
    print(f"Региональный налог: {regional} ")
    print(f"Общий налог: {total_tax} ")
    print(f"Итоговая сумма к оплате: {total_payment} ")

if __name__ == "__main__":
    main()
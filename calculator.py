go= 'f'
while go == 'f' :
    number_1=float(input("Введіть перше число: "))
    oper = input("Введіть операцію(+,-,*,/): ")
    number_2=float(input("Введіть друге число:"))
    if oper == "+" :
        print(number_1 + number_2)
    if oper == "*" :
        print(number_1 * number_2) 
    if oper == "-" :
        print(number_1 - number_2)
    if oper == "/" :
        print(number_1 / number_2)
    go = input("Натисніть 'f' щоб продовжити ")

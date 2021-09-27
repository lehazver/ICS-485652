print("Генератор рандомного числа")
onemoreattemp = "f"
while onemoreattemp == "f":
    numbers = [1,4,5,6,2,3,10,9,8,7] * 4
    import random
    random.shuffle(numbers)
    start = input("Натисніть enter щоб почати")
    current = numbers.pop()
    print("Ви отримали число %d" %current) 
    onemoreattemp = input("Натисніть 'f' щоб спробувати ще раз")

N = int(input("Введите количество чисел из ряда Фибоначчи: "))
K = int(input("Введите порядковый номер в ряду Фибоначчи, с которого нужно начать: "))


if K < 1 or N < 1:
    print("Числа должны быть > 0")
else:
    a, b = 0, 1
    sum_fib = 0
    
    for i in range(1, K + N):
        if i >= K:
            sum_fib += a
        a, b = b, a + b 
    
    print(f"Сумма {N} чисел Фибоначчи, начиная с {K}-го: {sum_fib}")
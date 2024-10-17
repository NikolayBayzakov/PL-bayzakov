n = int(input("Введите число: "))
i = 1 

while True:
    sqrt = i * i  
    if sqrt > n:
        break
    print(sqrt)
    i += 1


# for i in  range(10):
#     i = i ** 2
#     print(i)
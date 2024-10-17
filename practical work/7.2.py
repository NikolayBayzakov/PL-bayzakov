from random import randint
#вариант 10

lst = [randint(1, 40) for x in range(15)]
print('Первоначальный список:', lst)

new_lst = [0 if x < 10 else 1 if x > 20 else x for x in lst]
print('Измененный список:', new_lst)




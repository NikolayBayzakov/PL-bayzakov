from random import randint
#вариант 10

lst = [randint(10, 80) for x in range(10)]
print('Сгенерированный список', lst)

unique_lst = set(lst)

if len(lst) != unique_lst:
    duplicate = set([i for i in unique_lst if lst.count(i) > 1])
    if len(duplicate) >= 1:
        print('Повторяющийся элемент: ', duplicate)
    else:
        print('В списке нет повторяющихся элементов')




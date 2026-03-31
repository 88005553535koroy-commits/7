my_list = [1, 2, 3, 2, 4, 5, 3]
repeated = []
for i in my_list:
    if my_list.count(i) > 1 and i not in repeated:
        repeated.append(i)
print("Повторяющиеся элементы:", repeated)
#2.	Задайте последовательность чисел. Напишите программу, 
#которая выведет список неповторяющихся элементов исходной последовательности.

num_list = [1,2,3,3,3,4,5,6,6,7,8,9,9,10]
new_list = []
for i in num_list:
    total = 0
    for j in num_list:
        if i == j:
            total+=1
    if total == 1:
        new_list.append(i)
print(new_list)

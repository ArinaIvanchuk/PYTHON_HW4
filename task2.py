#1.	Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N

n = int(input('input number: '))
i=1
for i in range(1, n+1):
    if n%i == 0:
        print(i, end=' ')
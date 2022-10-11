# 1.	Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
import numbers
import re
import itertools


file1 = 'Polynomial.txt'
file2 = 'Polynomial2.txt'
file_sum = 'Sum_poly.txt'

# Получение данных из файла

def read_polynom(file):
    with open(str(file), 'r') as data:
        poly = data.read()
    return poly

# Получение списка кортежей каждого (<коэффициент>, <степень>)

def convert_pol(pol):
    poly = pol.replace('= 0', '')
    poly = re.sub("[*|^| ]", " ", poly).split('+')
    poly = [char.split(' ') for char in poly]
    poly = [[x for x in list if x] for list in poly]
    for i in poly:
        if i[0] == 'x': i.insert(0, 1)
        if i[-1] == 'x': i.append(1)
        if len(i) == 1: i.append(0)
    poly = [tuple(int(x) for x in j if x != 'x') for j in poly]
    return poly

# Получение списка кортежей суммы (<коэф1 + коэф2>, <степень>)

def decompose_pols(poly_1, poly_2):   
    x = [0] * (max(poly_1[0][1], poly_2[0][1] + 1))
    for i in poly_1 + poly_2:        
        x[i[1]] += i[0]
    res = [(x[i], i) for i in range(len(x)) if x[i] != 0]
    res.sort(key = lambda r: r[1], reverse = True)
    return res

# Составление итогового многочлена

def get_sum_pol(pol):
    var = ['*x^'] * len(pol)
    numbers = [x[0] for x in pol]
    degrees = [x[1] for x in pol]
    new_poly = [[str(a), str(b), str(c)] for a, b, c in (zip(numbers, var, degrees))]
    for x in new_poly:
        if x[0] == '0': del (x[0])
        if x[-1] == '0': del (x[-1], x[-1])
        if len(x) > 1 and x[0] == '1' and x[1] == '*x^': del (x[0], x[0][0])
        if len(x) > 1 and x[-1] == '1': 
            del x[-1]
            x[-1] = '*x'
        x.append(' + ')
    new_poly = list(itertools.chain(*new_poly))
    new_poly[-1] = ' = 0'
    return "".join(map(str, new_poly))

def write_to_file(file, pol):
    with open(file, 'w') as data:
        data.write(pol)

polynom_1 = read_polynom(file1)
polynom_2 = read_polynom(file2)
pol_1 = convert_pol(polynom_1)
pol_2 = convert_pol(polynom_2)

pol_sum = get_sum_pol(decompose_pols(pol_1, pol_2))
write_to_file(file_sum, pol_sum)

print(polynom_1)
print(polynom_2)
print(pol_sum)
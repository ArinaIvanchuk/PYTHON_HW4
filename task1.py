#1.	Вычислить число c заданной точностью d
#Пример:
#- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
def round_num(num, dig):
    a = int((10**dig) * num)
    num = a/(10**dig)
    return num
print(round_num(float(input('input real number: ')), int(input('input remains digit: '))))
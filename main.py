print('введите 1й 2й и 3й коэффиценты квадратного уравнения')
a, b, c = float(input()), float(input()), float(input())
if b**2 - 4*a*c == 0:
    print('x =', (-b)/(2*a))
elif b**2 - 4*a*c > 0:
    print('x1 =', (-(b) + (b**2 - 4*a*c)**0.5)/(2*a), 'x2 =', (-(b) - (b**2 - 4*a*c)**0.5)/(2*a))
else:
    print('Нет корней')

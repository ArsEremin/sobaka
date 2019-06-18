a = int(input())
b = int(input())
c = int(input())
D = b ** 2 - 4 * a * c
if D > 0:
    x1 = (-b + D ** 0.5)/(2 * a)
    x2 = (-b - D ** 0.5)/(2 * a)
    print(x1,x2,sep = '\n')
if D == 0:
    x = (-b)/(2 * a)
    print(x)
if D<0:
    print('Нет корней')

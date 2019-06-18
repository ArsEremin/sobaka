n = int(input())
if i > 1:
    for i in range(2,n):
        if (n % i) == 0:
            print('Непростое')
            break
    else:
        print('Простое')

x = int(input())
y = int(input())
for i in range(x, y):
    if i > 1:
        for n in range(2, i):
            if (i % n) == 0:
                break
        else:
            print(i)

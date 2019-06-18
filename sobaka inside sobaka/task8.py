N = int(input())
P = int(input())
s = []
for i in range(N,P):
    if i % 2 != 0:
        s.append(i**3)
        s.sort(reverse=True)
print(s)

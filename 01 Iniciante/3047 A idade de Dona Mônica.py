n = int(input())
n1 = int(input())
n2 = int(input())
n3 = n - (n1+n2)
if n1 > n2 and n1 > n3:
    print(n1)
elif n2 > n1 and n2 > n3:
    print(n2)
else:
    print(n3)
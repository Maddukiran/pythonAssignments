def fibo(n):
    if n<=1:
        return n
    return fibo(n-1) + fibo(n-2)

x = 9

for i in range(x):
    print(fibo(i), end=' ')
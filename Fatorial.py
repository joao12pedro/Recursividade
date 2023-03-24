def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        mult = 1
        mult =  n * fatorial(n-1)
        return mult

result = fatorial(5)
print(result)
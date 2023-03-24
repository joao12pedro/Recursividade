def maior(L):
    if len(L) == 1:
        return L[0]
    else:
        return max(L[0], maior(L[1:]))

lista = [7,4]
result = maior(lista)
print(result)
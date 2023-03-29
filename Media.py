def media(L):
    if len(L) == 1:
        return L[0]
    else:
        return (L[0] + media(L[1:]) * (len(L)-1)) / len(L)

    
lista = [20,2]
print(media(lista))
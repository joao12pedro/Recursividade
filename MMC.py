def mmc(X, Y):
    # Encontra o maior número entre a e b
    if X > Y:
        maior = X
    else:
        maior = Y


    # Verifica se o maior número é um múltiplo de a e b
    if maior % X == 0 and maior % Y == 0:
        return maior
    else:
       maior += 1

result = mmc(3,9)
print(result)

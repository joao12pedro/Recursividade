def soma(n):
    cont = 0
    i = 0
    num = str(n)
    if len(num) == 1:
        return n
    else:
        ultimo_digito = n % 10
        resto_do_numero = n // 10
        return ultimo_digito + soma(resto_do_numero)


result = soma(1234)
print(result)

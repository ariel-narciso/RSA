def isPrimo(n):
    if (n != 2) and (n % 2 == 0):
        return(False)
    elif n % 2 != 0:
        aux = (n ** 0.5) // 1
        while aux > 1:
            if n % aux == 0:
                return(False)
            aux -= 1
    return(True)

def listaDivisores(n):
    aux = (n ** 0.5) // 1
    divisores = []
    i = 1
    while i <= aux:
        if n % i == 0:
            divisores.append(i)
        i += 1

    tam = len(divisores)
    if divisores[tam - 1] ** 2 == n:
        i = tam - 2
    else:
        i = tam -1
    while i >= 0:
        divisores.append(n // divisores[i])
        i -= 1

    return(divisores)
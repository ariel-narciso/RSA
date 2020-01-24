from RSA import *

# exemplo de uso

texto = RSA(47, 53, list(range(25)))
texto.encriptar()
print(texto)
texto.decriptar()
print(texto)

# as validações já ocorrem internamente

# resta saber se a entrada e saida do programa
# pode ser uma lista de inteiros
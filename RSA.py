class RSA:

    """
    A transformacao eh aplicada a cada caracter
    da string
    Nao eh garantido que apos a transformacao os novos
    caracteres sejam imprimiveis
    """

    def __init__(self, p, q, mensagem):
        self.__p = p
        self.__q = q
        self.__n = p * q # verificar se cada inteiro dentro da mensagem eh inferior ou igual a n
        self.__z = (p - 1) * (q - 1)
        self.__e = self.candidatos(self.__z)[0] # Eh garantido que a lista nunca estará vazia?
        # tem que achar d pra decriptar
        self.__mensagem = mensagem

    def ehPrimo(n):
        pass

    def candidatos(self, n):
        return [item for item in range(2, n) if self.mdc(item, n) == 1]
    
    def mdc(self, a, b):
        if b == 0:
            return a
        return self.mdc(b, a % b)

    def encriptar(self):
        mensagem = ""
        for c in self.__mensagem:
            mensagem += chr((ord(c)) ** self.__e % self.__n)
        self.__mensagem = mensagem
    
    def decriptar(self):
        pass
    
    def __str__(self):
        return self.__mensagem

t = RSA(5, 7, "RSA")
t.encriptar()
print(t)
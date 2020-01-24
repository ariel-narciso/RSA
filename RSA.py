def primo(n):
	if n in [2,3,5,7]:
		return True
	if n % 2 == 0:
		return False
	i = 3
	while i * i <= n:
		if n % i == 0:
			return False
		i += 2
	return True

def mdc(a, b):
	if b == 0:
		return a
	return mdc(b, a % b)

class RSA:

	"""
	Caso os argumentos passados não respeitem as regras
	do método RSA, valores-padrão são adotados
	(p = 3, q = 5 e mensagem = [0])
	"""
	def __init__(self, p, q, mensagem, enc = False):
		self.__p = p
		self.__q = q
		self.__n = p * q
		if not self.validarPQ(): # devem respeitar os limites minimos, serem primos e distintos
			self.__p = 3
			self.__q = 5
			self.__n = 15
		self.__mensagem = mensagem
		if not self.validarMensagem(): # cada inteiro da mensagem deve ser menor que p * q
			self.__mensagem = [0]
		self.__enc = enc # se a mensagem está ou não criptografada
		self.setZED()
	
	"""
	Modifica as demais variáveis em funcão de p e q
	"""
	def setZED(self):
		self.__z = (self.__p - 1) * (self.__q - 1)
		self.__e = 2
		while self.__e < self.__z and mdc(self.__z, self.__e) > 1: # Da pra fazer melhor?
			self.__e += 1
		self.__d = 1
		while self.__d * self.__e % self.__z != 1 or self.__d == self.__e: # Da pra fazer melhor?
			self.__d += 1

	"""
	Modifica o par de inteiros primos p e q
	Retorna True se de fato modificou ou
	False caso contrário, indicando que os
	novos inteiros não são válidos
	"""
	def setPQ(self, p, q):
		a = self.__p
		b = self.__q
		self.__p = p
		self.__q = q
		self.__n = p * q
		if not self.validarPQ() or not self.validarMensagem():
			self.__p = a
			self.__q = b
			self.__n = a * b
			return False
		self.setZED()
		return True
	
	def getPQ(self):
		return [self.__p, self.__q]
	
	def getN(self):
		return self.__n
	
	def getEnc(self):
		return self.__enc
	
	def getZ(self):
		return self.__z
	
	def getE(self):
		return self.__e
	
	def getD(self):
		return self.__d
	
	"""
	Modifica o texto
	Retorna True se modificou
	ou False caso contrário,
	indicando que o novo texto
	não é válido
	"""
	def setMensagem(self, mensagem):
		temp = self.__mensagem
		self.__mensagem = mensagem
		if not self.validarMensagem():
			self.__mensagem = temp
			return False
		return True

	def validarPQ(self):
		if self.__p + self.__q < 6 or self.__p == self.__q:
			"""
			Se a soma for menor que 6,
			'z' será muito pequeno e não
			haverá candidatos para 'e'.
			Alem disso, se os inteiros são iguais,
			a mensagem original é perdida depois de
			criptografada, ou seja, mesmo escolhendo um
			'd' válido, ao aplicar a fórmula, a mensagem
			pode não voltar a sua versão original
			"""
			return False
		if not primo(self.__p) or not primo(self.__q):
			return False
		return True

	def validarMensagem(self):
		for x in self.__mensagem:
			if x >= self.__n:
				return False
		return True

	"""
	Cifra a mensagem caso ela não esteja cifrada
	Retorna True se foi encriptada ou False
	caso contrário
	"""
	def encriptar(self):
		if not self.__enc:
			for n in range(len(self.__mensagem)):
				self.__mensagem[n] = self.__mensagem[n] ** self.__e % self.__n
			self.__enc = True
			return True
		return False
	
	"""
	Decifra a mensagem caso ela não esteja decifrada
	Retorna True se foi decriptada ou False
	caso contrário
	"""
	def decriptar(self):
		if self.__enc:
			for n in range(len(self.__mensagem)):
				self.__mensagem[n] = self.__mensagem[n] ** self.__d % self.__n
			self.__enc = False
			return True
		return False
	
	def __str__(self):
		return str(self.__mensagem)

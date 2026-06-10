import random

class Perceptron:
	def __init__(self, amostras, saidas, taxa_aprendizado=0.1, geracoes=1000, limiar=1):
		self.amostras = amostras
		self.saidas = saidas
		self.taxa_aprendizado = taxa_aprendizado
		self.geracoes = geracoes
		self.limiar = limiar
		self.n_amostras = len(amostras)
		self.n_atributos = len(amostras[0])
		self.pesos = []

	def treinar(self):
		for amostra in self.amostras:
			amostra.insert(0, self.limiar)
		for i in range(self.n_atributos):
			self.pesos.append(random.random())
		self.pesos.insert(0, self.limiar)
		geracoes = 0
		while True:
			aprendeu = True
			for i in range(self.n_amostras):
				soma = 0
				for j in range(self.n_atributos + 1):
					soma += self.pesos[j] * self.amostras[i][j]
				saida_gerada = self.funcao_ativacao_signal(soma)
				if saida_gerada != self.saidas[i]:
					erro = self.saidas[i] - saida_gerada
					for j in range(self.n_atributos + 1):
						self.pesos[j] = self.pesos[j] + self.taxa_aprendizado * erro * self.amostras[i][j]
					aprendeu = False
			geracoes += 1
			if aprendeu or geracoes > self.geracoes:
				print('Quantidade de gerações para aprender: %d\n' % geracoes)
				break

	def teste(self, amostra):
		amostra.insert(0, self.limiar)
		soma = 0
		for i in range(self.n_atributos + 1):
			soma += self.pesos[i] * amostra[i]
		saida_gerada = self.funcao_ativacao_signal(soma)

		if saida_gerada == 1:
			print('Classe: %d. Chuva' % saida_gerada)
		else:
			print('Classe: %d. Sol' % saida_gerada)

	def funcao_ativacao_signal(self, soma):
		if soma >= 0:
			return 1
		return -1

# Amostras: [Umidade, Pressão] (Valores normalizados entre 0 e 1)
amostras = [
	[0.20, 0.90],  # Ar seco, pressão alta -> Sol
	[0.35, 0.85],  # Ar seco, pressão alta -> Sol
	[0.15, 0.75],  # Muito seco, pressão média -> Sol
	[0.40, 0.80],  # Umidade média, pressão alta -> Sol
	[0.55, 0.45],  # Umidade média, pressão baixa -> Chuva
	[0.85, 0.30],  # Muito úmido, pressão baixa -> Chuva
	[0.90, 0.20],  # Muito úmido, pressão muito baixa -> Chuva
	[0.75, 0.35]   # Úmido, pressão baixa -> Chuva
]

# Saídas: -1 = Não Chove (Sol) | 1 = Chove
saidas = [-1, -1, -1, -1, 1, 1, 1, 1]

rede = Perceptron(amostras, saidas)
rede.treinar()

while True:
	umidade = float(input('Umidade normalizada (0 a 1): '))
	pressao = float(input('Pressão normalizada (0 a 1): '))
	print('Entrada: Umidade =', umidade, ', Pressão =', pressao)
	rede.teste([umidade, pressao])

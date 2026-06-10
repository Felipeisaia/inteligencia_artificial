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
			print('Classe: %d. Crédito Aprovado' % saida_gerada)
		else:
			print('Classe: %d. Crédito Recusado' % saida_gerada)

	def funcao_ativacao_signal(self, soma):
		if soma >= 0:
			return 1
		return -1

# Amostras: [Histórico de Crédito, Renda Mensal] (Normalizados de 0 a 1)
amostras = [
	[0.10, 0.20],  # Histórico ruim, renda baixa -> Recusado
	[0.25, 0.30],  # Histórico ruim, renda média-baixa -> Recusado
	[0.40, 0.15],  # Histórico médio, renda muito baixa -> Recusado
	[0.20, 0.50],  # Histórico ruim, renda média -> Recusado
	[0.70, 0.65],  # Histórico bom, renda média-alta -> Aprovado
	[0.90, 0.80],  # Histórico excelente, renda alta -> Aprovado
	[0.60, 0.90],  # Histórico bom, renda muito alta -> Aprovado
	[0.85, 0.55]   # Histórico excelente, renda média -> Aprovado
]

# Saídas: -1 = Alto Risco (Recusado) | 1 = Baixo Risco (Aprovado)
saidas = [-1, -1, -1, -1, 1, 1, 1, 1]

rede = Perceptron(amostras, saidas)
rede.treinar()

while True:
	historico = float(input('Histórico de crédito normalizado (0 a 1): '))
	renda = float(input('Renda mensal normalizada (0 a 1): '))
	print('Entrada: Histórico =', historico, ', Renda =', renda)
	rede.teste([historico, renda])

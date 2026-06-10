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
                print("Quantidade de gerações para aprender:", geracoes)
                break

    def teste(self, amostra):

        amostra.insert(0, self.limiar)

        soma = 0

        for i in range(self.n_atributos + 1):
            soma += self.pesos[i] * amostra[i]

        saida_gerada = self.funcao_ativacao_signal(soma)

        if saida_gerada == 1:
            print("Classe: 1 - Cliente Confiável (Aprovado)")
        else:
            print("Classe: -1 - Cliente de Risco (Recusado)")

    def funcao_ativacao_signal(self, soma):
        if soma >= 0:
            return 1
        return -1


# [Histórico de Crédito, Renda Mensal]
amostras = [
    [0.10, 0.20],
    [0.25, 0.30],
    [0.40, 0.15],
    [0.20, 0.50],
    [0.70, 0.65],
    [0.90, 0.80],
    [0.60, 0.90],
    [0.85, 0.55]
]

# -1 = Recusado | 1 = Aprovado
saidas = [-1, -1, -1, -1, 1, 1, 1, 1]

rede = Perceptron(amostras, saidas)
rede.treinar()

while True:

    historico = float(input("Histórico de crédito (0 a 1): "))
    renda = float(input("Renda mensal (0 a 1): "))

    rede.teste([historico, renda])
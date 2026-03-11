from itertools import combinations

tempos = {'aluno': 1, 'professora': 2, 'zelador': 5, 'cientista': 10}

# 1. ESTADOS
class Estado:
    def __init__(self, origem, destino, lanterna, tempo):
        self.origem = set(origem)
        self.destino = set(destino)
        self.lanterna = lanterna
        self.tempo = tempo

# 5. FUNÇÃO OBJETIVO
def eh_objetivo(estado):
    return len(estado.origem) == 0 and estado.lanterna == 1 and estado.tempo <= 17

# 4. VISITADOS (Controle de Loops)
visitados = {}

def deve_explorar(estado):
    configuracao = (frozenset(estado.origem), frozenset(estado.destino), estado.lanterna)
    
    if configuracao not in visitados or estado.tempo < visitados[configuracao]:
        visitados[configuracao] = estado.tempo
        return True
    return False

# 2. REGRAS DE TRANSIÇÃO e 3. RESTRIÇÕES
def gerar_proximos_estados(estado):
    proximos_estados = []
    
    lado_atual = estado.origem if estado.lanterna == 0 else estado.destino
    
    # Restrição 1: Capacidade (1 a 2 pessoas) e Restrição 2: Posse da lanterna
    grupos_possiveis = list(combinations(lado_atual, 1)) + list(combinations(lado_atual, 2))
    
    for grupo in grupos_possiveis:
        tempo_viagem = max(tempos[p] for p in grupo)
        novo_tempo = estado.tempo + tempo_viagem
        
        # Restrição 3: Limite de tempo
        if novo_tempo > 17:
            continue
            
        nova_origem = estado.origem.copy()
        novo_destino = estado.destino.copy()
        
        # Transição: Ida (0 -> 1) ou Volta (1 -> 0)
        if estado.lanterna == 0: 
            nova_origem.difference_update(grupo)
            novo_destino.update(grupo)
            nova_lanterna = 1
        else:
            novo_destino.difference_update(grupo)
            nova_origem.update(grupo)
            nova_lanterna = 0
            
        novo_estado = Estado(nova_origem, novo_destino, nova_lanterna, novo_tempo)
        proximos_estados.append(novo_estado)
        
    return proximos_estados

# Instanciando o Estado Inicial
todas_pessoas = {'aluno', 'professora', 'zelador', 'cientista'}
estado_inicial = Estado(todas_pessoas, set(), 0, 0)
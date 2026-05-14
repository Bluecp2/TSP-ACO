import random
from ambiente import Ambiente
class Formiga:
    def __init__(self, cidade_inicial, num_total_cidades):
        self.caminho = [cidade_inicial]
        self.visitados = {cidade_inicial}
        self.distancia_percorrida = 0.0
        self.num_total_cidades = num_total_cidades

    def selecionar_proxima_cidade(self, g: 'Ambiente', alfa, beta):
        cidade_atual = self.caminho[-1]
        candidatas = [c for c in range(self.num_total_cidades) if c not in self.visitados]
        
        pesos = []
        soma_total_atratividade = 0.0
        
        for proxima in candidatas:
            tau = g.feromonios[cidade_atual][proxima]
            eta = g.visibilidade[cidade_atual][proxima]
            
            atratividade = (tau ** alfa) * (eta ** beta)
            pesos.append(atratividade)
            soma_total_atratividade += atratividade
        
        sorteio = random.uniform(0, soma_total_atratividade)
        acumulado = 0.0
        
        for i, peso in enumerate(pesos):
            acumulado += peso
            if acumulado >= sorteio:
                return candidatas[i]
        
        return candidatas[-1]

    def construir_solucao(self, g: 'Ambiente', alfa, beta):
        while len(self.visitados) < self.num_total_cidades:
            proxima = self.selecionar_proxima_cidade(g, alfa, beta)
            
            u = self.caminho[-1]
            self.distancia_percorrida += g.distancias[u][proxima]
            self.caminho.append(proxima)
            self.visitados.add(proxima)
        
        origem = self.caminho[0]
        ultimo = self.caminho[-1]            
        self.distancia_percorrida += g.distancias[ultimo][origem]
        self.caminho.append(origem)

    def limpar(self, cidade_inicial):
        self.caminho = [cidade_inicial]
        self.visitados = {cidade_inicial}
        self.distancia_percorrida = 0.0
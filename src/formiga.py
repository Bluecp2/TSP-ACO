class Formiga:
    def __init__(self, cidade_inicial):
        # Inicializa o caminho com a cidade de partida [cite: 9]
        self.caminho = [cidade_inicial]
        # Conjunto para controle rápido de cidades já visitadas (lista tabu) [cite: 9]
        self.visitados = {cidade_inicial}
        self.distancia_percorrida = 0.0

    def selecionar_proxima_cidade(self, g: 'Grafo', alfa, beta):
        """
        Calcula a probabilidade de transição baseada no feromônio (alfa) 
        e na visibilidade (beta).
        """
        # A lógica da roleta ou busca gananciosa entraria aqui
        pass

    def construir_solucao(self, g: 'Grafo', alfa, beta):
        """
        Ciclo principal da formiga para percorrer todas as cidades 
        da instância[cite: 7, 14].
        """
        # Enquanto não visitar todas as cidades do grafo
        # proxima = self.selecionar_proxima_cidade(g, alfa, beta)
        # self.caminho.append(proxima)
        # self.visitados.add(proxima)
        pass

    def limpar(self, cidade_inicial):
        """Reseta a formiga para o próximo ciclo de iteração."""
        self.caminho = [cidade_inicial]
        self.visitados = {cidade_inicial}
        self.distancia_percorrida = 0.0
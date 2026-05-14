import numpy as np

class Ambiente:
    def __init__(self, matriz_distancias: np.ndarray, tau_0: float = 1e-6):
        self.distancias = matriz_distancias
        self.num_cidades = len(matriz_distancias)
        
        self.feromonios = np.full((self.num_cidades, self.num_cidades), tau_0)
        
        self.visibilidade = 1.0 / (self.distancias + np.eye(self.num_cidades) * 1e-9)#isso aqui e pra nao ter problemas de divisao por 0

    def aplicar_evaporacao(self, rho):
        self.feromonios *= (1- rho)

    def depositar_feromonio(self, i, j, quantidade):
       self.feromonios[i][j] += quantidade
       self.feromonios[j][i] += quantidade

    @staticmethod
    def carregar_instancia(caminho_arquivo) -> np.ndarray:
        return np.loadtxt(caminho_arquivo)
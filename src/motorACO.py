from ambiente import Ambiente
from formiga import Formiga
import copy

class MotorACO:
    def __init__(self, ambiente: 'Ambiente', num_formigas, alfa, beta, rho, q):
        self.ambiente = ambiente
        self.num_formigas = num_formigas
        self.alfa = alfa
        self.beta = beta
        self.rho = rho
        self.q = q
        
        self.melhor_caminho = None
        self.melhor_distancia = float('inf')

    def executar(self, num_iteracoes: int):
        for t in range(num_iteracoes):
            colonia = []
            
            for _ in range(self.num_formigas):
                formiga = Formiga(0, self.ambiente.num_cidades)
                formiga.construir_solucao(self.ambiente, self.alfa, self.beta)
                colonia.append(formiga)
                
                if formiga.distancia_percorrida < self.melhor_distancia:
                    self.melhor_distancia = formiga.distancia_percorrida
                    self.melhor_caminho = list(formiga.caminho)
                
            self.ambiente.aplicar_evaporacao(self.rho)
            self._atualizar_feromonios_global(colonia)
                

    def _atualizar_feromonios_global(self, colonia):
        for formiga in colonia:
            delta_tau = self.q / formiga.distancia_percorrida
            
            for k in range(len(formiga.caminho) - 1):
                i = formiga.caminho[k]
                j = formiga.caminho[k + 1]
                self.ambiente.depositar_feromonio(i, j, delta_tau)
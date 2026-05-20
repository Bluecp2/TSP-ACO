from src.motorACO import MotorACO
from src.ambiente import Ambiente
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from itertools import product


class ExperimentoFatorial:

    def __init__(self, distancias_arquivo,
                 n_interacao=20,
                 n_geracoes=20):

        self.distancias_np = Ambiente.carregar_instancia(
            distancias_arquivo
        )

        self.n_interacao = n_interacao
        self.n_geracoes = n_geracoes

        self.fatores = {
            'alfa': [1.0, 2.0],
            'beta': [2.0, 5],
            'rho': [0.1,0.5],
            'Q': [100],
            'populacao': [50]
        }

        self.dados_tabela = []
        self.convergencia_global = {}

        self.melhor_absoluto = float('inf')

        self.pasta_saida = "resultados"

        os.makedirs(self.pasta_saida, exist_ok=True)

    def _executar_configuracoes(self, config, id_config):

        resultados = []

        historico_acumulado = np.zeros(self.n_geracoes)

        for t in range(self.n_interacao):

            ambiente = Ambiente(self.distancias_np)
            
            motor = MotorACO(
                ambiente=ambiente,
                num_formigas=config['populacao'],
                alfa=config['alfa'],
                beta=config['beta'],
                rho=config['rho'],
                q=config['Q']
            )
            
            historico_corrida = []
            for g in range(self.n_geracoes):
                motor.executar(num_iteracoes=1)
                historico_corrida.append(motor.melhor_distancia)
            
            resultados.append(motor.melhor_distancia)
            
            historico_acumulado += np.array(historico_corrida)

            if motor.melhor_distancia < self.melhor_absoluto:
                self.melhor_absoluto = motor.melhor_distancia

        historico_medio = historico_acumulado / self.n_interacao

        self.convergencia_global[id_config] = historico_medio

        media = np.mean(resultados)
        desvio = np.std(resultados)
        melhor = np.min(resultados)
        pior = np.max(resultados)

        self.dados_tabela.append({
            'configuracao': id_config,
            'alfa': config['alfa'],
            'beta': config['beta'],
            'rho': config['rho'],
            'Q': config['Q'],
            'populacao': config['populacao'],
            'media': media,
            'desvio_padrao': desvio,
            'melhor': melhor,
            'pior': pior
        })

    def rodar(self):

        combinacoes = product(
            self.fatores['alfa'],
            self.fatores['beta'],
            self.fatores['rho'],
            self.fatores['Q'],
            self.fatores['populacao']
        )

        contador = 1

        for alfa, beta, rho, q, pop in combinacoes:

            config = {
                'alfa': alfa,
                'beta': beta,
                'rho': rho,
                'Q': q,
                'populacao': pop
            }

            id_config = f"Configuracao_{contador}"

            print(f"\nExecutando {id_config}")
            print(config)

            self._executar_configuracoes(
                config,
                id_config
            )

            contador += 1

        df = pd.DataFrame(self.dados_tabela)

        caminho_csv = os.path.join(
            self.pasta_saida,
            "resultado.csv"
        )

        df.to_csv(caminho_csv, index=False)

        print(f"\ncsv em: {caminho_csv}\n")

        print(f"Melhor absoluto: {self.melhor_absoluto}\n")


        self._plot_convergencia()

    def _plot_convergencia(self):

        plt.figure(figsize=(12, 6))

        for id_config, valores in self.convergencia_global.items():
            plt.plot(
                valores,
                label=id_config
            )

        plt.title("Grafico de Convergencia do ACO")
        plt.xlabel("Geracoes")
        plt.ylabel("Melhor Distancia")
        plt.legend()

        caminho_grafico = os.path.join(
            self.pasta_saida,
            "convergencia_final.png"
        )

        plt.savefig(caminho_grafico)
        plt.close()

        print(f"Grafico em: {caminho_grafico}\n")

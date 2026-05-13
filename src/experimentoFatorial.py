class ExperimentoFatorial:
    def __init__(self, instancia_caminho):
        # Carrega dados como LAU15 ou SGB128 
        self.matriz = self._carregar(instancia_caminho)

    def executar(self):
        """
        Define 3 dos valores (α, β, ρ, Q) para um experimento fatorial[cite: 18].
        Sugestões: α=1, β=5, ρ=0,5, Q=100[cite: 23].
        """
        # Loops aninhados para testar as combinações de parâmetros
        pass

    def _carregar(self, caminho):
        """Lê os arquivos de distâncias (ex: lau15_dist.txt)[cite: 14]."""
        pass
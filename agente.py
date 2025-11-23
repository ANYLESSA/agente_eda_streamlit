
import matplotlib.pyplot as plt
import seaborn as sns
from utils import gerar_estatisticas, gerar_grafico

class AgenteEDA:
    def __init__(self, df):
        self.df = df
        self.memoria = []

    def responder(self, pergunta):
        pergunta_lower = pergunta.lower()
        resposta = ""
        grafico = None

        if "média" in pergunta_lower:
            col = pergunta.split()[-1]
            if col in self.df.columns:
                resposta = f"Média de {col}: {self.df[col].mean()}"
        elif "distribuição" in pergunta_lower:
            col = pergunta.split()[-1]
            if col in self.df.columns:
                grafico = gerar_grafico(self.df, col)
                resposta = f"Distribuição da coluna {col}"
        elif "estatísticas" in pergunta_lower:
            resposta = gerar_estatisticas(self.df)
        elif "conclusões" in pergunta_lower:
            resposta = "Com base nos dados, há padrões e possíveis outliers. Classes desbalanceadas indicam necessidade de técnicas de balanceamento."

        self.memoria.append((pergunta, resposta))
        return resposta, grafico

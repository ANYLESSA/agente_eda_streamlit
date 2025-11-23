
import matplotlib.pyplot as plt
import seaborn as sns

def gerar_estatisticas(df):
    return df.describe().to_string()

def gerar_grafico(df, coluna):
    fig, ax = plt.subplots()
    sns.histplot(df[coluna], ax=ax)
    ax.set_title(f"Distribuição de {coluna}")
    return fig

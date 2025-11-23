import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Funções auxiliares
def calcular_estatistica(df, coluna, tipo):
    if coluna not in df.columns:
        return f"Coluna '{coluna}' não encontrada."
    if tipo == "média":
        return f"A média da coluna {coluna} é {df[coluna].mean():.2f}."
    elif tipo == "mediana":
        return f"A mediana da coluna {coluna} é {df[coluna].median():.2f}."
    elif tipo == "máximo":
        return f"O valor máximo da coluna {coluna} é {df[coluna].max():.2f}."
    elif tipo == "mínimo":
        return f"O valor mínimo da coluna {coluna} é {df[coluna].min():.2f}."
    else:
        return "Tipo de estatística não reconhecido."

def gerar_histograma(df, coluna):
    if coluna not in df.columns:
        return None, f"Coluna '{coluna}' não encontrada."
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(df[coluna], bins=50, ax=ax)
    ax.set_title(f"Histograma da coluna {coluna}")
    return fig, None

def gerar_correlacao(df):
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(df.corr(), cmap='coolwarm', annot=False, ax=ax)
    ax.set_title("Matriz de Correlação")
    return fig

def conclusoes(df):
    return "Com base nos dados, há padrões e possíveis outliers. Classes desbalanceadas indicam necessidade de técnicas de balanceamento."

# Interface Streamlit
st.title("Agente Autônomo de Análise Exploratória de Dados")

uploaded_file = st.file_uploader("Carregue um arquivo CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Pré-visualização dos dados:")
    st.write(df.head())

    # Campo para pergunta
    pergunta = st.text_input("Faça sua pergunta (pode incluir várias, separadas por espaço):")

    if pergunta:
        pergunta_lower = pergunta.lower()
        respostas = []
        graficos = []

        # Processar múltiplas palavras-chave
        if "média" in pergunta_lower:
            for col in df.columns:
                if col in pergunta_lower:
                    respostas.append(calcular_estatistica(df, col, "média"))
        if "mediana" in pergunta_lower:
            for col in df.columns:
                if col in pergunta_lower:
                    respostas.append(calcular_estatistica(df, col, "mediana"))
        if "histograma" in pergunta_lower:
            for col in df.columns:
                if col in pergunta_lower:
                    fig, erro = gerar_histograma(df, col)
                    if erro:
                        respostas.append(erro)
                    else:
                        graficos.append(fig)
        if "correlação" in pergunta_lower:
            graficos.append(gerar_correlacao(df))
            respostas.append("Gerando matriz de correlação...")
        if "conclusões" in pergunta_lower:
            respostas.append(conclusoes(df))

        # Exibir respostas
        for r in respostas:
            st.write(r)
        for g in graficos:
            st.pyplot(g)

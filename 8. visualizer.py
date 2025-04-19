import matplotlib.pyplot as plt
import seaborn as sns

def plot_ranking(df):
    df_sorted = df.sort_values("Pontuação Total", ascending=False)
    plt.figure(figsize=(10, 5))
    sns.barplot(x="Pontuação Total", y="Empresa", data=df_sorted, palette="viridis")
    plt.title("Ranking ESG das Empresas")
    plt.xlabel("Pontuação ESG")
    plt.tight_layout()
    plt.show()

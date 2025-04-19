from src.esg.empresa import Empresa
from src.esg.esg_calculator import calcular_pontuacao_esg
from src.esg.visualizer import plot_ranking
import pandas as pd

def main():
    empresas = [
        Empresa("Empresa A", 85, 90, 75),
        Empresa("Empresa B", 70, 60, 90),
        Empresa("Empresa C", 95, 88, 80),
    ]

    dados = []
    for emp in empresas:
        total = calcular_pontuacao_esg(emp)
        dados.append({
            "Empresa": emp.nome,
            "E": emp.ambiental,
            "S": emp.social,
            "G": emp.governanca,
            "Pontuação Total": total
        })

    df = pd.DataFrame(dados)
    df.to_csv("data/empresas_esg.csv", index=False)
    print("Relatório ESG salvo em data/empresas_esg.csv")

    plot_ranking(df)

if __name__ == "__main__":
    main()

import pandas as pd
from src.esg.visualizer import plot_ranking

def test_plot(monkeypatch):
    monkeypatch.setattr("matplotlib.pyplot.show", lambda: None)
    df = pd.DataFrame({
        "Empresa": ["A", "B"],
        "Pontuação Total": [85, 75]
    })
    plot_ranking(df)

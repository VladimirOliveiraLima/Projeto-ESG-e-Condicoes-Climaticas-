def calcular_pontuacao_esg(empresa, pesos=None):
    """
    Calcula pontuação ponderada ESG de uma empresa.
    """
    if pesos is None:
        pesos = {"E": 0.33, "S": 0.33, "G": 0.34}

    score = (
        empresa.ambiental * pesos["E"] +
        empresa.social * pesos["S"] +
        empresa.governanca * pesos["G"]
    )
    return round(score, 2)

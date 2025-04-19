def normalizar(valor, minimo=0, maximo=100):
    return max(min(valor, maximo), minimo)

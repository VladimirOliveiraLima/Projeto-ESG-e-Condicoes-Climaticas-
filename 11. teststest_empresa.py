from src.esg.empresa import Empresa

def test_empresa_init():
    emp = Empresa("Teste", 80, 85, 90)
    assert emp.nome == "Teste"
    assert emp.ambiental == 80

import unittest

# Função simples para testar
def soma(a, b):
    return a + b

class TestSoma(unittest.TestCase):

    def test_soma(self):
        # Verificando se 2 + 3 é igual a 5
        self.assertEqual(soma(2, 3), 5)

    def test_soma_negativos(self):
        # Verificando se -1 + -1 é igual a -2
        self.assertEqual(soma(-1, -1), -2)

    def test_soma_zero(self):
        # Verificando se 0 + 0 é igual a 0
        self.assertEqual(soma(0, 0), 0)

if __name__ == '__main__':
    unittest.main()

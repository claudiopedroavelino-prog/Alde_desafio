import unittest
from app import app

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_registro(self):
        resposta = self.app.post('/registro', data={
            "nome": "Teste",
            "apelido": "Bot",
            "senha": "1234",
            "telefone": "910000000"
        })
        self.assertEqual(resposta.status_code, 201)

    def test_login_sucesso(self):
        # Primeiro, registre um usuário
        self.app.post('/registro', data={
            "nome": "Teste",
            "apelido": "Bot",
            "senha": "1234",
            "telefone": "910000000"
        })

        # Depois, faça o login
        resposta = self.app.post('/Login', data={
            "telefone": "910000000",
            "senha": "1234"
        })
        self.assertEqual(resposta.status_code, 302)  # Redirecionamento

if __name__ == "__main__":
    unittest.main()

import unittest
from biblioteca import Biblioteca
from modelos.livro import Livro
from modelos.usuario import Usuario
from modelos.exceptions import *
from modelos.estrategia_multa import MultaFixa, MultaPorDiaAtraso

class TestBiblioteca(unittest.TestCase):
    def setUp(self):
        self.bib = Biblioteca()
        self.user = Usuario("Ana", 1)
        self.book = Livro("Dom Casmurro", "Machado de Assis", 1899, 2)
        self.bib.cadastrar_usuario(self.user)
        self.bib.adicionar_livro(self.book)

    def test_emprestar_livro(self):
        self.bib.emprestar_livro(1, "Dom Casmurro")
        self.assertEqual(self.book.quantidade, 1)

    def test_devolver_livro(self):
        self.bib.emprestar_livro(1, "Dom Casmurro")
        self.bib.devolver_livro(1, "Dom Casmurro")
        self.assertEqual(self.book.quantidade, 2)

    def test_usuario_nao_encontrado(self):
        with self.assertRaises(UsuarioNaoEncontradoException):
            self.bib.emprestar_livro(99, "Dom Casmurro")

    def test_livro_indisponivel(self):
        self.bib.emprestar_livro(1, "Dom Casmurro")
        self.bib.emprestar_livro(1, "Dom Casmurro")
        with self.assertRaises(LivroIndisponivelException):
            self.bib.emprestar_livro(1, "Dom Casmurro")

    def test_multa_fixa(self):
        self.bib.emprestar_livro(1, "Dom Casmurro")
        multa = self.bib.calcular_multa(1, MultaFixa())
        self.assertEqual(multa, 10)

    def test_multa_dias_atraso(self):
        self.bib.emprestar_livro(1, "Dom Casmurro")
        multa = self.bib.calcular_multa(1, MultaPorDiaAtraso())
        self.assertGreaterEqual(multa, 0) 
        
if __name__ == '__main__':
    unittest.main()

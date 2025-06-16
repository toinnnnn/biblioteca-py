from modelos.livro import Livro
from modelos.usuario import Usuario
from modelos.emprestimo import Emprestimo
from modelos.exceptions import *
from modelos.estrategia_multa import EstrategiaMulta

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []
        self.emprestimos = []

    def adicionar_livro(self, livro: Livro):
        self.livros.append(livro)

    def cadastrar_usuario(self, usuario: Usuario):
        self.usuarios.append(usuario)

    def emprestar_livro(self, id_usuario, titulo_livro):
        usuario = next((u for u in self.usuarios if u.id == id_usuario), None)
        if not usuario:
            raise UsuarioNaoEncontradoException("Usuário não encontrado.")

        livro = next((l for l in self.livros if l.titulo == titulo_livro and l.quantidade > 0), None)
        if not livro:
            raise LivroIndisponivelException("Livro não disponível.")

        livro.quantidade -= 1
        emprestimo = Emprestimo(usuario, livro)
        self.emprestimos.append(emprestimo)

    def devolver_livro(self, id_usuario, titulo_livro):
        for e in self.emprestimos:
            if e.usuario.id == id_usuario and e.livro.titulo == titulo_livro and not e.devolvido:
                e.devolvido = True
                e.livro.quantidade += 1
                return
        raise EmprestimoNaoEncontradoException("Empréstimo não encontrado.")

    def calcular_multa(self, id_usuario, estrategia: EstrategiaMulta):
        emprestimo_usuario = [e for e in self.emprestimos if e.usuario.id == id_usuario]
        return estrategia.calcular(emprestimo_usuario)
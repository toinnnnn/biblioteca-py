from datetime import date

class Emprestimo:
    def __init__(self, usuario, livro):
        self.usuario = usuario
        self.livro = livro
        self.data_emprestimo = date.today()
        self.devolvido = False

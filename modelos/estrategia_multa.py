from abc import ABC, abstractmethod
from datetime import date

class EstrategiaMulta(ABC):
    @abstractmethod
    def calcular(self, emprestimos):
        pass

class MultaFixa(EstrategiaMulta):
    def calcular(self, emprestimos):
        return sum(10 for emprestimo in emprestimos if not emprestimo.devolvido )
    

class MultaPorDiaAtraso(EstrategiaMulta):
    def calcular(self, emprestimos):
        multa_total = 0
        for emprestimo in emprestimos:
            if not emprestimo.devolvido:
                dias = (date.today() - emprestimo.data_emprestimo).days
                multa_total += dias * 2 #Aplicando multa de 2 reais por dia igual a biblioteca do senac
        return multa_total
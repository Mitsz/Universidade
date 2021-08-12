from entidade.disciplina import Disciplina
from entidade.pessoa import Pessoa

class Aluno(Pessoa):
    
    def __init__(self, nome: str, codigo: int, idade):
        super().__init__(nome, codigo, idade)
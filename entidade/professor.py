
from entidade.disciplina import Disciplina

from entidade.pessoa import Pessoa

class Professor(Pessoa):
    
    def __init__(self, nome: str, codigo: int):
        super().__init__(nome, codigo)
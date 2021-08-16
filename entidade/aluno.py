from entidade.disciplina import Disciplina
from entidade.pessoa import Pessoa

class Aluno(Pessoa):
    
    def __init__(self, nome: str, matricula: int, idade):
        super().__init__(nome, idade)

        if isinstance(matricula, int):
            self.__matricula = matricula
        else: 
            raise Exception


    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def codigo(self, matricula: int):
        if isinstance(matricula, int):
            self.__matricula = matricula
        else:
            raise Exception
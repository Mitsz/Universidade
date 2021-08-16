from entidade.curso import Curso
from entidade.professor import Professor
from entidade.curso import Curso

class Disciplina():

    def __init__(
        self, 
        nome: str, 
        codigo: int, 
        curso: Curso, 
        professor_responsavel: Professor,
        max_alunos: int
        ):

        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(codigo, int):
            self.__codigo = codigo
        if isinstance(curso, Curso):
            self.__curso = curso
        if isinstance(professor_responsavel, Professor):
            self.__professor_responsavel = professor_responsavel
        if isinstance(max_alunos, int):
            self.__max_alunos = max_alunos
        #self.__lista_disciplinas = []
        #lista alunos
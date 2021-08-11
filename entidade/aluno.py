
class Aluno():

    def __init__(
        self, 
        nome: str, 
        matricula: int, 
        idade: int
        ):

        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(matricula, int):
            self.__matricula = matricula
        if isinstance(idade, int):
            self.__idade = idade
        self.__lista_alunos = []

        




class Curso():

    def __init__(
        self, 
        nome: str, 
        codigo: int
        ):

        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(codigo, int):
            self.__codigo = codigo
        self.__lista_cursos = []

        



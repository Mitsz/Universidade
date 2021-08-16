class Curso():

    def __init__(self, nome: str, codigo: int):

        if isinstance(nome, str) and isinstance(codigo, int):
            self.__nome = nome
            self.__codigo = codigo
            self.__lista_curso: list = []
            
@property
def codigo(self) -> int():
    return self.__codigo

@property
def nome(self) -> str:
    return self.__nome

@nome.setter
def nome(self, nome: str):
    self.__nome = nome
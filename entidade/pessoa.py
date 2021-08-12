from abc import ABC, abstractmethod

class Pessoa(ABC):

    @abstractmethod
    def __init__(self, nome: str, codigo: int, idade:int):
        if(isinstance(nome, str) and
         isinstance(codigo, int) and
         isinstance(idade, int) and 0<idade<=150
        ):
            self.__nome = nome
            self.__codigo = codigo
            self.__idade = idade
        else:
            raise Exception
        

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise Exception
    @property
    def codigo(self):
        return self.__codigo

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade: int):
        if isinstance(idade, int):
            self.__idade = idade
        else:
            raise Exception
            
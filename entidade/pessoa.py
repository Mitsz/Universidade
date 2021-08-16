from abc import ABC, abstractmethod

class Pessoa(ABC):

    @abstractmethod
    def __init__(self, nome: str, data_nasc:int):
        if(isinstance(nome, str) and
         isinstance(data_nasc, int)
        ):
            self.__nome = nome
            self.__data_nasc = data_nasc
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
    def data_nasc(self):
        return self.__data_nasc

    @data_nasc.setter
    def data_nasc(self, data_nasc: int):
        if isinstance(data_nasc, int):
            self.__data_nasc = data_nasc
        else:
            raise Exception
            
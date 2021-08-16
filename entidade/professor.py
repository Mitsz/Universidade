from entidade.pessoa import Pessoa

class Professor(Pessoa):
    
    def __init__(self, nome: str, codigo: int, idade):
        super().__init__(nome, idade)

        if isinstance(codigo, int):
            self.__codigo = codigo
        else: 
            raise Exception

        
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo: int):
        if isinstance(codigo, int):
            self.__codigo = codigo
        else:
            raise Exception
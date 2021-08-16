from entidade.professor import Professor
from tela.telaprofessor import TelaProfessor
from controle.excecoes import ListaVaziaException
from controle.excecoes import NenhumSelecionadoException
from controle.excecoes import CampoEmBrancoException

class ControladorProfessor():

    def __init__(self, ControladorSistema):
        self.__controladosistema = ControladorSistema
        self.__tela_professor = TelaProfessor()
        self.__lista_professor = []

    def abre_tela_professor(self):
        lista_opcoes = {
            1: self.adiciona_professor, 
            2: self.remove_professor, 
            3: self.edita_professor, 
            4: self.mostra_professor
            }
        while True:
            valor_lido = self.__tela_professor.tela_professor()
            if valor_lido == 0 or valor_lido == None:
                break
            else:
                lista_opcoes[valor_lido]()


    def adiciona_professor(self):
        dados = self.__tela_professor.cadastra_professor()
        while True:
            try:
                if dados == None:
                    break
                if dados['nome'] == '' or dados['idade'] == '' or dados['matricula'] == '':
                    raise CampoEmBrancoException
                else:
                    try:
                        if int(dados['idade']) < 18 or int(dados['idade']) > 150:
                            raise ValueError
                        break
                    except ValueError:
                        print('A idade deve ser um numero inteiro entre 18 e 150!') 
            except CampoEmBrancoException as mensagem:
                self.__tela_professor.mensagem(mensagem)
        if dados is not None: 
            self.__lista_professor.append(Professor(dados['nome'], int(dados['matricula']), int(dados['idade'])))


    def remove_professor(self):
        professor_selecionado = self.encontra_professor_por_codigo()
        if professor_selecionado is not None:
            self.__lista_professor.remove(professor_selecionado)
            self.__tela_professor.mensagem('Excluido!')


    def edita_professor(self, professor):
        if professor is not None: 
            while True:
                try:
                    novo_nome = self.__tela_professor.le_nome(professor.nome)
                    if novo_nome == '':
                        raise CampoEmBrancoException 
                    else:
                        break
                except CampoEmBrancoException as mensagem:
                    self.__tela_professor.mensagem(mensagem)
        if professor is not None and novo_nome is not None:
            professor.nome = novo_nome


    def lista_professors(self): 
        if len(self.__lista_professor) == 0:
            raise ListaVaziaException
        else:
            return self.__lista_professor
                

    def encontra_professor_por_codigo(self, codigo):
        pass
  

    def mostra_professor(self):
        self.__tela_professor.mostra_professor(self.__lista_professor())


    def seleciona_professor(self):
        pass
    #ainda em processo de criação
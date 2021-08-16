from entidade.atividade import Atividade
from tela.telaatividade import TelaAtividade
from controle.excecoes import ListaVaziaException
from controle.excecoes import NenhumSelecionadoException
from controle.excecoes import CampoEmBrancoException

class ControladorAtividade():

    def __init__(self, ControladorSistema):
        self.__controladosistema = ControladorSistema
        self.__tela_atividade = TelaAtividade()
        self.__lista_atividade = []

    def abre_tela_atividade(self):
        lista_opcoes = {
            1: self.adiciona_atividade, 
            2: self.remove_atividade, 
            3: self.edita_atividade, 
            4: self.mostra_atividade
            }
        while True:
            valor_lido = self.__tela_atividade.tela_atividade()
            if valor_lido == 0 or valor_lido == None:
                break
            else:
                lista_opcoes[valor_lido]()


    def adiciona_atividade(self):
        dados = self.__tela_atividade.cadastra_atividade()
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
                self.__tela_atividade.mensagem(mensagem)
        if dados is not None: 
            self.__lista_atividade.append(Atividade(dados['nome'], int(dados['matricula']), int(dados['idade'])))


    def remove_atividade(self):
        atividade_selecionado = self.encontra_atividade_por_codigo()
        if atividade_selecionado is not None:
            self.__lista_atividade.remove(atividade_selecionado)
            self.__tela_atividade.mensagem('Excluido!')


    def edita_atividade(self, atividade):
        if atividade is not None: 
            while True:
                try:
                    novo_nome = self.__tela_atividade.le_nome(atividade.nome)
                    if novo_nome == '':
                        raise CampoEmBrancoException 
                    else:
                        break
                except CampoEmBrancoException as mensagem:
                    self.__tela_atividade.mensagem(mensagem)
        if atividade is not None and novo_nome is not None:
            atividade.nome = novo_nome


    def lista_atividades(self): 
        if len(self.__lista_atividade) == 0:
            raise ListaVaziaException
        else:
            return self.__lista_atividade
                

    def encontra_atividade_por_codigo(self, codigo):
        pass
  

    def mostra_atividade(self):
        self.__tela_atividade.mostra_atividade(self.__lista_atividade())


    def seleciona_atividade(self):
        pass
    #ainda em processo de criação
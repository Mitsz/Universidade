from entidade.aluno import Aluno
from tela.telaaluno import TelaAluno
from controle.excecoes import ListaVaziaException
from controle.excecoes import NenhumSelecionadoException
from controle.excecoes import CampoEmBrancoException

class ControladorAluno():

    def __init__(self, tela_aluno: TelaAluno):
        self.__tela_aluno = tela_aluno
        self.__lista_aluno = []


    def adiciona_aluno(self):
        dados = self.__tela_aluno.cadastra_aluno()
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
                self.__tela_aluno.mensagem(mensagem)
        if dados is not None: 
            self.__lista_aluno.append(Aluno(dados['nome'], int(dados['matricula']), int(dados['idade'])))


    def remove_aluno(self):
        aluno_selecionado = self.encontra_aluno_por_codigo()
        if aluno_selecionado is not None:
            self.__lista_aluno.remove(aluno_selecionado)
            self.__tela_aluno.mensagem('Excluido!')


    def edita_aluno(self, aluno):
        if aluno is not None: 
            while True:
                try:
                    novo_nome = self.__tela_aluno.le_nome(aluno.nome)
                    if novo_nome == '':
                        raise CampoEmBrancoException 
                    else:
                        break
                except CampoEmBrancoException as mensagem:
                    self.__tela_aluno.mensagem(mensagem)
        if aluno is not None and novo_nome is not None:
            aluno.nome = novo_nome


    def lista_alunos(self): 
        if len(self.__lista_aluno) == 0:
            raise ListaVaziaException
        else:
            return self.__lista_aluno
                

    def encontra_aluno_por_codigo(self, codigo):
        pass
  

    def mostra_aluno(self):
        self.__tela_aluno.mostra_aluno(self.__lista_aluno())


    def seleciona_aluno(self):
        pass
    #ainda em processo de criação


    def abre_tela_aluno(self):
        lista_opcoes = {
            1: self.adiciona_aluno(), 
            2: self.remove_aluno(), 
            3: self.edita_aluno(), 
            4: self.mostra_aluno()
            }
        while True:
            valor_lido = self.__tela_aluno.opces_aluno()
            if valor_lido == 0 or valor_lido == None:
                break
            else:
                lista_opcoes[valor_lido]()
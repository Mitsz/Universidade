from entidade.disciplina import Disciplina
from tela.teladisciplina import TelaDisciplina
from controle.excecoes import ListaVaziaException
from controle.excecoes import NenhumSelecionadoException
from controle.excecoes import CampoEmBrancoException

class ControladorDisciplina():

    def __init__(self, ControladorSistema):
        self.__controladosistema = ControladorSistema
        self.__tela_disciplina = TelaDisciplina()
        self.__lista_disciplina = []

    def abre_tela_disciplina(self, TelaDisciplina):
        lista_opcoes = {
            1: self.adiciona_disciplina, 
            2: self.remove_disciplina, 
            3: self.edita_disciplina, 
            4: self.mostra_disciplina
            }
        while True:
            valor_lido = self.__tela_disciplina.tela_disciplina()
            if valor_lido == 0 or valor_lido == None:
                break
            else:
                lista_opcoes[valor_lido]()


    def adiciona_disciplina(self):
        dados = self.__tela_disciplina.cadastra_disciplina()
        while True:
            try:
                if dados == None:
                    break
                if dados['nome'] == '' or dados['codigo'] == '' or dados['curso'] == '' or dados['professor'] == '' or dados['qtd_alunos'] == '':
                    raise CampoEmBrancoException
            except CampoEmBrancoException as mensagem:
                self.__tela_disciplina.mensagem(mensagem)
        if dados is not None: 
            self.__lista_disciplina.append(Disciplina(dados['nome'], int(dados['codigo']), int(dados['curso']), (dados['professor']), int(dados['qtd_alunos'])))


    def remove_disciplina(self):
        disciplina_selecionado = self.encontra_disciplina_por_codigo()
        if disciplina_selecionado is not None:
            self.__lista_disciplina.remove(disciplina_selecionado)
            self.__tela_disciplina.mensagem('Excluido!')


    def edita_disciplina(self, disciplina):
        if disciplina is not None: 
            while True:
                try:
                    novo_nome = self.__tela_disciplina.le_nome(disciplina.nome)
                    if novo_nome == '':
                        raise CampoEmBrancoException 
                    else:
                        break
                except CampoEmBrancoException as mensagem:
                    self.__tela_disciplina.mensagem(mensagem)
        if disciplina is not None and novo_nome is not None:
            disciplina.nome = novo_nome


    def lista_disciplinas(self): 
        if len(self.__lista_disciplina) == 0:
            raise ListaVaziaException
        else:
            return self.__lista_disciplina
                

    def encontra_disciplina_por_codigo(self, codigo):
        pass
  

    def mostra_disciplina(self):
        self.__tela_disciplina.mostra_disciplina(self.__lista_disciplina())


    def seleciona_disciplina(self):
        pass
    #ainda em processo de criação
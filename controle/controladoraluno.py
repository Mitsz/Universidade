from entidade.aluno import Aluno
from tela.telaaluno import TelaAluno

class ControladorAluno():

    def __init__(self, tela_aluno: TelaAluno):
        self.__tela_aluno = tela_aluno

    def adiciona_aluno(self):
        while True:
            try:
                nome = self.__tela_aluno.le_nome() 
                if nome == '':
                    raise CampoEmBrancoException 
                else:
                    break
            except CampoEmBrancoException as mensagem:
                self.__tela_aluno.mensagem(mensagem) 

              
    def remove_aluno(self):
        aluno_selecionado = self.seleciona_aluno()
        if aluno_selecionado is not None:
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
        return self.__lista_alunos

    def encontra_aluno_por_codigo(self, codigo):
        pass
  
    def mostra_aluno(self):
        self.__tela_aluno.mostra_aluno(self.lista_alunos())

    def seleciona_aluno(self):
        pass
    #ainda em processo de criação

    def abre_tela_aluno(self):
        lista_opcoes = {1: self.adiciona_aluno, 2: self.remove_aluno, 3: self.edita_aluno, 4: self.mostra_aluno}
        while True:
            valor_lido = self.__tela_aluno.opces_aluno()
            if valor_lido == 0 or valor_lido == None:
                break
            else:
                lista_opcoes[valor_lido]()


#exceptions incluídas apenas com objetivo de organização de ideias, ainda nao implantadas.
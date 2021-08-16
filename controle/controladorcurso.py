from entidade.curso import Curso
from tela.telacurso import TelaCurso
from controle.excecoes import ListaVaziaException
from controle.excecoes import NenhumSelecionadoException
from controle.excecoes import CampoEmBrancoException

class ControladorCurso():

    def __init__(self, ControladorSistema):
        self.__controladosistema = ControladorSistema
        self.__tela_curso = TelaCurso()
        self.__lista_cursos = []
        self.__codigo_curso = 0

    def abre_tela_curso(self, TelaCurso):
        lista_opcoes = {
            1: self.adiciona_curso, 
            2: self.remove_curso, 
            3: self.edita_curso, 
            4: self.mostra_curso
            }
        while True:
            valor_lido = self.__tela_curso.tela_curso()
            if valor_lido == 0 or valor_lido == None:
                break
            else:
                lista_opcoes[valor_lido]()


    def adiciona_curso(self) -> Curso:
        try:
            nome_curso = self.__tela_curso.cadastra_curso()
            curso = Curso(nome=nome_curso, codigo=(self.__codigo_curso))
            if curso not in self.__lista_cursos:
                self.__lista_cursos.append(curso)
                self.__codigo_curso += 1
                return curso
            print('Curso já cadastrado')
        except CampoEmBrancoException:
            print('Erro no cadastro')

    def remove_curso(self):
        dados = self.__tela_curso.excluir_curso()
        while True:
            try:
                if dados == None:
                    break
                if dados['matricula'] == '':
                    raise CampoEmBrancoException 
            except CampoEmBrancoException as mensagem:
                self.__tela_curso.mensagem(mensagem) 
        
        curso_selecionado = self.encontra_curso_por_codigo(matricula)
        if curso_selecionado is not None:
            self.__lista_curso.remove(curso_selecionado)
            self.__tela_curso.mensagem('Excluido!')


    def edita_curso(self, curso):
        if curso is not None: 
            while True:
                try:
                    novo_nome = self.__tela_curso.le_nome(curso.nome)
                    if novo_nome == '':
                        raise CampoEmBrancoException 
                    else:
                        break
                except CampoEmBrancoException as mensagem:
                    self.__tela_curso.mensagem(mensagem)
        if curso is not None and novo_nome is not None:
            curso.nome = novo_nome


    def lista_curso(self): 
        if len(self.__lista_curso) == 0:
            raise ListaVaziaException
        else:
            return self.__lista_curso
                

    def encontra_curso_por_codigo(self, codigo):
        pass
  

    def mostra_curso(self) -> list[Curso]:
        try:
            self.__tela_curso.mostra_curso(self.__lista_cursos)
        except ListaVaziaException:
            pass

    def seleciona_curso(self):
        pass
    #ainda em processo de criação
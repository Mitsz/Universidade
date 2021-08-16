from tela.telasistema import TelaSistema
from controle.controladorcurso import ControladorCurso
from controle.controladordisciplina import ControladorDisciplina
from controle.controladoratividade import ControladorAtividade
from controle.controladorprofessor import ControladorProfessor
from controle.controladoraluno import ControladorAluno

class ControladorSistema():
    
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_curso = ControladorCurso(ControladorSistema)
        self.__controlador_disciplina = ControladorDisciplina(ControladorSistema)
        self.__controlador_atividade = ControladorAtividade(ControladorSistema)
        self.__controlador_professor = ControladorProfessor(ControladorSistema)
        self.__controlador_aluno = ControladorAluno(ControladorSistema)

    def iniciar_sistema(self):
        self.abre_tela()

    def encerrar_sistema(self, ControladorSistema):
        exit(0)

    def abre_tela(self):
        
        lista_opcoes = {
            1: self.gerencia_curso,
            2: self.gerencia_disciplina,
            3: self.gerencia_atividade,
            4: self.gerencia_professor,
            5: self.gerencia_aluno,
            0: self.encerrar_sistema
            }
            
        while True:
            opcao = self.__tela_sistema.tela_opcoes()

            funcao_escolhida = lista_opcoes[opcao]

            funcao_escolhida(self)

    def gerencia_curso(self, ControladorSistema):
        self.__controlador_curso.abre_tela_curso(self)

    def gerencia_disciplina(self, ControladorSistema):
        self.__controlador_disciplina.abre_tela_disciplina(self)

    def gerencia_atividade(self, ControladorSistema):
        self.__controlador_atividade.abre_tela_atividade(self)

    def gerencia_professor(self, ControladorSistema):
        self.__controlador_professor.abre_tela_professor(self)

    def gerencia_aluno(self, ControladorSistema):
        self.__controlador_aluno.abre_tela_aluno(self)
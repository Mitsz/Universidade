from tela.telasistema import TelaSistema
from controle.controladorcurso import ControladorCurso
from controle.controladordisciplina import ControladorDisciplina
from controle.controladoratividade import ControladorAtividade
from controle.controladorprofessor import ControladorProfessor
from controle.controladoraluno import ControladorAluno

class ControladorSistema():
    
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_curso = ControladorCurso
        self.__controlador_disciplina = ControladorDisciplina
        self.__controlador_atividade = ControladorAtividade
        self.__controlador_professor = ControladorProfessor
        self.__controlador_aluno = ControladorAluno

    def iniciar_sistema(self):
        self.abre_tela()

    def encerrar_sistema(self):
        exit(0)

    def gerencia_curso(self):
        self.__controlador_curso.abre_tela_curso(self)

    def gerencia_disciplina(self):
        self.__controlador_disciplina.abre_tela_disc(self)

    def gerencia_atividade(self):
        self.__controlador_atividade.abre_tela_atv(self)
    
    def gerencia_professor(self):
        self.__controlador_professor.abre_tela_prof(self)

    def gerencia_aluno(self):
        self.__controlador_aluno.abre_tela_aluno(self)

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

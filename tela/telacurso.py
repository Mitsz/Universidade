from entidade.curso import Curso
from controle.excecoes import ListaVaziaException
from controle.excecoes import CampoEmBrancoException

class TelaCurso():
    def __init__(self):
        pass


    def tela_curso(self):
        print('----- CURSO -----')
        print('ESCOLHA O NÚMERO DA OPÇÃO QUE DESEJA REALIZAR')
        print('1 - Cadastrar Curso')
        print('2 - Excluir Curso')
        print('3 - Modificar Curso')
        print('4 - Lista de Cursos')
        print('0 - Retornar')

        opcao = int(input('Escolha a opção: '))
        return opcao

    def cadastra_curso(self):
        print('Você escolheu cadastrar curso')
        print('Preencha os campos a seguir')

        nome = input('Nome: ')
        return {
            'Curso': nome,
        }

    def excluir_curso(self):
        print('Você escolheu excluir curso')
        print('Preencha o nome do curso que deseja excluir do sistema')
        nome = input('Nome: ')

        return nome

    def modifica_curso(self):
        pass

    def mostra_curso(self, ControladorCurso):
        print('Você escolheu listar os cursos cadastrados')
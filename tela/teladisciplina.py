class TelaDisciplina():
    def __init__(self):
        pass


    def tela_disciplina(self):
        print('----- DISCIPLINA -----')
        print('ESCOLHA O NÚMERO DA OPÇÃO QUE DESEJA REALIZAR')
        print('1 - Cadastrar disciplina')
        print('2 - Excluir disciplina')
        print('3 - Modificar disciplina')
        print('4 - Listagem de disciplina')
        print('5 - Lista de alunos por disciplina')
        print('0 - Retornar')

        opcao = int(input('Escolha a opção: '))
        return opcao

    def cadastra_disciplina(self):
        print('Você escolheu cadastrar disciplina')
        print('Preencha os campos a seguir')
        nome = input('Nome da disciplina: ')
        codigo = input('Código da disciplina: ')
        curso = input('Código do curso: ')
        professor = input('Professor Responsável: ')
        qtd_alunos = input('Número máximo de alunos: ')
        
        return {
            '----- DISCIPLINA CADASTRADA -----'
            'Nome da disciplina': nome,
            'Código': codigo,
            'Curso': curso,
            'Professor': professor,
            'Número de alunos': qtd_alunos
        }

    def excluir_disciplina(self):
        print('Você escolheu excluir disciplina')
        print('Preencha o código da disciplina que deseja excluir do sistema')
        codigo = input('Código da Disciplina: ')

        return codigo

    def modificar_disciplina(self):
        print('Você escolheu modificar disciplina')
        print('Informe código da disciplina:')
        print('O que você deseja alterar?')
        print('Digite Nome, Curso, Professor Responsável ou Número máximo de alunos')
        print('Digite nova informação: ')

    def lista_disciplinas(self):
        print('Você escolheu listagem de disciplinas')

    def aluno_disciplina(self):
        print('Você escolheu listar os alunos matriculados em uma disciplina')
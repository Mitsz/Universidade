

class TelaAluno():
    def __init__(self):
        pass


    def tela_aluno(self):
        print('----- ALUNO -----')
        print('ESCOLHA O NÚMERO DA OPÇÃO QUE DESEJA REALIZAR')
        print('1 - Cadastrar aluno')
        print('2 - Excluir aluno')
        print('3 - Modificar aluno')
        print('4 - Lista de alunos')
        print('0 - Retornar')

        opcao = int(input('Escolha a opção: '))
        return opcao

    def cadastra_aluno(self):
        print('Você escolheu cadastrar aluno')
        print('Preencha os campos a seguir')
        nome = input('Nome: ')
        idade = input('Idade: ')
        codigo = input('Matrícula: ')

        return {
            'nome': nome,
            'idade': idade,
            'matricula': codigo
        }

    def excluir_aluno(self):
        print('Você escolheu excluir aluno')
        print('Preencha a matrícula do aluno que deseja excluir do sistema')
        codigo = input('Matrícula: ')

        return codigo

    def lista_alunos(self):
        print('Você escolheu listar os alunos cadastrados')

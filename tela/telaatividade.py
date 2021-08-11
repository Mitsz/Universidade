

class TelaAtividade():
    def __init__(self):
        pass


    def tela_aluno(self):
        print('----- ATIVIDADE -----')
        print('ESCOLHA O NÚMERO DA OPÇÃO QUE DESEJA REALIZAR')
        print('1 - Cadastrar atividade')
        print('2 - Excluir atividade')
        print('3 - Modificar atividade')
        print('4 - Listagem de atividades')
        print('0 - Retornar')

        opcao = int(input('Escolha a opção: '))
        return opcao

    def cadastra_aluno(self):
        print('Você escolheu cadastrar aluno')
        print('Preencha os campos a seguir')
        nome = input('Nome: ')
        idade = input('Idade: ')
        matricula = input('Matrícula: ')

        return {
            'nome': nome,
            'idade': idade,
            'matricula': matricula
        }

    def excluir_aluno(self):
        print('Você escolheu excluir aluno')
        print('Preencha a matrícula do aluno que deseja excluir do sistema')
        matricula = input('Matrícula: ')

        return matricula

    def lista_alunos(self):
        print('Você escolheu listar os alunos cadastrados')

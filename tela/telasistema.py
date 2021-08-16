class TelaSistema():
    def __init__(self):
        pass


    def tela_opcoes(self):
        print('----- UNIVERSIDADE -----')
        print('ESCOLHA O NÚMERO DA OPERAÇÃO QUE DESEJA REALIZAR')
        print('1 - Gerenciar curso')
        print('2 - Gerenciar disciplinas')
        print('3 - Gerenciar atividades')
        print('4 - Gerenciar professores')
        print('5 - Gerenciar alunos')
        print('0 - Sair')

        opcao = int(input('Escolha a opção: '))
        return opcao 
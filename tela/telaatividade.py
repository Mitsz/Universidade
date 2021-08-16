

class TelaAtividade():
    def __init__(self):
        pass


    def tela_aluno(self):
        print('----- ATIVIDADE -----')
        print('ESCOLHA O NÚMERO DA OPÇÃO QUE DESEJA REALIZAR')
        print('1 - Cadastrar atividade')
        print('2 - Excluir atividade')
        print('3 - Modificar atividade')
        print('4- Adicionar nota')
        print('5 - Listagem de atividades')
        print('0 - Retornar')

        opcao = int(input('Escolha a opção: '))
        return opcao

    def cadastra_atividade(self):
        print('Você escolheu adicionar atividade')
        print('Preencha os campos a seguir')
        nome = input('Nome da atividade: ')
        codigo = input('Código da atividade: ')
        disciplina = input('Disciplina: ')
        prazo = input('Prazo: ')

        return {
            'nome': nome,
            'idade': idade,
            'matricula': matricula
        }

    def excluir_aluno(self):
        print('Você escolheu excluir aluno')
        print('Informe código da atividade: ')
        codigo = input('Código da atividade: ')

        return codigo

def modificar_atividade(self):
        print('Você escolheu modificar atividade')
        print('Informe código da atividade: ')
        print('O que você deseja alterar?')
        print('Digite Nome, Tipo, Disciplina ou Prazo')
        print('Digite nova informação: ')

def adicionar_nota(self):
    print('Você escolheu adicionar nota')
    print('Informe código da atividade: ')
    print('Informe matrícula do aluno: ')

def lista_atividades(self):
    print('ESCOLHA O NÚMERO DA OPÇÃO QUE DESEJA REALIZAR')
    print('1 - Listar todas as atividades')
    print('2 - Listar por disciplina')
    print('3 - Listar por aluno')
    print('4- Listar por tipo')
    print('0 - Retornar')
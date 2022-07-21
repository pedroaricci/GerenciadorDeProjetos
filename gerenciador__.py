import pandas as pd

df = pd.read_excel("C:\\Users\\pedro\\music\\Python\\projetos2\\Projetos.xlsx")
df2 = pd.read_excel("C:\\Users\\pedro\\music\\Python\\projetos2\\Atividades.xlsx")

def insereProjeto():
    df = pd.read_excel("C:\\Users\\pedro\\music\\Python\\projetos2\\Projetos.xlsx")
    rows_count = df.count()['Nome do Projeto']
    i = int(rows_count)
    nome = str(input('Insira o nome do seu projeto'))
    df.loc[i, 'Nome do Projeto'] = nome
    dataInicio = input('Insira a data de Início: ')
    df.loc[i, 'Data Inicio'] = dataInicio
    dataFim = input('Insira a data do final prevista: ')
    df.loc[i, 'Data do Fim'] = dataFim
    df.loc[::,'Nome do Projeto':].to_excel("C:\\Users\\pedro\\music\\Python\\projetos2\\Projetos.xlsx")
    df = pd.read_excel("C:\\Users\\pedro\\music\\Python\\projetos2\\Projetos.xlsx")
    return print('Projeto inserido com sucesso!')

def alteraProjeto():
    df = pd.read_excel("C:\\Users\\pedro\\music\\Python\\projetos2\\Projetos.xlsx")
    rows_count = df.count()['Nome do Projeto']
    i = int(rows_count)
    idProjeto = int(input('Insira o ID do projeto que deseja alterar: '))
    if idProjeto <= i-1:
        coluna = int(input('Para alterar o nome digite 1\nPara alterar a data de início digite 2\nPara alterar a data do fim previsto digite 3'))
        if coluna == 1:
            nomeNovo = str(input('Insira o novo nome do projeto que deseja colocar: '))
            df.loc[idProjeto, 'Nome do Projeto'] = nomeNovo
        elif coluna == 2:
            dataInicioNovo = input('Insira a nova data de início: ')
            df.loc[idProjeto, 'Data Inicio'] = dataInicioNovo
        elif coluna == 3:
            dataFimNovo = input('Insira a nova data do final prevista: ')
            df.loc[idProjeto, 'Data do Fim'] = dataFimNovo
        else:
            print('ERRO')
    df.loc[::,'Nome do Projeto':].to_excel("C:\\Users\\pedro\\music\\Python\\projetos2\\Projetos.xlsx")
    df = pd.read_excel("C:\\Users\\pedro\\music\\Python\\projetos2\\Projetos.xlsx")
    return print('Projeto alterado com sucesso!')

def insereAtividade():
    df2 = pd.read_excel("C:\\Users\\pedro\\music\\Python\\projetos2\\Atividades.xlsx")
    rows_count = df2.count()['Nome da Atividade']
    i = int(rows_count)
    idProjeto = int(input('Insira o ID do projeto: '))
    df2.loc[i, 'ID Projeto'] = idProjeto
    nome = str(input('Insira o nome da atividade: '))
    df2.loc[i,'Nome da Atividade'] = nome
    dataInicio = input('Insira a data inicial da atividade: ')
    df2.loc[i, 'Data Inicio'] = dataInicio
    dataFim = input('Insira a data prevista do final da atividade: ')
    df2.loc[i, 'Data do Fim'] = dataFim
    finalizada = str(input('Essa tarefa foi finalizada?\n'))
    df2.loc[i, 'Finalizada?'] = finalizada
    df2.loc[::,'ID Projeto':].to_excel("C:\\Users\\pedro\\music\\Python\\projetos2\\Atividades.xlsx")
    df2 = pd.read_excel("C:\\Users\\pedro\\music\\Python\\projetos2\\Atividades.xlsx")
    return print('Atividade inserida com sucesso!')

def alteraAtividade():
    df2 = pd.read_excel("C:\\Users\\pedro\\music\\Python\\projetos2\\Atividades.xlsx")
    rows_count = df2.count()['Nome da Atividade']
    i = int(rows_count)
    idAtividade = int(input('Insira o ID da atividade que deseja alterar: '))
    if idAtividade <= i-1 and idAtividade >= 0:
        coluna = int(input('Para alterar o ID do projeto digite 1\nPara alterar o nome da atividade digite 2\nPara alterar a data de inicio digite 3\nPara alterar a data de fim digite 4\nPara alterar a situação da atividade digite 5'))
        if coluna == 1:
            idProjeto = int(input('Insira o novo ID do Projeto: '))
            df2.loc[idAtividade, 'ID Projeto'] = idProjeto
        elif coluna == 2:
            nomeNovo = str(input('Insira o novo nome da atividade: '))
            df2.loc[idAtividade, 'Nome da Atividade'] = nomeNovo
        elif coluna == 3:
            dataInicioNovo = input('Insira a nova data de início da atividade: ')
            df2.loc[idAtividade, 'Data Inicio'] = dataInicioNovo
        elif coluna == 4:
            dataFimNovo = input('Insira a nova data do fim previsto da atividade: ')
            df2.loc[idAtividade, 'Data do Fim'] = dataFimNovo
        elif coluna == 5:
            finalizadaNovo = str(input('Essa tarefa já foi finalizada? '))
            df2.loc[idAtividade, 'Finalizada?'] = finalizadaNovo
        else:
            print('ERRO')
    df2.loc[::,'ID Projeto':].to_excel("C:\\Users\\pedro\\music\\Python\\projetos2\\Atividades.xlsx")
    df2 = pd.read_excel("C:\\Users\\pedro\\music\\Python\\projetos2\\Atividades.xlsx")
    return print('Atividade alterada com sucesso!')

def main():
    df = pd.read_excel("C:\\Users\\pedro\\music\\Python\\projetos2\\Projetos.xlsx")
    df2 = pd.read_excel("C:\\Users\\pedro\\music\\Python\\projetos2\\Atividades.xlsx")
    i = 1
    while (i != 0):
        escolha = int(input('Para inserir um novo projeto digite 1\nPara alterar um projeto digite 2\nPara inserir uma atividade digite 3\nPara alterar uma atividade digite 4\nPara sair digite 0\n'))
        if escolha == 1:
            insereProjeto()
        elif escolha == 2:
            alteraProjeto()
        elif escolha == 3:
            insereAtividade()
        elif escolha == 4:
            alteraAtividade()
        elif escolha == 0:
            i = 0
        else:
            print('Escolha errada, insira novamente\n')

main()
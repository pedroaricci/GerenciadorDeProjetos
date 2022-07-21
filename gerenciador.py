from PySimpleGUI import PySimpleGUI as sg
import pandas as pd
import matplotlib.pyplot as plt

#layout
def main():
    sg.theme('Reddit')
    layoutMain = [
        [sg.Button('Inserir Projeto',size=(20,1)), sg.Button('Alterar Projeto', size=(20,1))],
        [sg.Button('Inserir atividade', size=(20,1)), sg.Button('Alterar Atividade', size=(20,1))]
    ]

    janelaMain = sg.Window('Desafio EUAX', layoutMain)

    while True:
        eventos, valores = janelaMain.read()
        if eventos == sg.WINDOW_CLOSED:
            break
        if eventos == 'Inserir Projeto':
            inserirProjeto()
        if eventos == 'Alterar Projeto':
            alterarProjeto()
        if eventos == 'Inserir atividade':
            inserirAtividade()
        if eventos == 'Alterar Atividade':
            alteraAtividade()

    df2 = pd.read_excel("CaminhoPC\\Atividades.xlsx")

    #plt.pie(df2, 'Finalizada?')
    #plt.show()

def inserirProjeto():
    sg.theme('Reddit')
    layoutInsProj = [
        [sg.Text('Nome do Projeto', size=(20,1)), sg.Input(key='nomeProjeto', size=(20,1))],
        [sg.Text('Data de Inicio', size=(20,1)), sg.Input(key='dataInicioProj', size=(20,1))],
        [sg.Text('Data do Fim', size=(20,1)), sg.Input(key='dataFimProj', size=(20,1))],
        [sg.Button('Confirmar')]
    ]

    janelaInsProj = sg.Window('Insere Projeto', layoutInsProj)

    while True:
        eventos, valores = janelaInsProj.read()
        df = pd.read_excel("CaminhoPC\\Projetos.xlsx")
        if eventos == sg.WINDOW_CLOSED:
            break
        if eventos == 'Confirmar':
            rows_count = df.count()['Nome do Projeto']
            i = int(rows_count)
            df.loc[i, 'Nome do Projeto'] = str(valores['nomeProjeto'])
            df.loc[i, 'Data Inicio'] = str(valores['dataInicioProj'])
            df.loc[i, 'Data de Fim'] = str(valores['dataFimProj'])
            df.loc[::,'Nome do Projeto':].to_excel("CaminhoPC\\Projetos.xlsx")
            df = pd.read_excel("CaminhoPC\\Projetos.xlsx")
            janelaInsProj.close()

def alterarProjeto():
    sg.theme('Reddit')
    layoutAltProj = [
        [sg.Text('ID do Projeto', size=(20,1)), sg.Input(key='idProjeto', size=(20,1))],
        [sg.Text('Nome Projeto', size=(20,1)), sg.Input(key='novoNomeProj', size=(20,1))],
        [sg.Text('Data Inicial', size=(20,1)), sg.Input(key='novaDataInicio', size=(20,1))],
        [sg.Text('Data Fim', size=(20,1)), sg.Input(key='novaDataFim', size=(20,1))],
        [sg.Button('Confirmar')]
    ]

    janelaAltProj = sg.Window('Altera Projeto', layoutAltProj)

    while True:
        eventos, valores = janelaAltProj.read()
        df = pd.read_excel("CaminhoPC\\Projetos.xlsx")
        if eventos == sg.WINDOW_CLOSED:
            break
        if eventos == 'Confirmar':
            rows_count = df.count()['Nome do Projeto']
            i = int(rows_count)
            idProjeto = int(valores['idProjeto'])
            if idProjeto <= i-1 and idProjeto >= 0:
                df.loc[idProjeto, 'Nome do Projeto'] = str(valores['novoNomeProj'])
                df.loc[idProjeto, 'Data Inicio'] = str(valores['novaDataInicio'])
                df.loc[idProjeto, 'Data de Fim'] = str(valores['novaDataFim'])
                df.loc[::,'Nome do Projeto':].to_excel("CaminhoPC\\Projetos.xlsx")                
                janelaAltProj.close()
                
def inserirAtividade():
    sg.theme('Reddit')
    layoutInsAtiv = [
        [sg.Text('ID do Projeto', size=(20,1)), sg.Input(key='idProjetoAtiv',size=(20,1))],
        [sg.Text('Nome da Atividade', size=(20,1)), sg.Input(key='nomeAtividade', size=(20,1))],
        [sg.Text('Data de Inicio', size=(20,1)), sg.Input(key='dataInicioAtiv', size=(20,1))],
        [sg.Text('Data de Fim', size=(20,1)), sg.Input(key='dataFimAtiv', size=(20,1))],
        [sg.Text('Atividade Finalizada?', size=(20,1)), sg.Input(key='finalizada', size=(20,1))],
        [sg.Button('Confirmar')]
    ]

    janelaInsAtiv = sg.Window('Insere Atividade', layoutInsAtiv)

    while True:
        eventos, valores = janelaInsAtiv.read()
        df2 = pd.read_excel("CaminhoPC\\Atividades.xlsx")
        if eventos == sg.WINDOW_CLOSED:
            break
        if eventos == 'Confirmar':
            rows_count = df2.count()['Nome da Atividade']
            i = int(rows_count)
            df2.loc[i, 'ID Projeto'] = int(valores['idProjetoAtiv'])
            df2.loc[i, 'Nome da Atividade'] = str(valores['nomeAtividade'])
            df2.loc[i, 'Data Inicio'] = str(valores['dataInicioAtiv'])
            df2.loc[i, 'Data de Fim'] = str(valores['dataFimAtiv'])
            df2.loc[i, 'Finalizada?'] = str(valores['finalizada'])
            df2.loc[::,'ID Projeto':].to_excel("CaminhoPC\\Atividades.xlsx")
            df2 = pd.read_excel("CaminhoPC\\Atividades.xlsx")
            janelaInsAtiv.close()

def alteraAtividade():
    sg.theme('Reddit')
    layoutAltAtiv = [
        [sg.Text('ID da Atividade', size=(20,1)), sg.Input(key='idAtiv', size=(20,1))],
        [sg.Text('ID do Projeto', size=(20,1)), sg.Input(key='idProjetoNovo', size=(20,1))],
        [sg.Text('Nome Atividade', size=(20,1)), sg.Input(key='novoNomeAtiv', size=(20,1))],
        [sg.Text('Data Inicial', size=(20,1)), sg.Input(key='dataInicioNovo', size=(20,1))],
        [sg.Text('Data Fim', size=(20,1)), sg.Input(key='dataFimNovo', size=(20,1))],
        [sg.Text('Atividade Finalizada?', size=(20,1)), sg.Input(key='finalizadaNovo', size=(20,1))],
        [sg.Button('Confirmar')]
    ]

    janelaAltAtiv = sg.Window('Altera Atividade', layoutAltAtiv)

    while True:
        eventos, valores = janelaAltAtiv.read()
        df2 = pd.read_excel("CaminhoPC\\Atividades.xlsx")
        if eventos == sg.WINDOW_CLOSED:
            break
        if eventos == 'Confirmar':
            rows_count = df2.count()['Nome da Atividade']
            i = int(rows_count)
            idAtiv = int(valores['idAtiv'])
            if idAtiv <= i - 1 and idAtiv >= 0:
                df2.loc[idAtiv, 'ID Projeto'] = int(valores['idProjetoNovo'])
                df2.loc[idAtiv, 'Nome da Atividade'] = str(valores['novoNomeAtiv'])
                df2.loc[idAtiv, 'Data Inicio'] = str(valores['dataInicioNovo'])
                df2.loc[idAtiv, 'Data de Fim'] = str(valores['dataFimNovo'])
                df2.loc[idAtiv, 'Finalizada?'] = str(valores['finalizadaNovo'])
                df2.loc[::,'ID Projeto':].to_excel("C:\\Users\\pedro\\music\\Python\\projetos2\\Atividades.xlsx")
                df2 = pd.read_excel("CaminhoPC\\Atividades.xlsx")
                janelaAltAtiv.close()
main()


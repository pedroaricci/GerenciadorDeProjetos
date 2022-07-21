# GerenciadorDeProjetos

## Introdução
Este projeto foi criado segundo o [Desafio](https://github.com/Artia/desafios-desevolvimento/blob/master/desafio-fullstack.md) para a vaga de estágio em desenvolvimento web do Grupo EUAX.

## Desafio
Você precisa criar um cadastro de projetos com a data de início e data final para a entrega, esse projeto pode ter 1 ou N atividades que também precisam ser cadastradas com as datas de início e data de fim. Após ter feito todos os cadastros precisamos saber quantos % dos projetos já temos finalizados e também se o projeto terá atrasos ou não. Para saber a % de andamento do projeto deve ser considerado o número de atividades finalizadas e quantidade de atividades ainda sem finalizar. Para saber se o projeto terá atraso considere a maior data final das atividades e compare com a data final do projeto, se for maior que a data final, o projeto terminará com atrasos. Abaixo segue exemplo das tabelas para cadastros.

## Funcionamento do Software
Criado em Python, foi utilizada as bibliotecas pandas e PySimpleGUI para que seja utilizado uma planilha como base de dados, podendo inserir e alterar projetos e também inserir e alterar atividades. Com a biblioteca pandas é possivel manipular as panilhas em forma de DataFrame e com o PySimpleGUI foi possível criar telas de interação do software.

## instruções para Iniciar
Primeiramente é necessário instalar as bibliotecas pandas e PySimpleGUI

* pip install pandas
* pip install PySimpleGUI

Após isso, onde está escrito "CaminhoPC\\Projetos.xlsx" ou "CaminhoPC\\Atividades.xlsx" favor trocar para o caminho de onde está salvos os arquivos xlsx indicado. Em seguida execute o gerenciador.py.

## Tecnologias
* Python

## Dificuldades
Após fazer o código em Python tentei transformar em um app Web, porém não consegui, por isso implantei telas para que seja possível manipular sem que seja através de terminal.

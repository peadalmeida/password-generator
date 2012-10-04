##Password-Generator
##Trabalho de Linguagens de Programação I

Implementar um programa em Python que gera senhas aleatórias e fáceis de
memorizar utilizando substantivos, adjetivos e números de, no maximo, 3 (três) 
digitos(0 a 100).
As senhas possuem tamanho fixo de 13 caracteres formatadas no seguinte padrão.

*Substantivo(5 caracteres) + Adjetivo(5 caracteres) + 
Número aleatório(3 caracteres)*

As senhas geradas são únicas e para facilitar memorização, o adjetivo concorda
em gênero com o substantivo.

##Grupo:

* Cássio Botaro
* Mônica Faria (contribuição)
* Pedro Augusto

##Professor: 
Bruno de Oliveira Schneider

##Dependências:

* Python 3 (`sudo apt-get install python3`) 
* Tkinter (`sudo apt-get install python3-tk`)


##Como utilizar:

1. Clone o repositório 

    `git clone git@github.com:augustopedro/Password-Generator.git`
    
2. Navegue até a pasta com conteúdo clonado

    `cd Password-Generator/`
    
3. Inicie o aplicativo  

    `python3 password_generator.py`

##FAQ:

1 **Programa abre,exibe erro e fecha.**

    R:Certifique que os arquivos listados abaixo estejam na pasta `arqs`
    e com permissão de leitura.A pasta arqs deve estar na mesma pasta
    do arquivo password_generator.py.
    Certifique também se as dependências estão satisfeitas.

* sub_mas.txt
* sub_fem.txt
* adj_mas.txt
* adj_fem.txt

2 **Adiconei novo adjetivo/substantivo e programa começou aparecer senha vazia
   esporadicamente.**

    R:Certifique que  o arquivo modificado não contenha linhas em branco 
    ao final.

3 **Programa não abre, e exibe erro dizendo não poder abrir arquivo de imagem.**

    R:Verifique a presença dos seguintes arquivos na pasta `imgs`:

* sair.gif
* senha.gif

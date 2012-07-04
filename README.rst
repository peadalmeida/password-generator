Password-Generator
==================

**Trabalho de Linguagens de Programação I -**
----------------------------------------------

Implementar um programa em Python que gere senhas aleatorias e faceis de memorizar utilizando substantivos, adjetivos e numeros
de, no maximo, 3 (três) digitos(0 a 100).
As senhas possuem tamanho fixo de 13 caracteres formatadas no seguinte padrão.

-Substantivo + Adjetivo + Número aleatório

As senhas geradas são únicas e para facilitar memorização, o adjetivo concorda em gênero com o substantivo.

**Grupo:**

* Cássio Botaro
* Pedro Augusto
* Mônica Faria 

**Professor:** Bruno de Oliveira Schneider

**Requisitos**

* Python 3
* Tkinter

**Como utilizar:**

1. Clone o repositório 
2. Navegue até a pasta com conteúdo clonado
3. Abra um terminal nesta pasta

.. sourcecode::bash
        $python3 controle.py

----

**FAQ:**

**1.Programa abre,exibe erro e fecha.**

R:Certifique de os arquivos listados abaixo estejam na pasta atual e com permissão de leitura.

* sub_mas.txt
* sub_fem.txt
* adj_mas.txt
* adj_fem.txt
* senhas_antigas.txt

**2.Programa não executa.** 
 
R:Certifique de que todos os pré-requisitos estejam satisfeitos.
Verifique se os arquivos abaixo estejam presentes.

* password_generator.py
* new_io.py


**3.Adiconei novo adjetivo\substantivo e programa começou aparecer senha vazia esporadicamente.**


R:Certifique que  o arquivo modificado não contenha linhas em branco ao final.

**4.Reiniciei sistema mas senhas ficaram salvas.**


R:Apague arquivo senhas_antigas.txt e crie um novo vazio.



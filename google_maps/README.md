# Raspagem de Dados de estabelecimentos comerciais no Google

Este Spyder faz a raspagem de algumas informações de estabelecimentos comerciais no Google Maps e salva estes dados em:

* Json
- CSV
+ XLSx


# Instruções


1) Python = Baixe e instale a partir de python.org

2) Instale as bibliotecas abaixo, Execute os seguintes comandos, um por um no CMD:

* pip install scrapy == 1.6
* pip install autopep8
* pip install pylint
* pip install selenium
* pip install scrapy-selenium
* pip install scrapy-xlsx

# Como usar



1) Execute no cmd o comando: 

```python
"Python gui_app.py"
```
2. O cmd irá questionar qual termo será usado na pesquisa, o que exatamente você quer pesquisar, digite e clique "enter":

```python
"Enter your search option : Restaurantes em São Paulo"
```
3. A interface irá solicitar que você escolha o Spyder a ser executado (você pode ter mais de um o/), selecione 1 deles, selecione o formato em que você quer salvar os dados: JSON, CSV, XLSx e selecione o local e o nome do arquivo a ser salvo.

4. Por fim, clique em "Execute"

5. O navegador irá se abrir e iniciar a pesquisa e a extração de dados.

# Observações:
1) É recomendável ter conexão de internet de alta velocidade antes da extração de dados.

2) Feche outros navegadores ou janelas antes de executar e deixe o PC concluir a estração de dados.
3) Dependendo do tamanho do conjunto de dados que ele encontrar, pode demorar alguns minutos para concluir a extração. 

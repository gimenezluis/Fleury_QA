# Teste automatizado - Fleury QA

<br>
# Ferramentas necessarias para rodar a aplicação.
PYCHARM
<br>
PYTHON 3.7
<br>
install: selenium
<br>
pip install behave
<br>
pip install allure-behave
<br>
chromedriver -na versao atual do navegador

# Comando para rodar aplicação:
<br>
behave -f allure_behave.formatter:AllureFormatter -o testes-report features/fleury_qa
<br>
testes configurados para rodar em headless

# Comando para gerar relatorio no servidor allure
<br>
allure serve C:\\Fleury_QA\testes-report
<br>

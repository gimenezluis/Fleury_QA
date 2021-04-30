#language:pt
Funcionalidade: Validar o Nome da unidade

  Contexto: Validar o nome da unidade que é exibida na tela, através do site Fleury
    Dado que esteja na tela principal do Fleury

  @cenario1
  Cenario: Validar carregamento pagina principal
    Quando estiver na home do Fleury
    Então o sistema deve exibir carregaento dos elementos em tela

  @cenario2
  Cenario: Validar nome da unidade
    Quando eu clicar em unidades
    E escolher entre 1 a 3 opçoes de facilidade
    E selecionar a unidade que aparecer em tela
    Então o sistema deve exibir o nome da unidade selecionada
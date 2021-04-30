# coding=utf-8
from behave import *

@given(u'que esteja na tela principal do Fleury')
def step_impl(context):
    context.driver.get(context.url)


@when(u'estiver na home do Fleury')
def step_impl(context):
    context.fleury.home_principal(context)


@then(u'o sistema deve exibir carregaento dos elementos em tela')
def step_impl(context):
    context.fleury.valida_carregamento_home(context)

#cenario2

@when(u'eu clicar em unidades')
def step_impl(context):
    context.fleury.clicar_unidades(context)


@when(u'escolher entre 1 a 3 opçoes de facilidade')
def step_impl(context):
    context.fleury.selecionar_opcao_facilidade(context)


@when(u'selecionar a unidade que aparecer em tela')
def step_impl(context):
    context.fleury.selecionar_unidade(context)


@then(u'o sistema deve exibir o nome da unidade selecionada')
def step_impl(context):
    context.fleury.validar_nome_unidade(context)

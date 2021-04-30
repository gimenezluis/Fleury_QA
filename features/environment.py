from selenium import webdriver
import shutil
import os

from features.pages.NavegacaoPage import NavegacaoPage


def before_all(context):
    # Configurações do driver
    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_argument("headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--test-type")
    chrome_options.add_argument("--disable-notifications")
    context.driver = webdriver.Chrome(chrome_options=chrome_options)

    # URL UTILIZAVEIS
    context.url = "https://www.fleury.com.br/"

    try:
        shutil.rmtree('testes-report')
    except:
        pass

    dir_json = './testes-report'
    os.makedirs(dir_json)

    context.fleury = NavegacaoPage(context.driver)


def after_all(context):
    context.driver.quit()

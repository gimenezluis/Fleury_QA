import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class NavegacaoPage:

    def __init__(self, driver):
        self.driver = driver
        self.waitShort = WebDriverWait(self.driver, 15)

        # Elementos da pagina
        self.logo = "logo"
        self.btn_unidades = "//*[@id='gatsby-focus-wrapper']/div[3]/div/div/div/div/div[16]"

        self.btn_filtro_facilidade = "//*[@id='checkoox-select-facilities']/div"

        self.btn_filtro_acessibilidade = ".checkbox-fieldcomponentstyle__CheckboxFieldStyled-sc-1mdajsk-0:nth-child(3) > .fa-check-square"

        self.btn_detelhe_unidade = "//*[@id='button-see-on-map-2-vila-mariana']/div"

        self.nome_unidade = "//*[@id='anchor-unit-cell-vila-mariana']/div[1]/div/div/div[3]/h3"

        self.nome_unidade_detalhe = "/html/body/div[2]/div/div[9]/div[2]/div/h1"

        # imagens de validação
        self.img_home = "report_images/validacao_carregament_home.png"
        self.img_validacao_unidade = "report_images/validacao_unidade.png"

    def home_principal(self, context):
        self.waitShort.until(EC.presence_of_element_located((By.ID, self.logo)))

    def valida_carregamento_home(self, context):
        try:
            self.waitShort.until(EC.presence_of_element_located((By.XPATH, self.btn_unidades)))
            time.sleep(0.2)
            self.driver.save_screenshot(self.img_home)
        except:
            self.driver.close

    def clicar_unidades(self, context):
        try:
            self.waitShort.until(EC.presence_of_element_located((By.XPATH, self.btn_unidades))).click()
        except:
            self.driver.save_screenshot("report_images/erro.png")

    def selecionar_opcao_facilidade(self, context):
        # clica filtro
        self.waitShort.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='checkoox-select-facilities']/div"))).click()

        # seleciona opcao filtro facilidade
        self.driver.find_element(By.CSS_SELECTOR, self.btn_filtro_acessibilidade).click()

    def selecionar_unidade(self, context):
        self.nome_unidade = self.driver.find_element(By.XPATH, self.nome_unidade).text

        self.driver.execute_script("window.scrollTo(0, 100)")
        self.waitShort.until(EC.presence_of_element_located((By.XPATH, self.btn_detelhe_unidade))).click()

    def validar_nome_unidade(self, context):
        time.sleep(0.5)
        self.waitShort.until(EC.presence_of_element_located((By.XPATH,"//*[@id='gatsby-focus-wrapper']/div[9]/div[3]/div/div[1]/div/div/div/img")))
        nome_unidade_detalhe = self.driver.find_element(By.XPATH, self.nome_unidade_detalhe).text
        try:
            assert self.nome_unidade == nome_unidade_detalhe
            self.driver.save_screenshot(self.img_validacao_unidade)
        except:
            self.driver.close()

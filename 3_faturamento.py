import sys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Recebe dados do app
usuario_ldap = sys.argv[1]
senha = sys.argv[2]

# Caminho dinâmico
base_user = os.path.expanduser("~")
pasta_destino = os.path.join(base_user, "Downloads", "GD", "3faturamento")

os.makedirs(pasta_destino, exist_ok=True)

# Configuração do Chrome
options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": pasta_destino,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=options)

# Força download na pasta correta
driver.execute_cdp_cmd(
    "Page.setDownloadBehavior",
    {"behavior": "allow", "downloadPath": pasta_destino}
)

wait = WebDriverWait(driver, 60)

# 🔥 FUNÇÃO FINAL (ignora downloads.htm e pega só Excel)
def esperar_download(pasta, timeout=180):
    tempo_inicial = time.time()

    arquivos_iniciais = set(os.listdir(pasta))

    print("Aguardando download do Excel...")

    while True:
        arquivos_atuais = set(os.listdir(pasta))
        novos_arquivos = arquivos_atuais - arquivos_iniciais

        # 🔥 pega só arquivos Excel
        novos_excel = [f for f in novos_arquivos if f.endswith(".xlsx")]

        if novos_excel:
            caminho = os.path.join(pasta, novos_excel[0])

            tamanho_anterior = -1
            while True:
                tamanho_atual = os.path.getsize(caminho)

                if tamanho_atual == tamanho_anterior:
                    return caminho

                tamanho_anterior = tamanho_atual
                time.sleep(1)

        if time.time() - tempo_inicial > timeout:
            raise Exception("Download do Excel não detectado")

        time.sleep(1)

try:
    driver.get("https://leroy.eu.qlikcloud.com/sense/app/d8c5f73b-c04c-4394-8efb-b6297681a6b8/sheet/b7de7e3c-0fa1-4237-8eb8-e7094f1bd955/state/analysis/hubUrl/%2Finsights%2Fhome")

    # Login
    wait.until(EC.presence_of_element_located((By.ID, "identifierInput"))).send_keys(usuario_ldap)
    driver.find_element(By.ID, "my_sign_on_button").click()

    wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys(senha)
    driver.find_element(By.ID, "signOnButton").click()

    # Espera objeto
    objeto = wait.until(EC.presence_of_element_located((
        By.XPATH,
        '//*[@id="34b6e2ea-8ef8-4693-b9d0-cdda683a9e1d-header-0"]'
    )))

    # Menu e download
    actions = ActionChains(driver)
    actions.context_click(objeto).perform()

    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Baixar')]"))).click()

    time.sleep(2)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Baixar')]"))).click()

    # Tempo pro Qlik iniciar o download
    time.sleep(5)

    # Espera download correto
    arquivo_baixado = esperar_download(pasta_destino)

    # Renomeia
    novo_nome = os.path.join(pasta_destino, "3faturamento.xlsx")

    if os.path.exists(novo_nome):
        os.remove(novo_nome)

    os.rename(arquivo_baixado, novo_nome)

    print("Download concluído com sucesso!")

except Exception as e:
    print("Erro no script:", e)

finally:
    driver.quit()
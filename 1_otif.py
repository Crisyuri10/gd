# import sys
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import os
# import shutil

# # Recebe LDAP e senha do app principal
# usuario_ldap = sys.argv[1]
# senha = sys.argv[2]

# pasta_download = r"C:\Users\51068683\Downloads"
# pasta_destino = r"C:\Users\51068683\Downloads\GD\1otif"

# driver = webdriver.Chrome()
# wait = WebDriverWait(driver, 60)

# try:
#     # Abre site
#     driver.get("https://leroy.eu.qlikcloud.com/sense/app/4031f242-6056-42ae-8c47-433f1d1dc022/sheet/49e3433b-41fe-4a83-a611-f518411a8c77/state/analysis/hubUrl//insights/home")

#     # Login
#     wait.until(EC.presence_of_element_located((By.ID, "identifierInput"))).send_keys(usuario_ldap)
#     driver.find_element(By.ID, "my_sign_on_button").click()

#     wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys(senha)
#     driver.find_element(By.ID, "signOnButton").click()

#     # Espera objeto aparecer
#     objeto = wait.until(EC.presence_of_element_located((
#         By.XPATH,
#         '//*[@id="9354d040-9fdd-4342-852f-3026427bfc47-header-0"]/div/div/div'
#     )))

#     # Menu direito e baixar
#     actions = ActionChains(driver)
#     actions.context_click(objeto).perform()

#     botao_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Baixar')]")))
#     botao_menu.click()

#     time.sleep(3)

#     botao_download = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Baixar')]")))
#     botao_download.click()

#     # Espera download
#     time.sleep(80)

#     # Pega arquivo mais recente
#     arquivos = [os.path.join(pasta_download, f) for f in os.listdir(pasta_download) if not f.endswith(".crdownload")]
#     arquivo_recente = max(arquivos, key=os.path.getctime)

#     # Move e renomeia
#     novo_caminho = os.path.join(pasta_destino, "fOTIF.xlsx")
#     shutil.move(arquivo_recente, novo_caminho)

#     print("Download concluído, arquivo renomeado e movido!")

# except Exception as e:
#     print("Erro no script:", e)
# finally:
#     driver.quit()





# import sys
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import os

# # Recebe dados do app
# usuario_ldap = sys.argv[1]
# senha = sys.argv[2]

# # Caminho dinâmico
# base_user = os.path.expanduser("~")
# pasta_destino = os.path.join(base_user, "Downloads", "GD", "1otif")

# os.makedirs(pasta_destino, exist_ok=True)

# # 🔥 CONFIGURAÇÃO DO CHROME PARA BAIXAR DIRETO NA PASTA
# options = webdriver.ChromeOptions()
# prefs = {
#     "download.default_directory": pasta_destino,
#     "download.prompt_for_download": False,
#     "download.directory_upgrade": True,
#     "safebrowsing.enabled": True
# }
# options.add_experimental_option("prefs", prefs)

# driver = webdriver.Chrome(options=options)
# wait = WebDriverWait(driver, 60)

# # 🔍 Função para esperar download terminar
# def esperar_download(pasta, timeout=120):
#     tempo_inicial = time.time()

#     while True:
#         arquivos = os.listdir(pasta)

#         # Se ainda existe arquivo temporário (.crdownload), continua esperando
#         if any(arq.endswith(".crdownload") for arq in arquivos):
#             if time.time() - tempo_inicial > timeout:
#                 raise Exception("Timeout no download")
#             time.sleep(2)
#             continue

#         # Se já existe Excel, terminou
#         arquivos_excel = [f for f in arquivos if f.endswith(".xlsx")]
#         if arquivos_excel:
#             return max(
#                 [os.path.join(pasta, f) for f in arquivos_excel],
#                 key=os.path.getctime
#             )

#         time.sleep(2)

# try:
#     driver.get("https://leroy.eu.qlikcloud.com/sense/app/4031f242-6056-42ae-8c47-433f1d1dc022/sheet/49e3433b-41fe-4a83-a611-f518411a8c77/state/analysis/hubUrl//insights/home")

#     # Login
#     wait.until(EC.presence_of_element_located((By.ID, "identifierInput"))).send_keys(usuario_ldap)
#     driver.find_element(By.ID, "my_sign_on_button").click()

#     wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys(senha)
#     driver.find_element(By.ID, "signOnButton").click()

#     # Espera objeto
#     objeto = wait.until(EC.presence_of_element_located((
#         By.XPATH,
#         '//*[@id="9354d040-9fdd-4342-852f-3026427bfc47-header-0"]/div/div/div'
#     )))

#     # Menu e download
#     actions = ActionChains(driver)
#     actions.context_click(objeto).perform()

#     wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Baixar')]"))).click()

#     time.sleep(2)

#     wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Baixar')]"))).click()

#     # 🔥 Espera inteligente
#     arquivo_baixado = esperar_download(pasta_destino)

#     # Renomeia
#     novo_nome = os.path.join(pasta_destino, "1otif.xlsx")

#     if os.path.exists(novo_nome):
#         os.remove(novo_nome)

#     os.rename(arquivo_baixado, novo_nome)

#     print("Download concluído com sucesso!")

# except Exception as e:
#     print("Erro no script:", e)

# finally:
#     driver.quit()



# import sys
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import os

# # Recebe dados do app
# usuario_ldap = sys.argv[1]
# senha = sys.argv[2]

# # Caminho dinâmico
# base_user = os.path.expanduser("~")
# pasta_destino = os.path.join(base_user, "Downloads", "GD", "1otif")

# os.makedirs(pasta_destino, exist_ok=True)

# # Configuração do Chrome
# options = webdriver.ChromeOptions()
# prefs = {
#     "download.default_directory": pasta_destino,
#     "download.prompt_for_download": False,
#     "download.directory_upgrade": True,
#     "safebrowsing.enabled": True
# }
# options.add_experimental_option("prefs", prefs)

# driver = webdriver.Chrome(options=options)
# wait = WebDriverWait(driver, 60)

# # 🔥 Função ajustada (espera iniciar + finalizar download)
# def esperar_download(pasta, timeout=180):
#     tempo_inicial = time.time()
#     tamanho_anterior = -1

#     print("Aguardando download iniciar...")

#     # Espera o download começar
#     while True:
#         arquivos = os.listdir(pasta)

#         if any(arq.endswith(".crdownload") or arq.endswith(".xlsx") for arq in arquivos):
#             break

#         if time.time() - tempo_inicial > timeout:
#             raise Exception("Download não iniciou")

#         time.sleep(1)

#     print("Download iniciado, aguardando finalizar...")

#     # Espera o download terminar
#     while True:
#         arquivos = [f for f in os.listdir(pasta) if f.endswith(".xlsx") or f.endswith(".crdownload")]

#         if arquivos:
#             caminho = os.path.join(pasta, arquivos[0])

#             if caminho.endswith(".crdownload"):
#                 time.sleep(2)
#                 continue

#             tamanho_atual = os.path.getsize(caminho)

#             if tamanho_atual == tamanho_anterior:
#                 return caminho

#             tamanho_anterior = tamanho_atual

#         if time.time() - tempo_inicial > timeout:
#             raise Exception("Timeout no download")

#         time.sleep(2)

# try:
#     driver.get("https://leroy.eu.qlikcloud.com/sense/app/4031f242-6056-42ae-8c47-433f1d1dc022/sheet/49e3433b-41fe-4a83-a611-f518411a8c77/state/analysis/hubUrl//insights/home")

#     # Login
#     wait.until(EC.presence_of_element_located((By.ID, "identifierInput"))).send_keys(usuario_ldap)
#     driver.find_element(By.ID, "my_sign_on_button").click()

#     wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys(senha)
#     driver.find_element(By.ID, "signOnButton").click()

#     # Espera objeto
#     objeto = wait.until(EC.presence_of_element_located((
#         By.XPATH,
#         '//*[@id="9354d040-9fdd-4342-852f-3026427bfc47-header-0"]/div/div/div'
#     )))

#     # Menu e download
#     actions = ActionChains(driver)
#     actions.context_click(objeto).perform()

#     wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Baixar')]"))).click()

#     time.sleep(2)

#     wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Baixar')]"))).click()

#     # 🔥 pequeno tempo pro Qlik iniciar o download
#     time.sleep(5)

#     # Espera download corretamente
#     arquivo_baixado = esperar_download(pasta_destino)

#     # Renomeia
#     novo_nome = os.path.join(pasta_destino, "1otif.xlsx")

#     if os.path.exists(novo_nome):
#         os.remove(novo_nome)

#     os.rename(arquivo_baixado, novo_nome)

#     print("Download concluído com sucesso!")

# except Exception as e:
#     print("Erro no script:", e)

# finally:
#     driver.quit()

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
pasta_destino = os.path.join(base_user, "Downloads", "GD", "1otif")

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
    driver.get("https://leroy.eu.qlikcloud.com/sense/app/4031f242-6056-42ae-8c47-433f1d1dc022/sheet/49e3433b-41fe-4a83-a611-f518411a8c77/state/analysis/hubUrl//insights/home")

    # Login
    wait.until(EC.presence_of_element_located((By.ID, "identifierInput"))).send_keys(usuario_ldap)
    driver.find_element(By.ID, "my_sign_on_button").click()

    wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys(senha)
    driver.find_element(By.ID, "signOnButton").click()

    # Espera objeto
    objeto = wait.until(EC.presence_of_element_located((
        By.XPATH,
        '//*[@id="9354d040-9fdd-4342-852f-3026427bfc47-header-0"]/div/div/div'
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
    novo_nome = os.path.join(pasta_destino, "1otif.xlsx")

    if os.path.exists(novo_nome):
        os.remove(novo_nome)

    os.rename(arquivo_baixado, novo_nome)

    print("Download concluído com sucesso!")

except Exception as e:
    print("Erro no script:", e)

finally:
    driver.quit()
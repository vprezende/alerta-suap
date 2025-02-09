import os
from bs4 import BeautifulSoup
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Carregar variáveis de ambiente
load_dotenv()
    
class Suap:

  def __init__(self):
    
    # Acessando as variáveis de ambiente
    suap_login_url = os.getenv("SUAP_LOGIN_URL")
    suap_bolsas_url = os.getenv("SUAP_BOLSAS_URL")
    suap_username = os.getenv("USER")
    suap_password = os.getenv("PASSWORD")

    # Fazendo login

    options = Options()
    options.add_argument("--headless")

    browser = webdriver.Chrome(options=options)

    browser.get(url=suap_login_url)
    sleep(1)

    username = browser.find_element(by=By.ID, value="id_username")
    username.send_keys(suap_username)
    sleep(1)

    password = browser.find_element(by=By.ID, value="id_password")
    password.send_keys(suap_password)
    sleep(1)

    buttonLogin = browser.find_element(by=By.CLASS_NAME, value="submit-row")
    buttonLogin.click()
    sleep(2)

    # Acessando as página das bolsas

    browser.get(url=suap_bolsas_url)

    sleep(3)

    # retornando apenas as bolsas do Campus Bom Jesus do Itabapoana

    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")

    # Lista para armazenar as bolsas encontradas

    bolsas = []

    # Procurando as tabelas

    for table in soup.find_all("table"):
      for row in table.find_all("tr")[1:]:  # Ignora a primeira linha
        cols = row.find_all("td")

        if not cols or len(cols) < 4:  # Verifica se tem pelo menos 4 colunas
          continue

        campus = cols[3].get_text(strip=True)  # 4ª coluna (índice 3)

        # Adicionando informações das bolsas na lista de dicionários
        if campus == "DGCBJESUS":
          bolsas.append({
            "Projeto": cols[1].get_text(strip=True),
            "Coordenador": cols[2].get_text(strip=True),
            "Campus": cols[3].get_text(strip=True)
          })
          
    # Exibindo as bolsas
    for bolsa in bolsas:
      print(f"Projeto: {bolsa["Projeto"]}")
      print(f"Coordenador: {bolsa["Coordenador"]}")
      print(f"Campus: {bolsa["Campus"]}")
      print("-" * 50)

def main():

  Suap()

if __name__ == "__main__":
  main()
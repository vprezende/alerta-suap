# bibliotecas para gerenciar e acessar as variáveis de ambiente
import os
from dotenv import load_dotenv

# bibliotecas para fazer a automação para acessar o site
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# biblioteca para extração dos dados
from bs4 import BeautifulSoup

# modulo da biblioteca time para dar um delay
from time import sleep

import requests

# Carregar variáveis de ambiente
load_dotenv()
    
class Suap:

  def __init__(self):
    
    # Acessando as variáveis de ambiente
    suap_login_url = os.getenv("SUAP_LOGIN_URL")
    suap_bolsas_url = os.getenv("SUAP_BOLSAS_URL")

    suap_username = os.getenv("SUAP_USERNAME")
    suap_password = os.getenv("SUAP_PASSWORD")

    receiver_email = os.getenv("EMAIL")
    
    mailtrap_token = os.getenv("MAILTRAP_API_TOKEN")

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

    # Acessando a página das bolsas

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

    # Configurações para enviar o e-mail
    send_email_url = f"https://send.api.mailtrap.io/api/send"

    # Exibindo as bolsas
    for bolsa in bolsas:

      email_body = f"""
      <p>Projeto: {bolsa["Projeto"]}</p>
      <p>Coordenador: {bolsa["Coordenador"]}</p>
      <p>Campus: {bolsa["Campus"]}</p>
      <br>
      """

      payload = {
        "from": {
            "email": "notificacoes@demomailtrap.com",
            "name": "Notificador de Bolsas"
        },
        "to": [
            {
                "email": receiver_email,
                "name": "Destinatário"
            }
        ],
        "subject": "Bolsas Disponíveis",
        "html": email_body + f"<br> Acesse esse link para se inscrever nas bolsas: {suap_bolsas_url}"
      }

    # Enviar o e-mail
    headers = {
        "Authorization": f"Bearer {mailtrap_token}",
        "Content-Type": "application/json"
    }

    response = requests.post(send_email_url, json=payload, headers=headers)

    print("\n", end="")

    if response.status_code == 200:
      print(f"E-mail enviado para {receiver_email}")
    else:
      print(f"Erro ao enviar e-mail: {response.text}")

    print("\n", end="")

def main():

  Suap()

if __name__ == "__main__":
  main()

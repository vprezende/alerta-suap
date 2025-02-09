import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Carregar variáveis de ambiente
load_dotenv()

class DeepSeek:

  def __init__(self):

    self.deepseek_api = os.getenv('DEEPSEEK_API')

    # Definindo comportamento geral para o deepseek

    self.history = [
      {
        "role": "system", 
        "content": "Você vai responder todas as perguntas em português"
      }
    ]

    self.headers = {
      "Content-Type": "application/json"
    }

  def ask(self, prompt):


    # adicionando mensagem do usuário ao histórico de conversas
    self.history.append({"role": "user", "content": prompt})

    data = {
      "model": "deepseek-r1:8b",
      "messages": self.history,
      "stream": False
    }

    response = requests.post(self.deepseek_api, json=data, headers=self.headers)

    if response.status_code == 200:
      response_model = response.json()["message"]["content"]

      # adicionando resposta do deepseek ao histórico de conversas
      self.history.append({"role": "assistant", "content": response_model})
      
      soup = BeautifulSoup(response_model, 'html.parser')

      think_tags = soup.find('think')
    
      for tag in think_tags:
        tag.decompose()

      clean_response = soup.get_text().strip()

      return clean_response
    else:
      return f"Erro: {response.status_code} - {response.text}"
    
class Suap:

  def __init__(self):
    
    # Acessando as variáveis de ambiente
    suap_login_url = os.getenv("SUAP_LOGIN_URL")
    suap_bolsas_url = os.getenv("SUAP_BOLSAS_URL")
    suap_username = os.getenv("USER")
    suap_password = os.getenv("PASSWORD")

    deepseek = DeepSeek()

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

    tables = soup.find_all("table")

def main():

  Suap()

if __name__ == "__main__":
  main()
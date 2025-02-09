import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

# Carregando as variáveis de ambiente do arquivo .env
load_dotenv()

class load_config:
  
  def __init__(self):

    # Acessando as variáveis de ambiente
    self.suap_url = os.getenv('SUAP_URL')
    self.user = os.getenv('USER')
    self.password = os.getenv('PASSWORD')

class deepseek:

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

  def response(self, prompt):


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
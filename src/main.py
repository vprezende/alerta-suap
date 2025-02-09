from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
from time import sleep

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
    
    bolsas_dgcbjesus = []

    # Encontrar todas as tabelas na página
    for table in soup.find_all('table'):
      # Encontrar todas as linhas da tabela
      rows = table.find_all('tr')
    
      # Pular tabelas vazias
      if not rows:
        continue
    
      # Encontrar cabeçalhos (se existirem)
      headers = [th.get_text(strip=True) for th in rows[0].find_all('th')]
    
      # Determinar o índice da coluna "Campus"
      try:
        campus_index = headers.index("Campus")
      except ValueError:
        # Se não encontrar cabeçalhos, tentar adivinhar a estrutura
        campus_index = None  # Ajuste este índice conforme necessário
    
      # Iterar pelas linhas da tabela (começando da segunda linha se houver cabeçalhos)
      for row in rows[1:]:
        cols = row.find_all('td')
        
        # Validar se há colunas suficientes
        if not cols:
          continue
            
        # Se não encontramos cabeçalho, assumir que a quarta coluna é o campus
        current_index = campus_index if campus_index is not None else 3  # Ajuste este índice
        
        try:
          campus = cols[current_index].get_text(strip=True)
        except IndexError:
          continue
        
        # Verificar se o campus é o desejado
        if campus == "DGCBJESUS":
          # Extrair todos os dados da linha
          dados_bolsa = {}
          for i, col in enumerate(cols):
            header_name = headers[i] if i < len(headers) else f'Coluna_{i+1}'
            dados_bolsa[header_name] = col.get_text(strip=True)
          bolsas_dgcbjesus.append(dados_bolsa)

    for bolsa in bolsas_dgcbjesus:
      print(f"Projeto: {bolsa["Projeto"]}")
      print(f"Coordenador: {bolsa["Coordenador"]}")
      print(f"Campus: {bolsa["Campus"]}")
      print("-" * 50)

def main():

  Suap()

if __name__ == "__main__":
  main()
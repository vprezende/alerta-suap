import os
from dotenv import load_dotenv

class load_config:
  
  def __init__(self):

    # Carregando as variáveis de ambiente do arquivo .env
    load_dotenv()

    # Acessando as variáveis de ambiente
    self.deepseek_api = os.getenv('DEEPSEEK_API')
    self.suap_url = os.getenv('SUAP_URL')
    self.user = os.getenv('USER')
    self.password = os.getenv('PASSWORD')
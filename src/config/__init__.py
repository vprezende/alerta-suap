import os
from dotenv import load_dotenv

class load_config:
  
  def __init__(self):

    # Carrega as variáveis de ambiente do arquivo .env
    load_dotenv()

    # Acessa as variáveis de ambiente
    self.deepseek_api = os.getenv('DEEPSEEK_API')
    self.suap_url = os.getenv('SUAP_URL')
    self.user = os.getenv('USER')
    self.password = os.getenv('PASSWORD')
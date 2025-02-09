from config import *

def main():
  config = Config()
  print(f"API do DeepSeek: {config.deepseek_api}")
  print(f"url do suap: {config.suap_url}")
  print(f"usuário: {config.user}")
  print(f"Senha: {config.password}")

if __name__ == "__main__":
  main()
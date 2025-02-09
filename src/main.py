import config

def main():
  env_config = config.load_config()
  print(f"API do DeepSeek: {env_config.deepseek_api}")
  print(f"url do suap: {env_config.suap_url}")
  print(f"usuário: {env_config.user}")
  print(f"Senha: {env_config.password}")

if __name__ == "__main__":
  main()
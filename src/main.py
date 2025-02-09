import config

def main():
  setup = config.load_config()
  deepseek = config.deepseek()

  print(deepseek.response("oi, tudo bem?"))


if __name__ == "__main__":
  main()
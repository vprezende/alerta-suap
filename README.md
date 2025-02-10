<h1 align="center">Alerta Suap</h1>

Este projeto tem como objetivo automatizar o envio de notificações por e-mail sobre os prazos de inscrição em bolsas publicadas no sistema SUAP 🎓💻 e também as etapas dos processos seletivos 🔔📅. O sistema monitora atualizações no SUAP e envia alertas por e-mail para os usuários interessados 📬.

## Funcionalidades

- 🚨 Monitoramento automático de novas publicações de bolsas no SUAP.
- 📅 Envio de notificações por e-mail sobre prazos de inscrição.
- ⏳ Envio de alertas sobre etapas e status dos processos seletivos.

## Tecnologias Utilizadas

- 🐍 Python 3.13.2
- 🔑 `dotenv` para gerenciar configurações sensíveis como senhas.
- 🖥️ `os` para acessar variáveis de ambiente no sistema operacional.
- 🧑‍💻 `bs4` para fazer parsing de conteúdo HTML e facilitar a extração de dados de páginas web.
- 🖥️ `selenium` para automação de navegação na web e interação com o SUAP.
- ⏳ `time` para gerenciar intervalos de tempo e pausas no processo de monitoramento.

## Requisitos

Antes de rodar o projeto, instale as dependências:

```bash
pip3 install -r requirements.txt
```

Além disso, crie um arquivo `.env` para armazenar suas credenciais de usuário e outras configurações sensíveis:

```ini
SUAP_LOGIN_URL=https://suap.iff.edu.br/accounts/login
SUAP_BOLSAS_URL=https://suap.iff.edu.br/sisep/adicionar_candidatura_participacao/
USER=seu_usuario
PASSWORD=sua_senha
```

## Como Usar

1. Clone o repositório para sua máquina local:

    ```bash
    git clone https://github.com/vprezende/alerta-bolsa-suap.git
    ```
    
    ```bash
    cd alerta-bolsa-suap
    ```

2. Instale as dependências necessárias:

    ```bash
    pip3 install -r requirements.txt
    ```

3. Execute o script principal para começar a monitorar os prazos e etapas:

    ```bash
    cd src
    ```
    
    ```bash
    python3 main.py
    ```

O sistema irá começar a monitorar o SUAP e enviar e-mails com as atualizações conforme necessário.

## Contribuições

Sinta-se à vontade para contribuir com melhorias, novas funcionalidades ou correções de bugs 🚀. Para isso, faça um fork deste repositório, crie uma branch com sua modificação e envie um pull request. 💡

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes. 📝

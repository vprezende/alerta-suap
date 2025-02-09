# 📧 Sistema de Notificação sobre Prazos e Etapas de Inscrição em Bolsas no SUAP

Este projeto tem como objetivo automatizar o envio de notificações por e-mail sobre os prazos de inscrição em bolsas publicadas no sistema SUAP 🎓💻 e também as etapas dos processos seletivos 🔔📅. O sistema monitora atualizações no SUAP e envia alertas por e-mail para os usuários interessados 📬.

## Funcionalidades

- 🚨 Monitoramento automático de novas publicações de bolsas no SUAP.
- 📅 Envio de notificações por e-mail sobre prazos de inscrição.
- ⏳ Envio de alertas sobre etapas e status dos processos seletivos.

## Tecnologias Utilizadas

- 🐍 Python 3.13.2
- 🔑 `dotenv` para gerenciar configurações sensíveis como credenciais de e-mail.

## Requisitos

Antes de rodar o projeto, instale as dependências:

```bash
pip3 install -r requirements.txt
```

Além disso, crie um arquivo `.env` para armazenar suas credenciais de usuário e outras configurações sensíveis:

```ini
DEEPSEEK_API=deepseek_api_url
SUAP_URL=https://suap.iff.edu.br/accounts/login
USER=seu_usuario
PASSWORD=sua_senha
```

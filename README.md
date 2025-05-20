# 🎬 YouTube Video Uploader com Flask

Este projeto é uma aplicação Flask que permite fazer **upload de vídeos para o YouTube** via **YouTube Data API v3**, com suporte para **agendamento**, **privacidade** e marcação de conteúdo para crianças.

## ✨ Funcionalidades

- Autenticação via OAuth2 com Google
- Upload de vídeos diretamente do navegador
- Suporte a título, descrição, privacidade e agendamento
- Agendamento com conversão automática de horário local para UTC
- Suporte a vídeos marcados como “Feito para crianças”

---

## ⚙️ Pré-requisitos

- Conta Google com acesso ao YouTube
- Python 3.8+
- Projeto criado no [Google Cloud Console](https://console.cloud.google.com/)
- Biblioteca `pip install` das dependências listadas em `requirements.txt`

---

## 🔐 Configuração do Google Cloud (OAuth2)
### 1. Criar projeto no Google Cloud
Acesse: [Google Cloud Resource Manager](https://console.cloud.google.com/cloud-resource-manager)
- Crie um novo projeto
- Selecione o projeto e vá em APIs & Services

### 2. Configurar OAuth Consent Screen
- Vá em OAuth consent screen
- App Name: Nome da sua aplicação
- User support email: Seu e-mail
- Audience: External
- Informações de contato: Seu e-mail
- Marque os termos de uso e clique em Create

### 3. Criar credenciais OAuth
- Acesse: [Credenciais](https://console.cloud.google.com/apis/credentials)
- Clique em Create Credentials → OAuth client ID
- Application Type: Web Application
- Nome: (Ex: Web client youtube)
- Authorized redirect URIs:
```bash
http://localhost:5000/oauth2callback
http://127.0.0.1:5000/oauth2callback
```

### 4. Adicionar escopo à tela de consentimento
- Vá em OAuth consent screen
- Clique em Edit App
- Vá em Scopes → Add or Remove Scopes
- Adicione: https://www.googleapis.com/auth/youtube.upload
- Clique em Update → Save and Continue

### 5. Baixar client_secret.json
- Vá em Credentials
- Clique no seu OAuth 2.0 Client ID
- Clique em Download JSON para baixar client_secret.json
- Coloque o arquivo na raiz do projeto

### 6. Adicionar e-mail de testador
- Vá em OAuth consent screen → aba Test Users
- Adicione o e-mail Google que será usado para fazer login

### 7. Ativar YouTube API
- Vá em APIs & Services → Library
- Pesquise YouTube Data API v3
- Clique em Enable

---

## 🚀 Executar a aplicação
Para executar a aplicação, use o seguinte comando:
```bash
python main.py
```

Acesse em seu navegador:
```bash
http://localhost:5000
```

---

## 🛠️ Tecnologias Usadas
- Python + Flask
- Google OAuth 2.0
- YouTube Data API v3
- Bootstrap (para o front-end, opcional)

---

## ❗ Dicas e Observações
- O vídeo agendado precisa estar como private, e será tornado público na data definida.
- Se ocorrer erro como redirect_uri_mismatch, verifique os URIs autorizados.
- A aplicação roda localmente em ambiente de teste. Para produção, usar HTTPS e domínio validado.

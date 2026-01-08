# 🎥 yt-video-summary

Ferramenta em Python para **transcrever e resumir vídeos do YouTube automaticamente** usando inteligência artificial.

O projeto baixa o áudio do vídeo, transcreve com **Whisper** e gera um resumo claro e objetivo utilizando a **Google Gemini API**.

---

## 🚀 Funcionalidades
- Download automático do áudio de vídeos do YouTube
- Transcrição de áudio para texto
- Geração de resumos com IA
- Uso seguro de variáveis de ambiente (`.env`)

---

## 🛠️ Tecnologias Utilizadas
- Python
- yt-dlp
- OpenAI Whisper
- Google Gemini API

---

## ⚙️ Instalação

### 1. Clone o repositório
~~~bash
git clone git@github.com:henriqueelj/yt-video-summary.git
cd yt-video-summary
~~~

### 2. Crie e ative um ambiente virtual
~~~bash
python -m venv .venv
source .venv/bin/activate
~~~

### 3. Instale as dependências
~~~bash
pip install -r requirements.txt
~~~

### 4. Configure a API Key
Crie um arquivo `.env` na raiz do projeto:
~~~env
GOOGLE_API_KEY=SUA_API_KEY_AQUI
~~~

---

## ▶️ Como Usar
Execute o script e cole o link do vídeo quando solicitado:

~~~bash
python main.py
~~~

---

## 📌 Observações
- O diretório `.venv` não é versionado
- Arquivos de áudio são gerados localmente
- Projeto com foco educacional e automação


import os
from dotenv import load_dotenv
import whisper
import yt_dlp
from google import genai


load_dotenv()


api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise RuntimeError("GOOGLE_API_KEY não encontrada no .env")

client = genai.Client(api_key=api_key)


def baixar_audio(url):
    ydl_opts = {
        "format": "bestaudio",
        "outtmpl": "audio.%(ext)s",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
            }
        ],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return "audio.mp3"


def transcrever_audio(audio_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result["text"]


def resumir_video(texto):
    prompt = f"""
Você é um assistente especialista em resumir vídeos do YouTube de forma clara, fiel e útil.

Tarefa:
A partir da transcrição abaixo, gere um resumo completo e bem estruturado do vídeo.

Regras obrigatórias:
- Preserve apenas as ideias realmente importantes.
- Remova repetições, enrolação, cumprimentos e partes irrelevantes.
- Não invente informações que não estejam na transcrição.
- Use linguagem clara, objetiva e direta.
- Escreva como se estivesse explicando para alguém que não viu o vídeo.


Transcrição:

{texto}
"""

    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
)


    return response.text


if __name__ == "__main__":
    link = input("Cole o link do YouTube: ")

    audio = baixar_audio(link)
    texto = transcrever_audio(audio)
    resumo = resumir_video(texto)

    print("\n===== RESUMO =====\n")
    print(resumo)
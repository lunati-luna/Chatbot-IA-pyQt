import os
import google.generativeai as genai
from dotenv import load_dotenv

# Carga las variables del archivo .env
load_dotenv()

# Lee la clave de forma segura
API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

def preguntar_a_gemini(mensaje):
    try:
        model = genai.GenerativeModel('gemini-flash-latest') 
        response = model.generate_content(mensaje)
        return response.text
    except Exception as e:
        if "429" in str(e):
            return "IA: Estoy un poco cansada (límite de mensajes). Esperá un minuto y volvé a intentar."
        return f"Error: {e}"
import os
from urllib.parse import urlencode, urlparse

from flask import Flask, render_template

app = Flask(__name__)

# Configuración general
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "clave-local-desarrollo")

BRAND_NAME = os.getenv("BRAND_NAME", "Apasionado por la Tecnología CCU").strip()

CONTACT_EMAIL = os.getenv("CONTACT_EMAIL", "ccuempresadesistemas@gmail.com").strip()

WHATSAPP_URL = os.getenv("WHATSAPP_URL", "https://wa.me/573206652771").strip()

# Validar el enlace de WhatsApp
parsed_url = urlparse(WHATSAPP_URL)

if parsed_url.scheme != "https" or parsed_url.netloc != "wa.me":
    raise ValueError("El enlace de WhatsApp no es válido.")

# Mensaje automático para los clientes
whatsapp_message = urlencode(
    {"text": "Hola, estoy interesado en conocer sus servicios tecnológicos."}
)

WHATSAPP_LINK = f"{WHATSAPP_URL}?{whatsapp_message}"


@app.get("/")
def home():
    return render_template(
        "index.html",
        brand_name=BRAND_NAME,
        contact_email=CONTACT_EMAIL,
        whatsapp_link=WHATSAPP_LINK,
    )


if __name__ == "__main__":
    debug_mode = os.getenv("FLASK_DEBUG", "0") == "1"

    app.run(host="127.0.0.1", port=5000, debug=debug_mode)

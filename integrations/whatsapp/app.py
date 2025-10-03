from fastapi import FastAPI, Request, Response
import uvicorn
import os
from dotenv import load_dotenv  # PRUEBA: Carga las variables de entorno desde el archivo .env

load_dotenv()   # PRUEBA: Carga las variables de entorno desde el archivo .env

app = FastAPI()

@app.get("/webhook/whatsapp/vali")
async def validate_webhook(request: Request):
    hub_mode = request.query_params.get("hub.mode")
    hub_challenge = request.query_params.get('hub.challenge')
    hub_verify_token = request.query_params.get('hub.verify_token')
    VERIFY_TOKEN_WHATSAPP = os.getenv('VERIFY_TOKEN_WHATSAPP')
    if hub_verify_token == VERIFY_TOKEN_WHATSAPP and hub_mode == "subscribe":
        return int(hub_challenge)
    return Response(status_code=403)

@app.post("/webhook/whatsapp/vali")
async def handle_webhook(request: Request):
    body = await request.json()
    print('MENSAJE ENTRANTE\n', body)
    return Response(status_code=200)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
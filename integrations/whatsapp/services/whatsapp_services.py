from fastapi import Request, Response
import os
from models.whatsapp_message_received import WhatsappPayload


async def service_validate_webhook(request: Request):
    hub_mode = request.query_params.get("hub.mode")
    hub_challenge = request.query_params.get('hub.challenge')
    hub_verify_token = request.query_params.get('hub.verify_token')
    VERIFY_TOKEN_WHATSAPP = os.getenv('VERIFY_TOKEN_WHATSAPP')
    if hub_verify_token == VERIFY_TOKEN_WHATSAPP and hub_mode == "subscribe":
        return int(hub_challenge)
    return Response(status_code=403)

async def service_handle_webhook(request: Request):
    message_user = WhatsappPayload(**(await request.json()))
    print('MENSAJE ENTRANTE\n', message_user.entry[0].changes[0].value.messages[0].text.body) # Prueba para ver resultado
    return Response(status_code=200)
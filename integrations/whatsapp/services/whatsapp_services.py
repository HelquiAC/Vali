import asyncio
from fastapi import Request, Response
import os
from integrations.whatsapp.models.whatsapp_message_received import WhatsappPayload
from integrations.whatsapp.clients.request_customers_microservice import validate_id_user
from integrations.whatsapp.clients.request_conversations_microservice  import send_message_whatsapp_to_conversations_microservice
from dotenv import load_dotenv  # PRUEBA: Carga las variables de entorno desde el archivo .env


load_dotenv('integrations/whatsapp/config/.env')   # PRUEBA: Carga las variables de entorno desde el archivo .env

async def service_validate_webhook(request: Request): 
    if request.query_params.get('hub.verify_token') == os.getenv('VERIFY_TOKEN_WHATSAPP') and request.query_params.get("hub.mode") == "subscribe":
        return int(request.query_params.get('hub.challenge'))
    return Response(status_code=403)

async def service_handle_webhook(request: Request):
    message_user = WhatsappPayload(**(await request.json()))
    asyncio.create_task(process_webhook_background(message_user))    
    return Response(status_code=200)

async def process_webhook_background(message_user: WhatsappPayload):
    id_user = await validate_id_user(message_user.entry[0].changes[0].value.contacts[0].wa_id)
    if id_user:
        await send_message_whatsapp_to_conversations_microservice(message_user)      
    else:
        pass # no se puede concretar la operacion
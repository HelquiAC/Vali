from fastapi import APIRouter, Request
from services.whatsapp_services import service_handle_webhook, service_validate_webhook
from dotenv import load_dotenv  # PRUEBA: Carga las variables de entorno desde el archivo .env


load_dotenv('config/.env')   # PRUEBA: Carga las variables de entorno desde el archivo .env

router = APIRouter(prefix="/webhook/whatsapp/vali")

@router.get("")
async def validate_webhook(request: Request):
    await service_validate_webhook(request)    

@router.post("")
async def handle_webhook(request: Request):
    await service_handle_webhook(request)    
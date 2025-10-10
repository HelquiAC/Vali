from fastapi import APIRouter, Request
from integrations.whatsapp.services.whatsapp_services import service_handle_webhook, service_validate_webhook


router = APIRouter(prefix='/webhook/whatsapp/vali')

@router.get('')
async def validate_webhook(request: Request):
    return await service_validate_webhook(request)    

@router.post('')
async def handle_webhook(request: Request):
    return await service_handle_webhook(request)    
from fastapi import APIRouter, Request

router = APIRouter(prefix='/microservice/conversations')

@router.post('/get_message_whatsapp')
async def get_message_whatsapp(request: Request):
    data = await request.json()
    response = data.get('message')
    return {"respuesta": f"recibidooooO: {response}"}
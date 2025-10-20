import httpx
from integrations.whatsapp.app.logger import get_logger
from integrations.whatsapp.models.whatsapp_message_received import WhatsappPayload


logger = get_logger('whatsapp.clients.request_conversations_microservice')

async def send_message_whatsapp_to_conversations_microservice(message_user: WhatsappPayload):
    logger.info('Execute fun send_message_whatsapp_to_conversations_microservice')
    async with httpx.AsyncClient() as client:
        try:
            message = message_user.entry[0].changes[0].value.messages[0].text.body
            logger.info('send POST request to conversations microservice')
            response = await client.post(
                f'http://127.0.0.1:8001/microservice/conversations/get_message_whatsapp',
                json={"message": message})
            if response.status_code == 200:
                logger.info(f'status_code: {response.status_code}, response conversations microservice: {response.json()}')
            else:
                logger.error(f'status_code: {response.status_code}, response conversations microservice: {response.text}')
            return None #Aqui podemos usar para generar otro request
        except httpx.RequestError as e:
            logger.error('httpx.RequestError when sending message to conversations microservice', e)        
        except Exception as e:
            logger.error('Exception when sending message to conversations microservice', e)           
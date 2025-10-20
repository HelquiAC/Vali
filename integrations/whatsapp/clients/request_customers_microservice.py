import pstats
from integrations.whatsapp.app.logger import get_logger
import httpx


logger = get_logger('whatsapp.clients.request_customers_microservice')

async def validate_id_user(from_: str):
    logger.info('Execute fun validate_id_user')
    async with httpx.AsyncClient() as client:
        try:
            logger.info('send POST request to customers microservice')
            response = await client.post(f'http://127.0.0.1:8002/microservice/customers/validate_user', json={"from": from_})
            if response.status_code == 200:
                logger.info(f'status_code: {response.status_code}, response customers microservice: {response.json()}')
                return response.json()['id_user']
            else:
                logger.error(f'status_code: {response.status_code}, response customers microservice: {response.text}')
        except httpx.RequestError as e:
            logger.error('httpx.RequestError when sending message to customers microservice', e)
        except Exception as e:
            logger.error('Exception when sending message to customers microservice', e)
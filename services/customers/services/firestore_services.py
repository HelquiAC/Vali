from google.cloud import firestore
import asyncio
from google.api_core.exceptions import GoogleAPIError
from services.customers.app.logger import get_logger
from dotenv import load_dotenv


load_dotenv('services/customers/config/.env')

logger = get_logger('customers.services.firestore_services')

db = firestore.Client()

async def find_id_user_with_phone_BD(from_: str):
    logger.info('Execute fun find_id_user_with_phone_BD')
    return await asyncio.to_thread(find_id_user_with_phone_sync, from_)

def find_id_user_with_phone_sync(from_: str):
    logger.info('Execute fun find_id_user_with_phone_sync')
    try:
        docs = db.collection("Users").where("phone", "==", from_).limit(1).get()
        if not docs:
            logger.info('the "id_user" was not found')
            return None
        return str(docs[0].id)
    except GoogleAPIError as e:
        logger.error(f'GoogleAPIError when search "id_user": {e}')
        return None
    except Exception as e:
        logger.error(f'Exception when search "id_user": {e}')
        return None    

async def create_id_user_BD(id_user: str, from_: str):
    logger.info('Execute fun create_id_user_BD')
    return await asyncio.to_thread(create_id_user_sync, id_user, from_)

def create_id_user_sync(id_user: str,from_: str):
    logger.info('Execute fun create_id_user_sync')
    try:
        db.collection("Users").document(id_user).set({"phone": from_})
        return True
    except GoogleAPIError as e:
        logger.error(f'GoogleAPIError when create "id_user": {e}')
        return False
    except Exception as e:
        logger.error(f'Exception when create "id_user": {e}')  
        return False
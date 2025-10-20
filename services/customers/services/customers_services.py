from fastapi import Request, HTTPException
from services.customers.services.firestore_services import find_id_user_with_phone_BD, create_id_user_BD
from services.customers.utils.utils_customers import create_id_user
from services.customers.app.logger import get_logger


logger = get_logger('customers.services.customers_services')

async def service_validate_user(request: Request):
    logger.info('Execute fun service_validate_user')
    data = await request.json()
    from_ = data.get('from')
    if not from_:
        logger.error('fastapi.HTTPException: Invalid request: the "from_" field (WhatsApp number) is missing or empty') 
        raise HTTPException(status_code=400, detail={"error": "Missing 'from'"})
    logger.info('the "from_" field was received')
    id_user = await find_id_user_with_phone_BD(from_)
    if not id_user:
        logger.info('the "id_user" field is missing or empty')
        id_user = create_id_user()
        result_create_id_user = await create_id_user_BD(id_user, from_)
        if not result_create_id_user:
            logger.error('fastapi.HTTPException: Failed operation: error when create "id_user" in firestore') 
            raise HTTPException(status_code=500, detail={"error": "Failed to create 'id_user' in firestore"})
    logger.info('sending the "id_user" field')
    return {"id_user": id_user}
from fastapi import APIRouter, Request, HTTPException
from services.customers.app import logger
from services.customers.services.customers_services import service_validate_user
from services.customers.app.logger import get_logger
from fastapi import HTTPException


router = APIRouter(prefix='/microservice/customers')

logger = get_logger('customers.routes.customers_routes')

@router.post('/validate_user')
async def validate_user(request: Request):
    logger.info('Execute route validate_user')
    try:
        return await service_validate_user(request)
    except HTTPException as e:
        logger.error(f'fastapi.HTTPException when execute route validate_user: {e}')
        raise e
    except Exception as e:
        logger.error(f'Exception when execute route validate_user: {e}')
        raise HTTPException(status_code=400, detail={"error": "Endpoint error: validate_user"})
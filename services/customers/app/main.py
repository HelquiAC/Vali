from fastapi import FastAPI
import uvicorn
from services.customers.routes.customers_routes import router
from services.customers.app.logger import get_logger


logger = get_logger('customers.app.main')

app = FastAPI()
logger.info('starting customers microservice')

app.include_router(router)
logger.info('Routes of customers microservice loading successfully')

if __name__ == '__main__':
    logger.info('Excecute uvicorn server in 0.0.0.0:8002 in customers microservice')
    uvicorn.run(app, host='0.0.0.0', port=8002)


from fastapi import FastAPI
import uvicorn
from integrations.whatsapp.routes.whatsapp_routes import router
from integrations.whatsapp.app.logger import get_logger


logger = get_logger('whatsapp.app.main')

app = FastAPI()
logger.info('starting whatsapp microservice')

app.include_router(router)
logger.info('Routes of whatsapp microservice loading successfully')

if __name__ == '__main__':
    logger.info('Excecute uvicorn server in 0.0.0.0:8000 in whatsapp microservice')
    uvicorn.run(app, host='0.0.0.0', port=8000)
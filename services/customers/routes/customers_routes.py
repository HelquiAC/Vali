from fastapi import APIRouter, Request


router = APIRouter(prefix='/microservice/customers')

@router.post('/')
async def create_user(request: Request):
    pass
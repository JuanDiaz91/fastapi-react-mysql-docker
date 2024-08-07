import os
from fastapi import FastAPI
from database import engine
from db.db_models import Base
from dotenv import load_dotenv
from services.user_router import router as user_router

load_dotenv()
PORT = os.getenv('PORT')
API_URL = os.getenv('API_URL')


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_router, prefix='/api')



@app.get('/ping')
async def ping():
    return {'ping': 'pong'}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host=API_URL, port=int(PORT))

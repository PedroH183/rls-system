from fastapi import FastAPI
from populate import populate
from database import engine, Base
from contextlib import asynccontextmanager


@asynccontextmanager
async def insertingData(app : FastAPI):
    Base.metadata.create_all(bind=engine)

    try:
        populate()
    except Exception as e: 
        print(e)
        pass
    yield


app = FastAPI(title="RlsSystemTest", lifespan=insertingData)

@app.get("/")
async def root():
    return {"message": "Hello World"}
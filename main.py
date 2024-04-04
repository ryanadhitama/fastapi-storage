from fastapi import FastAPI
from router.upload import router as upload_router

app = FastAPI()

app.include_router(upload_router)

@app.get("/")
def root():
    return {"ping": "pong!"}

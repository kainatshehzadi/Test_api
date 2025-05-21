from fastapi import FastAPI
from fastapi.responses import JSONResponse
from mangum import Mangum

fastapi_app = FastAPI()

@fastapi_app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on Vercel!"}

@fastapi_app.get("/test")
def test():
    return JSONResponse({"status": "Success", "info": "This is a test endpoint"})

app = Mangum(fastapi_app) 

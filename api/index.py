from fastapi import FastAPI
from fastapi.responses import JSONResponse
from mangum import Mangum

app = FastAPI()

def handler(request):
    return {
        "statusCode": 200,
        "body": "Hello from Vercel!"
    }

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on Vercel!"}

@app.get("/test")
def test():
    return JSONResponse({"status": "Success", "info": "This is a test endpoint"})

handler = Mangum(app)
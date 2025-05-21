from fastapi import FastAPI
from fastapi.responses import JSONResponse
from mangum import Mangum

app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on Vercel!"}

@app.get("/test")
def test():
    return JSONResponse({"status": "Success", "info": "This is a test endpoint"})

handler = Mangum(app)
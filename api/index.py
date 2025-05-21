from fastapi import FastAPI
from fastapi.responses import JSONResponse
from mangum import Mangum
from http.server import BaseHTTPRequestHandler
app = FastAPI()


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from Python on Vercel!")

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on Vercel!"}

@app.get("/test")
def test():
    return JSONResponse({"status": "Success", "info": "This is a test endpoint"})

handler = Mangum(app)
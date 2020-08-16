from fastapi import FastAPI
from mangum import Mangum


app = FastAPI()


@app.get("/")
def ping():
    return "pong"

handler = Mangum(app)

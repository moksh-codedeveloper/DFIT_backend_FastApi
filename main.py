# import cloudinary.api
from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get("/")
async def home():
    return {"message" : "Hello how are you i am from India"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
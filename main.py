# import cloudinary.api
from fastapi import FastAPI
import uvicorn
from config.cloudinary_model import CloudinaryModel


app = FastAPI()

@app.get("/")
async def home():
    return {"message" : "Hello how are you i am from India"}


@app.get("/scan/{user_id}")
async def url_fetcher(user_id:str):
    if not user_id :
        raise Exception("please pass the user id as it is or else the server will be stopped")
    url = CloudinaryModel(user_id=user_id)
    image_url = url.fetch_url_cloudinary()
    return {"url" : image_url}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
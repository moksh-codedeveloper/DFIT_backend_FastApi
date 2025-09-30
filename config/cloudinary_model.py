import cloudinary
import os 
from dotenv import load_dotenv
load_dotenv()
from cloudinary.api import resources
CLOUD_NAME = os.getenv("CLOUDINARY_CLOUD_NAME")
CLOUD_API_KEY = os.getenv("CLOUDINARY_API_KEY")
CLOUD_API_SECRET = os.getenv("CLOUDINARY_API_SECRET")

cloudinary.config(
    cloud_name = CLOUD_NAME,
    api_key = CLOUD_API_KEY,
    api_secret = CLOUD_API_SECRET
)

class CloudinaryModel:
    def __init__(self, user_id):
        self.user_id = user_id
    
    def fetch_url_cloudinary(self):
        result = resources(type = "upload", prefix=f'uploads/{self.user_id}', max_result=15)
        for i,item in enumerate(result.get("resources",[])):
            print("hello i am inside the loop and see this baby")
            url = item["secure_url"]
            return {"url" : url}
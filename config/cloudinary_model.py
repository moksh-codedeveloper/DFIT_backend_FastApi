import numpy as np
import cloudinary
from io import BytesIO
import os, requests
from PIL import Image 
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
            print(url)
            return url
        
class ImageNumpyArrayExtracter:
    def __init__(self, url):
        self.url = url
        self.img_arr = np.array([])
    
    def image_numpy_extractor(self):
        try:
            result = requests.get(self.url, stream=True)
            resp = Image.open(BytesIO(result.content))
            self.img_arr = np.array(resp)
            return {
                "message" : "Your array has been extracted here it is",
                "shape" : self.img_arr.shape,
                "dtype" : self.img_arr.dtype
            }
        except:
          print('An exception occurred in the server due to the network or the url is not proper')
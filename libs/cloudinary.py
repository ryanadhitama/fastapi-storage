import cloudinary
import os 
from cloudinary.uploader import upload
from fastapi import HTTPException, status, UploadFile
from dotenv import load_dotenv
from typing import List

load_dotenv()

cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET")
)

async def upload_image(image: UploadFile):
    try:
        print(image)
        upload_result = upload(image.file)
        file_url = upload_result['secure_url']
        return file_url
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error uploading images: {e}")
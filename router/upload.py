from fastapi import APIRouter, HTTPException, status, UploadFile
from typing import List
from libs.cloudinary import upload_image

router = APIRouter()

@router.post("/upload")
async def handle_upload(image: UploadFile):
    try:
        url = await upload_image(image)
        return {
            "data": {
                "url": url
            }
        }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e)
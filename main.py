from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from utils.image_analysis import analyze_chart
from fastapi.staticfiles import StaticFiles
import shutil
import os

app = FastAPI()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.post("/upload/")
async def upload_chart(file: UploadFile = File(...)):
    file_location = f"{UPLOAD_FOLDER}/{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = analyze_chart(file_location)
    return JSONResponse(content=result)

app.mount("/", StaticFiles(directory="static", html=True), name="static")
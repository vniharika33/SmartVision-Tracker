from fastapi import FastAPI, UploadFile, File
import shutil
import os

from backend.tracker import process_video

# -----------------------------------
# FASTAPI APP
# -----------------------------------
app = FastAPI()

# -----------------------------------
# HOME
# -----------------------------------
@app.get("/")
def home():

    return {
        "message": "AI Smart Surveillance API Running"
    }

# -----------------------------------
# TRACK VIDEO API
# -----------------------------------
@app.post("/track-video")
async def track_video(
    file: UploadFile = File(...)
):

    # Save uploaded video
    input_path = f"videos/{file.filename}"

    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Output path
    output_path = f"outputs/output_{file.filename}"

    # Process video
    process_video(
        input_path,
        output_path
    )

    return {
        "message": "Video processed successfully",
        "output_video": output_path
    }
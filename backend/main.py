# uvicorn main:app
# uvicorn main:app --reload

# Main Imports
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai

# custom function imports
from functions.openai_requests import convert_audio_to_text

# initiate app
app = FastAPI()


# CORS - Origins
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:4173",
    "http://localhost:4174",
    "http://localhost:3000",
]


# CORS - Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Check Health
@app.get("/health")
async def check_health():
    return  {"message": "healthy"}

# Get audio
@app.get("/post-audio-get/")
async def get_audio(file: UploadFile = File(...)):
    
    # Get saved audio
    audio_input = open("voice.mp3", "rb")
    print("test")
    # Decode audio
    message_decoded = convert_audio_to_text(audio_input)
    
    print(message_decoded)

    return "Done"



from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Mount the static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# ELEVENLABS CREDENTIALS (from .env)
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
ELEVENLABS_AGENT_ID = os.getenv("ELEVENLABS_AGENT_ID")


# Endpoint: Get Signed URL for frontend-initiated WebSocket connection
@app.get("/api/get-signed-url")
def get_signed_url(agent_id: str = None):
    if not agent_id:
        agent_id = ELEVENLABS_AGENT_ID

    url = f"https://api.elevenlabs.io/v1/convai/conversation/get_signed_url?agent_id={agent_id}"
    headers = {"xi-api-key": ELEVENLABS_API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    return JSONResponse(
        content={"error": response.text}, status_code=response.status_code
    )


@app.get("/")
async def read_root():
    return FileResponse("static/index.html")


@app.get("/manifest.json")
async def get_manifest():
    return FileResponse("manifest.json")


@app.get("/color.png")
async def get_color_icon():
    # Placeholder: In a real app, serve an actual image
    return FileResponse("color.png")


@app.get("/outline.png")
async def get_outline_icon():
    # Placeholder: In a real app, serve an actual image
    return FileResponse("outline.png")

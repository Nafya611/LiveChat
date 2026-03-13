# FastAPI Voice Processing Service

This service receives an audio file, forwards it to an n8n workflow, and returns the processed result.

## Setup

1.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

2.  **Configure Environment:**

    Update the `N8N_URL` variable in `main.py` with your actual n8n webhook URL.

    ```python
    N8N_URL = "https://YOUR_N8N_WEBHOOK_URL"
    ```

## Running the Application

Run the server using `uvicorn`:

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## API Usage

**Endpoint:** `POST /voice`

**Body:** `multipart/form-data` with a file field named `audio`.

**Example using curl:**

```bash
curl -X POST "http://127.0.0.1:8000/voice" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "audio=@path/to/your/audio.wav"
```

# Kara Voice Chat for Microsoft Teams

A real-time, full-duplex voice chat application powered by **ElevenLabs Conversational AI**, designed to run seamlessly inside **Microsoft Teams**.

## Features

- **Real-time Voice Conversation**: Low-latency voice interaction using ElevenLabs WebSockets.
- **Natural VAD (Voice Activity Detection)**: Automatically detects when you stop speaking.
- **Microsoft Teams Integration**:
  - Automatically detects the logged-in user's name via the Teams SDK.
  - Sends a "silent" introduction to the AI so it greets the user by name.
  - Standard Teams App Manifest included.
- **Modern UI**: Clean, ChatGPT-style interface with real-time text transcription and audio visualization.
- **Secure Authentication**: Backend signatures prevent exposing API keys on the client.

## Tech Stack

- **Frontend**: Vanilla JavaScript, WebSocket, Microsoft Teams SDK.
- **Backend**: Python 3.11, FastAPI.
- **AI**: ElevenLabs Conversational AI (custom agent linked to n8n).
- **Deployment**: Docker, Render.

## Prerequisites

1.  **ElevenLabs Account**: You need an Agent ID and API Key.
2.  **Microsoft Teams**: Permission to upload custom apps (sideloading).

## Setup & Running Locally

1.  **Clone the repository**:
    ```bash
    git clone <repo-url>
    cd Livechat
    ```

2.  **Environment Variables**:
    Create a `.env` file in the root directory:
    ```env
    ELEVENLABS_API_KEY=your_api_key_here
    ELEVENLABS_AGENT_ID=your_agent_id_here
    ```

3.  **Run with Docker Compose**:
    ```bash
    docker compose up --build -d
    ```
    The app will be available at `http://localhost:8000`.

## Deployment

This app is configured for deployment on platforms like **Render**, **Railway**, or **Azure Web Apps**.

1.  **Deploy the code** to your provider.
2.  **Set Environment Variables** in your provider's dashboard (`ELEVENLABS_API_KEY`, `ELEVENLABS_AGENT_ID`).
3.  **Note your Production URL** (e.g., `https://your-app.onrender.com`).

## Microsoft Teams Integration

To add this app to Microsoft Teams:

### 1. Configure the Manifest
Ensure `manifest.json` points to your deployed URL.
- Replace `https://livechat-c8k0.onrender.com` with your actual URL in:
  - `developer.websiteUrl`
  - `staticTabs[0].contentUrl`
  - `validDomains`

### 2. Create the App Package
**IMPORTANT:** The zip file must contain the following files at the **root** level (not inside a subfolder):
1.  `manifest.json`
2.  `color.png`
3.  `outline.png`

Name it e.g., `kara-teams-app.zip`.

### 3. Sideload into Teams
1.  Open **Microsoft Teams**.
2.  Go to **Apps** > **Manage your apps**.
3.  Select **Upload an app** -> **Upload a custom app**.
4.  Select your `.zip` file.
5.  Click **Add**.

### 4. Personalization
The app uses the `microsoftTeams.app.getContext()` method to fetch the user's name. It secretly sends this to the AI at the start of the conversation:
> *"Hi, my name is [User Name]."*
This prompts the AI to greet the user personally without any manual configuration.

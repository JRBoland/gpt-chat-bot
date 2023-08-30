import requests
from decouple import config

ELEVEN_LABS_API_KEY = config("ELEVEN_LABS_API_KEY")

# Eleven labs
# Convert Text to speech
def convert_text_to_speech(message):
    
    # Define data (body of req)
    body = {
        "text": message,
        "voice_settings": {
            "stability": 0,
            "similarity_boost": 0,
        }
    }

    # Define voice
    # voice_daniel = "onwK4e9ZLuTAKqWW03F9"
    voice_ryan = "wViXBPUzp2ZZixB1xQuM"
    # voice_fin = "D38z5RcWu1voky8WS1ja"

    # Constructing headers and endpoint
    headers = { "xi-api-key": ELEVEN_LABS_API_KEY, "Content-Type": "application/json", "accept": "audio/mpeg" }
    endpoint = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_ryan}"

    # Send request
    try: 
        response = requests.post(endpoint, json=body, headers=headers)

    except Exception as e:
        return
    
    # Handle response
    if response.status_code == 200: 
        return response.content
    else:
        return
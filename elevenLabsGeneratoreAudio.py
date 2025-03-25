import requests
import os
import apiKeysManager


def getApiKey():
    return apiKeysManager.getApiKey(os.environ["ELEVEN_LABS_API_KEY"])


def getVoiceId():
    return os.environ["VOICE_ID"]


def getVoiceOutputFilePath():
    return f"{os.getcwd()}\\{os.environ["VOICE_OUTPUT_FILE_PATH"]}"


def getVociDisponibili():

    url = "https://api.elevenlabs.io/v1/voices"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "xi-api-key": getApiKey(),
    }

    response = requests.get(url, headers=headers)

    if not str(response.status_code).startswith("2"):
        errore = response.json()
        print(f"Si è verificato un errore: {errore}")
        raise errore

    data = response.json()

    return data


def convertTextToAudio(testo: str):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{getVoiceId()}"

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": getApiKey(),
    }

    data = {
        "text": testo,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {"speed": 1.09, "stability": 0.6, "similarity_boost": 0.8},
    }

    response = requests.post(url, headers=headers, json=data)

    if not str(response.status_code).startswith("2"):
        errore = response.json()
        print(f"Si è verificato un errore: {errore}")
        raise errore

    CHUNK_SIZE = 1024
    path = getVoiceOutputFilePath()

    with open(path, "wb") as file:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                file.write(chunk)

    return path

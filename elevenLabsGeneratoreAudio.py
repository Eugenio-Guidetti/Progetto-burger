import os
import apiKeysManager
import requests
import util


def getApiKey():
    return apiKeysManager.getApiKey(os.environ["ELEVEN_LABS_API_KEY"])


def getVociDisponibili():

    url = "https://api.elevenlabs.io/v2/voices?include_total_count=true"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "xi-api-key": getApiKey(),
    }

    response = requests.get(url, headers=headers)

    if not str(response.status_code).startswith("2"):
        errore = response.json()
        print(f"Si è verificato un errore: {errore}")
        raise Exception(errore)

    data = response.json()

    return data


def convertiTestoVoce(testo: str):
    
    if util.getIdVoceSelezionata() == "":
        raise Exception("Nessuna voce selezionata")

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{util.getIdVoceSelezionata()}"

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": getApiKey(),
    }

    data = {
        "text": testo,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {"speed": 1, "stability": 0.6, "similarity_boost": 0.85},
    }

    response = requests.post(url, headers=headers, json=data)

    if not str(response.status_code).startswith("2"):
        errore = response.json()
        raise Exception(errore)

    if not os.path.exists(f"{util.getOutputFolder()}"):
        os.makedirs(util.getOutputFolder())

    CHUNK_SIZE = 1024
    voceOutputFilePath = util.getVoceOutputFilePath()

    with open(voceOutputFilePath, "wb") as file:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                file.write(chunk)

    return voceOutputFilePath

import os
import elevenLabsGeneratoreAudio
import glob
import random
import mediaEditor
import dotenv


def getInputFilesDir():
    return f"{os.getcwd()}\\{os.environ["INPUT_FILES_DIR"]}"


def getInputFilePath():
    return f"{getInputFilesDir()}\\{getInputFileName()}"


def getInputFileName():
    return os.environ["TESTO_SELEZIONATO"]


def getOutputFolder():
    return f"{os.getcwd()}\\out\\{str.removesuffix(getInputFileName(), ".txt")}"


def getVoceOutputFilePath():
    return f"{os.getcwd()}\\out\\{str.removesuffix(getInputFileName(), ".txt")}\\{os.environ["VOICE_OUTPUT_FILE_NAME"]}"


def getVoceSelezionata():
    return os.environ["VOCE_SELEZIONATA"]


def getMusicaFilePath():
    return f"{os.getcwd()}\\{os.environ["MUSICA_PATH"]}"


def getAudioOutputFilePath():
    return f"{os.getcwd()}\\out\\{str.removesuffix(getInputFileName(), ".txt")}\\{os.environ["AUDIO_OUTPUT_FILE_NAME"]}"


def getVideosDir():
    return f"{os.getcwd()}\\{os.environ["STOCK_VIDEOS_DIR"]}"


def getVideoOutputFilePath():
    return f"{os.getcwd()}\\out\\{str.removesuffix(getInputFileName(), ".txt")}\\{os.environ["VIDEO_OUTPUT_FILE_NAME"]}"


def getTesto():
    return open(getInputFilePath(), "r").read()


def selezionaTesto():
    testi = glob.glob(f"{getInputFilesDir()}\\*.txt")

    if len(testi) == 0:
        print("Nessun testo disponibile")
        return

    print("\nTesti disponibili:")
    for i in range(len(testi)):
        testo = testi[i]
        print(f" {i}) {testo}")

    try:
        scelta = input("Scegli un'opzione: ")
    except KeyboardInterrupt:
        print("\nNessun testo selezionato")
        return

    try:
        scelta = int(scelta)
    except:
        print("Input non valido")
        return

    try:
        os.environ["TESTO_SELEZIONATO"] = str.removeprefix(
            testi[scelta], f"{getInputFilesDir()}\\"
        )

    except:
        print("Scelta non valida")
        return

    dotenv.set_key(
        dotenv.find_dotenv(), "TESTO_SELEZIONATO", os.environ["TESTO_SELEZIONATO"]
    )


def mostraTestoSelezionato():
    try:
        print(f'\nTesto selezionato: \n"{getTesto()}"')
    except:
        print(f"Testo {getInputFilePath()} non disponibile, seleziona un altro testo")


def selezionaVoce():

    data = elevenLabsGeneratoreAudio.getVociDisponibili()

    max = -1
    for voice in data["voices"]:
        if len(voice["name"]) > max:
            max = len(voice["name"])

    print("\nVoci disponibili:")
    for i in range(len(data["voices"])):
        voice = data["voices"][i]
        print(
            f' {i}) Nome: "{voice["name"]}"{ " " * (max - len(voice["name"]))}  id: "{voice["voice_id"]}"'
        )

    try:
        scelta = input("Scegli un'opzione: ")
    except KeyboardInterrupt:
        print("\nNessuna voce selezionata")
        return

    try:
        scelta = int(scelta)
    except:
        print("Input non valido")
        return

    try:
        os.environ["VOCE_SELEZIONATA"] = data["voices"][scelta]
    except:
        print("Scelta non valida")
        return

    dotenv.set_key(
        dotenv.find_dotenv(), "VOCE_SELEZIONATA", os.environ["VOCE_SELEZIONATA"]
    )


def mostraVoceSelezionata():
    print(f"\nVoce selezionata: {getVoceSelezionata()}")


def convertiTestoVoce():
    try:
        out = elevenLabsGeneratoreAudio.convertiTestoVoce(getTesto())
        print(f"File creato: {out}")

    except Exception as e:
        print(f"Errore: {e}")


def scegliVideoCasuale():
    videos = glob.glob(f"{getVideosDir()}\\*.mp4")

    if len(videos) == 0:
        raise Exception("Nessun video trovato")

    return videos[random.randint(0, len(videos) - 1)]


def unisciVoceMusica():
    try:
        out = mediaEditor.unisciVoceMusica(getVoceOutputFilePath(), getMusicaFilePath())
        print(f"File creato: {out}")

    except Exception as e:
        print(f"Errore: {e}")


def unisciAudioVideo():

    try:
        out = mediaEditor.unisciAudioVideo(
            getAudioOutputFilePath(), scegliVideoCasuale()
        )
        print(f"File creato: {out}")

    except Exception as e:
        print(f"Errore: {e}")

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


def getNomeVoceSelezionata():
    return os.environ["NOME_VOCE_SELEZIONATA"]


def getIdVoceSelezionata():
    return os.environ["ID_VOCE_SELEZIONATA"]


def getMusicaFilePath():
    return f"{os.getcwd()}\\{os.environ["MUSICA_PATH"]}"


def getAudioOutputFilePath():
    return f"{os.getcwd()}\\out\\{str.removesuffix(getInputFileName(), ".txt")}\\{os.environ["AUDIO_OUTPUT_FILE_NAME"]}"


def getVideosDir():
    return f"{os.getcwd()}\\{os.environ["STOCK_VIDEOS_DIR"]}"


def getVideoOutputFilePath():
    return f"{os.getcwd()}\\out\\{str.removesuffix(getInputFileName(), ".txt")}\\{os.environ["VIDEO_OUTPUT_FILE_NAME"]}"


def getTesto():
    try:
        return open(getInputFilePath(), "r").read()
    except FileNotFoundError:
        raise Exception("Il testo selezionato non è disponibile")


def selezionaTesto():
    if not os.path.exists(getInputFilesDir()):
        os.mkdir(getInputFilesDir())
        print("Nessun testo disponibile")
        return
    
    testi = glob.glob(f"{getInputFilesDir()}\\*.txt")

    if len(testi) == 0:
        print("Nessun testo disponibile")
        return

    print("Testi disponibili:")
    for i in range(len(testi)):
        testo = testi[i]
        print(f" {i + 1})\t{testo}")

    while True:
        try:
            scelta = input("Scegli un'opzione: ")
        except KeyboardInterrupt:
            os.environ["TESTO_SELEZIONATO"] = ""
            print("\nNessun testo selezionato")

        else:
            try:
                scelta = int(scelta) - 1
            except:
                print("Input non valido")
                continue

            try:
                if scelta < 0 or scelta >= len(testi):
                    raise Exception("Scelta non valida")

                os.environ["TESTO_SELEZIONATO"] = str.removeprefix(
                    testi[scelta], f"{getInputFilesDir()}\\"
                )

            except:
                print("Scelta non valida")
                continue

        dotenv.set_key(
            dotenv.find_dotenv(), "TESTO_SELEZIONATO", os.environ["TESTO_SELEZIONATO"]
        )
        print("")
        return


def mostraTestoSelezionato():
    try:
        print(f'Testo selezionato "{getInputFileName()}": \n"{getTesto()}"')
    except:
        print(f'Testo "{getInputFilePath()}" non disponibile, seleziona un altro testo')


def selezionaVoce():

    data = elevenLabsGeneratoreAudio.getVociDisponibili()

    if len(data["voices"]) == 0:
        print("Nessuna voce disponibile")
        return

    max = -1
    for voice in data["voices"]:
        if len(voice["name"]) > max:
            max = len(voice["name"])

    print("Voci disponibili:")
    for i in range(len(data["voices"])):
        voice = data["voices"][i]
        print(
            f' {i + 1})\tNome: "{voice["name"]}"{ " " * (max - len(voice["name"]))}  id: "{voice["voice_id"]}"'
        )

    while True:
        try:
            scelta = input("Scegli un'opzione: ")
        except KeyboardInterrupt:
            os.environ["ID_VOCE_SELEZIONATA"] = ""
            os.environ["NOME_VOCE_SELEZIONATA"] = "Nessuna voce selezionata"
            print("\nNessuna voce selezionata")

        else:
            try:
                scelta = int(scelta) - 1
            except:
                print("Input non valido")
                continue

            try:
                if scelta < 0 or scelta >= len(data["voices"]):
                    raise Exception("Scelta non valida")

                os.environ["ID_VOCE_SELEZIONATA"] = data["voices"][scelta]["voice_id"]
                os.environ["NOME_VOCE_SELEZIONATA"] = data["voices"][scelta]["name"]

            except:
                print("Scelta non valida")
                continue

        dotenv.set_key(
            dotenv.find_dotenv(),
            "ID_VOCE_SELEZIONATA",
            os.environ["ID_VOCE_SELEZIONATA"],
        )
        dotenv.set_key(
            dotenv.find_dotenv(),
            "NOME_VOCE_SELEZIONATA",
            os.environ["NOME_VOCE_SELEZIONATA"],
        )

        print("")
        return


def mostraVoceSelezionata():
    print(
        f'Voce selezionata: "{getNomeVoceSelezionata()}"; Id: "{getIdVoceSelezionata()}"'
    )


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

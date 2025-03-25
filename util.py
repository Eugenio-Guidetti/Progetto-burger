import os
import elevenLabsGeneratoreAudio


def mostraMenu():

    print("\n --- Opzioni: ---\n")
    print(" 0) Esci")
    print(" 1) Mostra testo selezionato")
    print(" 2) Elenca voci disponibili")
    print(" 3) Genera audio")

    while True:
        try:
            scelta = input("Scegli un'opzione: ")
        except KeyboardInterrupt:
            return 0

        try:
            return int(scelta)
        except:
            print("Input non valido")


def getOutputFilePath():
    return f"{os.getcwd()}\\{os.environ["OUTUT_FILE_PATH"]}"


def getInputFilePath():
    return f"{os.getcwd()}\\{os.environ["INPUT_FILE_PATH"]}"


def getTesto():
    return open(getInputFilePath(), "r").read()


def mostraTesto():
    print(f'Testo selezionato: \n"{getTesto()}"')


def mostraVociDisponibili():

    data = elevenLabsGeneratoreAudio.getVociDisponibili()

    max = -1
    for voice in data["voices"]:
        if len(voice["name"]) > max:
            max = len(voice["name"])

    print(" Voci disponibili:")
    for voice in data["voices"]:
        print(
            f' - Nome: "{voice["name"]}"{ " " * (max - len(voice["name"]))}  id: "{voice["voice_id"]}"'
        )


def generaAudio():
    try:
        out = elevenLabsGeneratoreAudio.convertTextToAudio(getTesto())
        print(f"File creato: {out}")

    except Exception as e:
        print(f"Errore: {e}")

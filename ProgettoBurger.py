from dotenv import load_dotenv
import menu
import util

if __name__ == "__main__":
    load_dotenv()

    # PROGETTO BURGER
    print(
        "  ____  ____   ___   ____ _____ _____ _____ ___    ____  _   _ ____   ____ _____ ____  \n |  _ \\|  _ \\ / _ \\ / ___| ____|_   _|_   _/ _ \\  | __ )| | | |  _ \\ / ___| ____|  _ \\ \n | |_) | |_) | | | | |  _|  _|   | |   | || | | | |  _ \\| | | | |_) | |  _|  _| | |_) |\n |  __/|  _ <| |_| | |_| | |___  | |   | || |_| | | |_) | |_| |  _ <| |_| | |___|  _ < \n |_|   |_| \\_\\\\___/ \\____|_____| |_|   |_| \\___/  |____/ \\___/|_| \\_\\\\____|_____|_| \\_\\\n"
    )

    while True:
        match menu.mostraMenu():
            case 0:
                exit()

            case 1:
                util.selezionaTesto()
                util.mostraTestoSelezionato()
                util.convertiTestoVoce()
                util.unisciVoceMusica()
                util.unisciAudioVideo()

            case 2:
                util.selezionaTesto()
                util.mostraTestoSelezionato()
                util.convertiTestoVoce()
                util.unisciVoceMusica()

            case 3:
                util.selezionaTesto()

            case 4:
                util.mostraTestoSelezionato()

            case 5:
                util.selezionaVoce()

            case 6:
                util.mostraVoceSelezionata()

            case 7:
                util.convertiTestoVoce()

            case 8:
                util.unisciVoceMusica()

            case 9:
                util.unisciAudioVideo()

            case _:
                print("Scelta non valida")

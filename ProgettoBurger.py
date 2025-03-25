import config
import menu
import util

if __name__ == "__main__":
    config.inizializza()

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

            case 2:
                util.mostraTestoSelezionato()

            case 3:
                util.selezionaVoce()

            case 4:
                util.mostraVoceSelezionata()

            case 5:
                util.convertiTestoVoce()

            case 6:
                util.unisciVoceMusica()

            case 7:
                util.unisciAudioVideo()

            case 8:
                util.selezionaTesto()
                util.mostraTestoSelezionato()
                util.convertiTestoVoce()
                util.unisciVoceMusica()

            case 9:
                util.selezionaTesto()
                util.mostraTestoSelezionato()
                util.convertiTestoVoce()
                util.unisciVoceMusica()
                util.unisciAudioVideo()

            case _:
                print("Scelta non valida")

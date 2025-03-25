import config
import util


if __name__ == "__main__":
    config.inizializza()
    # PROGETTO BURGER
    print(
        "  ____  ____   ___   ____ _____ _____ _____ ___    ____  _   _ ____   ____ _____ ____  \n |  _ \\|  _ \\ / _ \\ / ___| ____|_   _|_   _/ _ \\  | __ )| | | |  _ \\ / ___| ____|  _ \\ \n | |_) | |_) | | | | |  _|  _|   | |   | || | | | |  _ \\| | | | |_) | |  _|  _| | |_) |\n |  __/|  _ <| |_| | |_| | |___  | |   | || |_| | | |_) | |_| |  _ <| |_| | |___|  _ < \n |_|   |_| \\_\\\\___/ \\____|_____| |_|   |_| \\___/  |____/ \\___/|_| \\_\\\\____|_____|_| \\_\\\n"
    )

    while True:
        match util.mostraMenu():
            case 0:
                exit()

            case 1:
                util.mostraTesto()

            case 2:
                util.mostraVociDisponibili()

            case 3:
                util.generaAudio()

            case _:
                print("Scelta non valida")

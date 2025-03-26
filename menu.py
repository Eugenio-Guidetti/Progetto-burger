def mostraMenu():

    print("\n --- Opzioni: ---\n")
    print(" 0) Esci")
    print(" 1) Genera video (fai tutto)")
    print(" 2) Genera solo audio")
    print(" 3) Seleziona testo")
    print(" 4) Mostra testo selezionato")
    print(" 5) Seleziona voce")
    print(" 6) Mostra voce selezionata")
    print(" 7) Converti testo voce")
    print(" 8) Unisci voce musica")
    print(" 9) Unisci audio video")

    while True:
        try:
            scelta = input("Scegli un'opzione: ")
        except KeyboardInterrupt:
            return 0

        try:
            print("")
            return int(scelta)
        except:
            print("Input non valido")

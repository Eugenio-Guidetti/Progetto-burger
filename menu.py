def mostraMenu():

    print("\n --- Opzioni: ---\n")
    print(" 0) Esci")
    print(" 1) Seleziona testo")
    print(" 2) Mostra testo selezionato")
    print(" 3) Seleziona voce")
    print(" 4) Mostra voce selezionata")
    print(" 5) Converti testo voce")
    print(" 6) Unisci voce musica")
    print(" 7) Unisci audio video")
    print(" 8) Genera solo audio")
    print(" 9) Genera video (fai tutto)")

    while True:
        try:
            scelta = input("Scegli un'opzione: ")
        except KeyboardInterrupt:
            return 0

        try:
            return int(scelta)
        except:
            print("Input non valido")

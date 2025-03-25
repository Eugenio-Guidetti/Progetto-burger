import os


def getApiKey(key: str):

    path = f"{os.getcwd()}\\{key}.key"

    if os.path.exists(path):
        return open(path, "r").read()
    
    print(f"Chiave API per \"{key}\" non trovata")
    key = input("Inserisci la chiave API: ")
    
    with open(path, "w") as file:
        if key:
            file.write(key)
    
    return key

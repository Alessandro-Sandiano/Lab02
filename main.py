import translator as tr

t = tr.Translator()


while True:

    t.printMenu()
    t.d.name = "dictionary"
    t.loadDictionary(t.d.name)

    txtIn = input()

    # Add input control here!
    while True:
        if len(txtIn) == 0:
            print("Non è stato inserito alcun numero. Riprovare:\n")
        elif len(txtIn) > 1:
            print("È stato inserito più di un carattere. Riprovare:\n")
        else:
            try:
                if not int(txtIn) in range(1, 6):
                    print("Il carattere numerico inserito non è tra quelli disponibili. Riprovare:\n")
                else: break
            except: print("Il carattere inserito non è numerico. Riprovare:\n")
        txtIn = input()

    match int(txtIn):
        case 1:
            result = t.handleAdd()
            if result == -1:
                continue
            print(result)
        case 2:
            print("Inserire la parola aliena da cercare:")
            print(t.handleTranslate(input()))
            print("Premere un qualunque tasto per continuare: \n")
            input()
        case 3:
            print("Inserire la parola aliena da cercare inserendo al suo interno un punto interrogativo "
                  "corrispondente al carattere jolly:")
            print(t.handleWildCard(input()))
            print("Premere un qualunque tasto per continuare: \n")
            input()
        case 4:
            print(t.d.__str__())
            print("Premere un qualunque tasto per continuare: \n")
            input()
        case 5: break
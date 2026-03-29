import translator as tr

t = tr.Translator()


while True:

    t.print_menu()

    t.load_dictionary("dictionary.txt")

    txtIn = input()

    # Add input control here!
    while True:
        '''
        try:
            if int(txtIn) not in range(1, 6):
                txtIn = input("Il numero intero digitato non corrisponde a nessuna opzione. Riprovare: ")
            else: break
        except ValueError: txtIn = input("Non è stato digitato un numero intero. Riprovare: ")
        '''
        if not txtIn.isnumeric():
            txtIn = input("Non è stato digitato un numero intero. Riprovare: ")
            continue
        if not int(txtIn) in range(1, 6):
            txtIn = input("Il numero intero digitato non corrisponde a nessuna opzione. Riprovare: ")
            continue
        break

    match int(txtIn):
        case 1:
            print("Ok, quale parola devo aggiungere?\n")
            txtIn = input()
            '''
            correct = False
            while not correct:
                correct = True
                for c in txtIn:
                    if not (c.isalpha() or c.isspace()):
                        correct = False
                        print("È stato inserito almeno un carattere non alfabetico.")
                        break
                if len(txtIn.split()) == 0:
                    correct = False
                    print("Non è stata inserita alcuna parola.")
                elif len(txtIn.split()) == 1:
                    correct = False
                    print("È stata inserita una sola parola.")
                elif len(txtIn.split(" ")) != len(txtIn.split():)
                    correct = False
                    print("Non è stata rispettata la sintassi",
                          "<parola_aliena traduzione> oppure",
                          "<parola_aliena traduzione1 traduzione2 ...>.")
                if not correct: txtIn = input("Riprovare: ")
            '''
            while True:
                #if any(not c.isalpha() and not c.isspace() for c in txtIn):
                if any(not (c.isalpha() or c.isspace()) for c in txtIn): print("È stato inserito almeno un carattere non alfabetico.")
                if len(txtIn.split()) == 0: print("Non è stata inserita alcuna parola.")
                elif len(txtIn.split()) == 1: print("È stata inserita una sola parola.")
                elif len(txtIn.split(" ")) != len(txtIn.split()): print("Non è stata rispettata la sintassi",
                          "<parola_aliena traduzione> oppure",
                          "<parola_aliena traduzione1 traduzione2 ...>.")
                if (any(not (c.isalpha() or c.isspace()) for c in txtIn)
                or len(txtIn.split()) == 0
                or len(txtIn.split()) == 1
                or len(txtIn.split(" ")) != len(txtIn.split())):
                    txtIn = input("Riprovare: ")
                    continue
                break
            print(t.handle_add(txtIn), end="\n\n")
        case 2:
            print("Ok, quale parola devo cercare?\n")
            txtIn = input()
            while True:
                if any(not (c.isalpha() or c.isspace()) for c in txtIn): print("È stato inserito almeno un carattere non alfabetico.")
                if len(txtIn.split()) == 0: print("Non è stata inserita alcuna parola.")
                elif len(txtIn.split()) > 1: print("È stata inserita più di una parola.")
                elif len(txtIn.split(" ")) != len(txtIn.split()): print("Non è stata rispettata la sintassi <parola_aliena>.")
                if (any(not (c.isalpha() or c.isspace()) for c in txtIn)
                        or len(txtIn.split()) == 0
                        or len(txtIn.split()) > 1
                        or len(txtIn.split(" ")) != len(txtIn.split())):
                    txtIn = input("Riprovare: ")
                    continue
                break
            print(t.handle_translate(txtIn), end="\n\n")
        case 3:
            print("Ok, quale parola devo cercare?\n")
            txtIn = input()
            while True:
                if any(not (c.isalpha() or c.isspace() or c=="?") for c in txtIn): print("È stato inserito almeno un carattere non alfabetico oltre al punto interrogativo.")
                if len(txtIn.split()) == 0: print("Non è stata inserita alcuna parola.")
                elif len(txtIn.split()) > 1: print("È stata inserita più di una parola.")
                elif len(txtIn.split(" ")) != len(txtIn.split()): print("Non è stata rispettata la sintassi <parola_aliena>.")
                if len(txtIn.split("?")) == 1: print("Non è stata utilizzata la wildcard.")
                if len(txtIn.split("?")) > 2: print("Sono utilizzate almeno due wildcard, mentre il numero massimo consentito è uno.")
                if (any(not (c.isalpha() or c.isspace() or c=="?") for c in txtIn)
                    or len(txtIn.split()) == 0
                    or len(txtIn.split()) > 1
                    or len(txtIn.split(" ")) != len(txtIn.split())
                    or len(txtIn.split("?")) == 1
                    or len(txtIn.split("?")) > 2):
                        txtIn = input("Riprovare: ")
                        continue
                break
            print(t.handle_wild_card(txtIn))
        case 4: print(t.dictionary, end="\n\n")
        case 5: break
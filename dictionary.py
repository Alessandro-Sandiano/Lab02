class Dictionary:
    def __init__(self):
        self.entries = [[]]
        #questo attributo consente di usare file di testo con qualunque nome
        self.name = ""

    def __str__(self):
        string=""
        # attenzione al documento vuoto!
        if len(self.entries) == 0: return "Il dizionario in questione è vuoto.\n"
        #istruzione che consente l'esecuzione del programma in caso di mancato caricamento del dizionario nel main;
        #di default, infatti, len(self.entries) = 1 e len(self.entries[0]) == 0
        if len(self.entries) == 1 and len(self.entries[0]) == 0: return "Non è stato caricato alcun dizionario.\n"
        for i in range(len(self.entries)-1):
            for j in range(len(self.entries[i])-1):
                if j == 0: string += "Parola aliena: "
                if j == 1: string += "  Traduzione/i: "
                string += (f"{self.entries[i][j]} ")
            if len(self.entries[i]) == 2: string += "  Traduzione/i: "
            string += (f"{self.entries[i][len(self.entries[i])-1]}\n")
        for j in range(len(self.entries[len(self.entries)-1])-1):
            if j == 0: string += "Parola aliena: "
            if j == 1: string += "  Traduzione/i: "
            string += (f"{self.entries[len(self.entries)-1][j]} ")
        if len(self.entries[len(self.entries)-1]) == 2: string += "  Traduzione/i: "
        string += (f"{self.entries[len(self.entries) - 1][len(self.entries[len(self.entries) - 1])-1]}\n")
        return string

    def addWord(self):
        """
        Metodo che aggiunge nuove parole al dizionario. In caso di errore di inserimento, all'utente viene chiesto
        di riprovare o di ritornare al menù principale.
        :return: int -1 in caso di ritorno al menù principale; str in tutti gli altri casi
        """
        while True:
            print("Inserire la nuova parola con la/e relativa/e traduzione/i usando uno spazio per separarle.\n"
                  "È anche possibile inserire nuove traduzioni di una parola già presente nel dizionario.\n"
                  "Sono ammessi solo caratteri alfabetici.\n")
            string = input().lower()
            inputError = False
            try:
                # il seguente controllo sugli spazi plurimi è superfluo in quanto il metodo "split()" li elimina automaticamente
                if string.find("  ") != -1:
                    inputError = True
                    print("Errore di inserimento: è stato inserito più di uno spazio.")
                if string[0] == " ":
                    inputError = True
                    print("Errore di inserimento: il primo carattere non può essere uno spazio.")
                if string[len(string) - 1] == " ":
                    inputError = True
                    print("Errore di inserimento: l'ultimo carattere non può essere uno spazio.")
            except:
                inputError = True
                print("Non è stato inserito nemmeno un carattere.")
            if len(string.split()) in range (0, 2):
                inputError = True
                print("Errore di inserimento: occorre inserire almeno due termini, ovvero la parola da tradurre e una traduzione.")
            for c in string:
                if not (c.isalpha() or c.isspace()):
                    inputError = True
                    print("Errore di inserimento: sono stati inseriti caratteri non ammessi.")
                    break
            while inputError == True:
                print("Per riprovare, digitare ""Continue"".\n"
                      "Per tornare al menù principale, digitare ""Exit"".\n")
                string = input().lower()
                match string:
                    case "continue": inputError = False
                    case "exit": return -1
                    case _: print("Inserimento errato.\n")
            if string != "continue": break
        splittedString = string.split()
        nAddedWords = 0
        i = 0
        while (i < len(self.entries)):
            if splittedString[0] == self.entries[i][0]:
                print("Parola già esistente nel dizionario. ")
                '''
                Il codice seguente non è ottimizzabile con l'utilizzo del metodo di lista "contains".
                Questo perché tale metodo, andando a controllare anche nel primo oggetto della lista "self.entries[i]",
                impedisce di aggiungere correttamente una traduzione omonima alla parola da tradurre.
                Infatti, la condizione
                if (not(self.entries[i].__contains__(splittedString[j])) or self.entries[i][0] == splittedString[j]):
                non esclude che la traduzione da inserire sia già presente tra quelle precedentemente inserite.
                '''
                j = 1
                while j < len(splittedString):
                    k = 1
                    while k < len(self.entries[i]):
                        if splittedString[j] == self.entries[i][k]:
                            break
                        k += 1
                    if k == len(self.entries[i]):
                        self.entries[i].append(splittedString[j])
                        nAddedWords += 1
                    j += 1
                break
            i += 1
        # per ragioni di efficienza, evito di riscrivere il file di testo del dizionario in caso di nessuna modifica
        if i < len(self.entries) and nAddedWords == 0:
            return "Tutte le traduzioni erano già presenti, quindi non ne sono state aggiunte.\n"
        if i == len(self.entries):
            self.entries.append(splittedString)
            #aggiorno la variabile i; istruzione equivalente, in questo caso, a i += 1
            i = len(self.entries)
        # riscrivo il file di testo del dizionario per aggiornarlo
        file = open(f"{self.name}.txt", "w", encoding="utf-8")
        for j in range(len(self.entries) - 1):
            for k in range(len(self.entries[j]) - 1):
                file.write(f"{self.entries[j][k]} ")
            file.write(f"{self.entries[j][len(self.entries[j]) - 1]}\n")
        for k in range(len(self.entries[len(self.entries) - 1]) - 1):
            file.write(f"{self.entries[len(self.entries) - 1][k]} ")
        file.write(f"{self.entries[len(self.entries) - 1][len(self.entries[len(self.entries) - 1]) - 1]}")
        file.close()
        #i < len(self.entries) è sempre verificata quando nAddedWords == 1, quindi è una condizione superflua
        if nAddedWords == 1: return f"È stata aggiunta {nAddedWords} nuova traduzione.\n"
        #se sono arrivato fin qui, vuol dire che nAddedWords > 1, quindi essa è una condizione superflua
        if i < len(self.entries): return f"Sono state aggiunte {nAddedWords} nuove traduzioni.\n"
        # se sono arrivato fin qui, vuol dire che i == len(self.entries), quindi essa è una condizione superflua
        if len(splittedString) == 2:
            return "La nuova voce è stata aggiunta al dizionario con la relativa traduzione.\n"
        return f"La nuova voce è stata aggiunta al dizionario con le {len(splittedString)-1} traduzioni inserite.\n"


    def translate(self, query):
        i = 0
        while i < len(self.entries):
            if query == self.entries[i][0]: break
            i += 1
        if i < len(self.entries):
            string = f"Traduzione/i di {query}:\n"
            k = 1
            while k < len(self.entries[i]):
                string += self.entries[i][k] + "\n"
                k += 1
            return string
        return "Parola non presente nel dizionario.\n"


    def translateWordWildCard(self, query):
        if len(query) == 0:
            return "Ricerca fallita: non è stata inserita alcuna parola.\n"
        nQuestionMarks = 0
        for c in query:
            if c == "?": nQuestionMarks += 1
        if nQuestionMarks == 0: return "Ricerca fallita: non è stato inserito alcun punto interrogativo.\n"
        if nQuestionMarks > 1: return "Ricerca fallita: è stato inserito più di un punto interrogativo.\n"
        index = 0
        while index < len(query):
            if query[index] == "?": break
            index += 1
        nFoundWords = 0
        string = ""
        for w in self.entries:
            if w[0][0:index] == query[0:index] and w[0][index+1:len(w[0])] == query[index+1:len(query)]:
                nFoundWords += 1
                string += self.translate(w[0]) + "\n"
        if nFoundWords == 0: return "Nessuna parola trovata.\n"
        if nFoundWords == 1: return "Una parola trovata:\n" + string
        return "Più di una parola trovata:\n" + string

    def load(self, dict):
        # dict is a string with the filename of the dictionary
        self.name = dict
        file = open(f"{self.name}.txt", "r", encoding="utf-8")
        self.entries = file.readlines()
        file.close()
        for i in range(len(self.entries)):
            self.entries[i] = self.entries[i].split()

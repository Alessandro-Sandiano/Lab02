import dictionary

class Translator:

    def __init__(self):
        self.d = dictionary.Dictionary()

    def printMenu(self):
        print ("______________________________\n" +
              "   Translator Alien-Italian\n"+
              "______________________________\n" +
              "1. Aggiungi nuova parola\n" +
              "2. Cerca una traduzione\n" +
              "3. Cerca con wildcard\n" +
              "4. Stampa tutto il Dizionario\n" +
              "5. Exit\n"+
              "______________________________\n")

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        # la seguente istruzione serve per tenere traccia del nome e poterlo usare nel metodo successivo
        self.d.name = dict
        file = open(f"{self.d.name}.txt", "r", encoding="utf-8")
        self.d.entries = file.readlines()
        file.close()
        # attenzione al documento vuoto!
        if len(self.d.entries) == 0: return "Operazione fallita perché il dizionario in questione è vuoto.\n"
        for i in range(len(self.d.entries)):
            self.d.entries[i] = self.d.entries[i].split()
        return "Dizionario caricato correttamente.\n"

    def handleAdd(self):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        returnAddWord = self.d.addWord()
        if returnAddWord == -1: return -1
        # per ragioni di efficienza, evito di riscrivere il file di testo del dizionario in caso di nessuna modifica
        if returnAddWord[0] == "T": return returnAddWord
        file = open (f"{self.d.name}.txt", "w", encoding="utf-8")
        # riscrivo il file di testo del dizionario per aggiornarlo
        for i in range(len(self.d.entries)-1):
            for j in range(len(self.d.entries[i])-1):
                file.write(f"{self.d.entries[i][j]} ")
            file.write(f"{self.d.entries[i][len(self.d.entries[i])-1]}\n")
        for j in range(len(self.d.entries[len(self.d.entries)-1])-1):
            file.write(f"{self.d.entries[len(self.d.entries)-1][j]} ")
        file.write(f"{self.d.entries[len(self.d.entries) - 1][len(self.d.entries[len(self.d.entries) - 1])-1]}")
        file.close()
        return returnAddWord


    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        return self.d.translate(query)

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        return self.d.translateWordWildCard(query)
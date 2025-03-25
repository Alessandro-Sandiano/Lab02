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
        return self.d.load(dict)

    def handleAdd(self):
        return self.d.addWord()

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        return self.d.translate(query)

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        return self.d.translateWordWildCard(query)
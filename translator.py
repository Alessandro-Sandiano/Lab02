import dictionary

class Translator:

    def __init__(self):
        self.d = dictionary.Dictionary()

    @staticmethod
    def print_menu():
        print ("______________________________\n" +
              "   Translator Alien-Italian\n"+
              "______________________________\n" +
              "1. Aggiungi nuova parola\n" +
              "2. Cerca una traduzione\n" +
              "3. Cerca con wildcard\n" +
              "4. Stampa tutto il Dizionario\n" +
              "5. Exit\n"+
              "______________________________\n")

    def load_dictionary(self, dict):
        return self.d.load(dict)

    def handle_add(self):
        return self.d.add_word()

    def handle_translate(self, query):
        # query is a string <parola_aliena>
        return self.d.translate(query)

    def handle_wild_card(self,query):
        # query is a string with a ? --> <par?la_aliena>
        return self.d.translate_word_wild_card(query)
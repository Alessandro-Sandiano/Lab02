import dictionary

class Translator:

    def __init__(self):
        self._dictionary = dictionary.Dictionary()

    @staticmethod
    def print_menu():
        print("______________________________")
        print("Translator Alien-Italian")
        print("______________________________")
        print("1. Aggiungi nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcard")
        print("4. Stampa tutto il Dizionario")
        print("5. Exit")
        print("______________________________")

    #controllare bene tutte le mie documentazioni
    def load_dictionary(self, dict_name):
        """
        :param dict_name: string with the filename of the dictionary.
        """
        self._dictionary.filename = dict_name
        with open(dict_name, "r", encoding="utf-8") as file:
            for line in file: self._dictionary.add_word(line)

    def handle_add(self, entry):
        """
        Call "addWord" method of the class Dictionary and update the file.
        :param entry: string <parola_aliena traduzione1 traduzione2 ...>.
        :return: string with the new word or new translation(s).
        """
        s = self._dictionary.add_word(entry)
        with open(self._dictionary.filename, "w", encoding="utf-8") as file:
            '''
            for i in range(len(self._dictionary.words_dict)-1):
                file.write(f"{list(self._dictionary.words_dict)[i]} {self._dictionary.words_dict[list(self._dictionary.words_dict)[i]]}\n")
            '''
            for i in list(self._dictionary.words_dict)[:-1]:
                file.write(f"{i} {self._dictionary.words_dict[i]}\n")
            #file.write(f"{list(self._dictionary.words_dict)[len(self._dictionary.words_dict)-1]} {self._dictionary.words_dict[list(self._dictionary.words_dict)[len(self._dictionary.words_dict)-1]]}")
            file.write(f"{list(self._dictionary.words_dict)[-1]} {self._dictionary.words_dict[list(self._dictionary.words_dict)[-1]]}")
        return s

    def handle_translate(self, query):
        """
        :param query: string <parola_aliena>
        :return: string with the translation(s) of the word.
        """
        s = self._dictionary.translate(query)
        match s:
            case None: return "Nessuna parola trovata."
            case _: return s

    def handle_wild_card(self,query):
        """
        :param query: string with a ? --> <par?la_aliena>
        :return: string with the word(s) founded with its translation(s).
        """
        return self._dictionary.translate_word_wild_card(query)

    def __str__(self):
        return self._dictionary.__str__()

    @property
    def dictionary(self):
        return self._dictionary

    @dictionary.setter
    def dictionary(self, dictionary):
        self._dictionary = dictionary
import re
import collections

class Dictionary:
    def __init__(self, words_dict={}):
        self._words_dict = words_dict
        self._filename = str()

    def add_word(self, word):
        """
        Add a new word or new translations to the dictionary.
        :param word: string <parola_aliena traduzione1 traduzione2 ...>.
        :return: string with the new word or new translation(s).
        """
        '''
        if word[len(word)-1] == "\n":
            word = word[:-1]
        word = word.lower()
        '''
        word = word.strip().lower()
        to_add = [word.split()[0]]
        if word.split()[0] in self._words_dict:
            for w in word.split(maxsplit=1)[1].split():
                if w not in self._words_dict[word.split()[0]].split():
                    #self._words_dict[word.split()[0]] = self._words_dict[word.split()[0]] + " " + w
                    #self._words_dict[word.split()[0]] = f"{self._words_dict[word.split()[0]]} {w}"
                    self._words_dict[word.split()[0]] = self._words_dict[word.split()[0]] + f" {w}"
                    to_add.append(w)
            match len(to_add):
                case 1: return "Parola già esistente; nessuna traduzione da aggiungere."
                case 2: return f"{to_add}\nParola già esistente; {len(to_add) - 1} traduzione aggiunta!"
                case _: return f"{to_add}\nParola già esistente; {len(to_add) - 1} traduzioni aggiunte!"
        s = ""
        for k in collections.Counter(word.split(maxsplit=1)[1].split()).keys():
            s += k + " "
        s = s[:-1]
        self._words_dict[word.split()[0]] = s
        '''
        #to_add.append(word.split(maxsplit=1)[1].split()[0])
        to_add.append(word.split()[1])
        for t in word.split(maxsplit=1)[1].split():
            if not to_add[1:].__contains__(t): to_add.append(t)
        '''
        to_add.extend(s.split())
        return f"{to_add}\nAggiunta!"

    def translate(self, word):
        #for w in self._words_dict.keys():
        for w in self._words_dict:
            #w.lower() already in addWord
            if w == word.lower():
                return self._words_dict[w].split()
        return None

    def translate_word_wild_card(self, word):
        s = str()
        for w in self._words_dict:
            if re.search(f"^{word.lower().split("?")[0]}.{word.lower().split("?")[1]}$", w):
                # Output required by the exercise:
                #s += f"{word.lower().split("?")[0]}.{word.lower().split("?")[1]}\n{list(self._words_dict[w].split())}\n\n"
                s += f"{w}\n{list(self._words_dict[w].split())}\n\n"
        if s == "": return "Nessuna parola trovata.\n\n"
        return s

    def __str__(self):
        s = str()
        d = sorted(self._words_dict.items(), key=lambda x: x[0])
        for w in d[:-1]:
            s += w[0] + " -> " + w[1] + "\n"
        s += d[-1][0] + " -> " + d[-1][1]
        return s

    @property
    def words_dict(self):
        return self._words_dict

    @words_dict.setter
    def words_dict(self, words_dict):
        self._words_dict = words_dict

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, filename):
        self._filename = filename

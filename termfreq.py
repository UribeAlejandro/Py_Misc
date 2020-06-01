from collections import namedtuple


def termfreq(s):
    unique_words = []
    terms = s.lower().strip().split()
    print(terms)
    Term = namedtuple('Term', 'word freq')

    aux = []
    for word in terms:
        if word.capitalize() not in unique_words:
            unique_words.append(word.capitalize())
            aux.append(Term(word=str(word.capitalize()),
                            freq=terms.count(word) / len(terms)))

    s = ""
    for i in range(0, len(aux)):
        s += aux[i].word + ": " + str(aux[i].freq) + " "
    return s


text = 'Deep deep Learning learning Machine machine DeEp'
print(termfreq(text))

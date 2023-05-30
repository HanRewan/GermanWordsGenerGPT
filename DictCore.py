
class Word:

    def __init__(self, worddata):
        self.translation = worddata[3]
        self.phrase = (worddata[1] + ' ') * (worddata[1] != '#') + worddata[0]
        self.type = worddata[2]

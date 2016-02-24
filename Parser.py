class WordList:
    def __init__(self, queryString):
        queryString = queryString.replace(",", " , ")
        queryString = queryString.replace("(", " ( ")
        queryString = queryString.replace(")", " ) ")
        self.wordList = queryString.lower().split()

    def next_word(self):
        if len(self.wordList) > 0:
            return self.wordList.pop(0)
        else:
            return False

    def peek(self):
        if len(self.wordList) > 0:
            return self.wordList[0]
        else:
            return False


class Parser:
    def __init__(self):
        print("I'm a parser")

    def _split_out_sub_clause(self, wordList):

        nextWord = wordList.next_word()
        while nextWord != "(":
            nextWord = wordList.next_word()
        bracketDepth = 1
        output = []
        while bracketDepth > 0 and wordList.peek() is not False:
            nextWord = wordList.next_word()
            if nextWord == "(":
                bracketDepth += 1
            elif nextWord == ")":
                bracketDepth -= 1
            output.append(nextWord)
        return output[:-1]

    def parse(self, query):

        if ";" in query or "with" not in query: return query.split(";")

        output = []
        wordList = WordList(query)
        while wordList.peek() is not False:
            nextWord = wordList.next_word()
            if nextWord == "select":
                output.append(["select"] + wordList.wordList)
                break
            elif nextWord in ["with", "as"]:
                output.append(self._split_out_sub_clause(wordList))
        return [" ".join(x) for x in output]

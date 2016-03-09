from Query import Query
import sqlparse
from sqlparse.tokens import Keyword, DML

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

        '''Todo: this has to be able to recognise dependencies'''
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

    def _update_dependencies(self, queryList):
        for baseQuery in queryList:
            for query in queryList:
                if query.name in baseQuery.query:
                    baseQuery.dependencies.append(query.name)
        return queryList


    def parse(self, query, name = None):

        query = query.replace("--", " ")
        if name is None: name = "final_query"

        if ";" in query or "with" not in query:
            return [Query("test", x.lower(), []) for x in query.split(";")]

        output = []
        wordList = WordList(query)
        standingName = ""

        while wordList.peek() is not False:
            nextWord = wordList.next_word()
            if nextWord == "select":
                output.append(Query(name, " ".join(["select"] + wordList.wordList), []))
                break
            elif nextWord in ["as"]:
                output.append(Query(standingName, " ".join(self._split_out_sub_clause(wordList)), []))
            else:
                standingName = nextWord

        output = self._update_dependencies(output)

        return output

    def parse_details(self, query, name = None):

        output = {"columns": [], "tables": [], "where": ""}
        state = "start"

        parsed = sqlparse.parse(query)
        for token in parsed[0].tokens:
            if token.ttype is sqlparse.tokens.Whitespace: continue

            if token.ttype is sqlparse.tokens.DML:
                state = "select"
                continue

            if state == "select" and token.ttype is not sqlparse.tokens.Punctuation:
                if token.value == "from":
                    state = "from"
                    continue

                if type(token) is sqlparse.sql.IdentifierList:
                    for item in token.get_identifiers():
                        if type(item) == sqlparse.sql.Identifier and item.has_alias():
                            output["columns"].append(item.get_alias())
                        elif type(item) == sqlparse.sql.Identifier:
                            output["columns"].append(item.get_name())
                        else:
                            output["columns"].append(item.value)
                    continue
                output["columns"].append(str(token.value))

            if state == "from":

                if type(token) is sqlparse.sql.Where:
                    output["where"] = token.value.replace("where", "").strip()
                    state = "where"
                    continue

                if type(token) is sqlparse.sql.Identifier:
                    output["tables"].append(token.get_name())


        return output
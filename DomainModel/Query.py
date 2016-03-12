import sqlparse
from DomainModel.Table import Table
from DomainModel.Column import Column

class Query:

    def __init__(self, name, text):
        self.name, self.text = name, text

        self.columns = []
        self.tables = []
        self.dependencies = []

        self.parse()

    def parse(self):

        state = "start"
        tokens = sqlparse.parse(self.text)[0].tokens
        tokens = [x for x in tokens if not (x.ttype is sqlparse.tokens.Whitespace)]

        for token in tokens:

            if token.ttype is sqlparse.tokens.DML:
                state = "select"
                continue

            if state == "select" and token.ttype is not sqlparse.tokens.Punctuation:
                if token.value.lower() == "from":
                    state = "from"
                    continue

                if type(token) is sqlparse.sql.IdentifierList:
                    for item in token.get_identifiers():
                        if type(item) == sqlparse.sql.Identifier and item.has_alias():
                            self.columns.append(Column(item.get_alias(), "varchar(255)"))
                        elif type(item) == sqlparse.sql.Identifier:
                            self.columns.append(Column(item.get_name(), "varchar(255)"))
                        else:
                            self.columns.append(Column(item.value, "varchar(255)"))
                    continue

                if token.ttype is not sqlparse.tokens.Punctuation and token.ttype is not sqlparse.tokens.Whitespace and str(token.value) != "\n":
                    self.columns.append(Column(item.value, "varchar(255)"))

            if state == "from":

                if type(token) is sqlparse.sql.Where or token.value.lower() == "group":
                    break

                if type(token) is sqlparse.sql.Identifier:
                    self.tables.append(Table(token.get_name()))

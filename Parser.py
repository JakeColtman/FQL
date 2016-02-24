class Parser:

    def __init__(self):
        print("I'm a parser")

    def parse(self, query):
        return query.split(";")
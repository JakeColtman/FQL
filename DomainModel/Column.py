class Column:

    def __init__(self, name):
        self.name = name
        self.sql_type = ""
        self.identifier = ""
        self.parse_name()

    def parse_name(self):
        identifier = self.name.split("_")[-1]
        self.identifier = identifier
        if identifier == "amount":
            self.sql_type = "float"
        elif identifier == "date":
            self.sql_type = "timestamp"
        elif identifier == "is":
            self.sql_type = "boolean"
        elif identifier == "bool":
            self.sql_type = "boolean"
        elif identifier == "id":
            self.sql_type = "int"
        elif identifier == "int":
            self.sql_type = "int"
        elif identifier == "number":
            self.sql_type = "int"
        elif identifier == "percent":
            self.sql_type = "float"
        elif identifier == "float":
            self.sql_type = "float"
        else:
            self.sql_type = "varchar(255)"

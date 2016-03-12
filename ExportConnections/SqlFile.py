from Repository import Repository

class SqlFile:

    def __init__(self, file_name: str):
        self.file_name = file_name

    def export(self, text):
        with open(self.file_name, "w") as file_open:
            file_open.write(text)

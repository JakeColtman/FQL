from Repository import Repository


class RepositorySearcher:

    def __init__(self, repo: Repository):
        self.repo = repo

    def get_best_guesses(self, keyword):
        queries = self.repo.retrieve_all_queries()
        inDescr = [q for q in queries if keyword in q.description]
        inName = [q for q in queries if keyword in q.name]
        inBoth = set(inDescr).intersection(inName)
        if len(inBoth) > 0:
            return list(inBoth)
        else:
            return inName
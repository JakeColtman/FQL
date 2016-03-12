import sqlparse
from DomainModel.Query import Query


class SqlCode:

    def __init__(self, text:str, final_query_name: str = None):
        if final_query_name is None: final_query_name = "final_query"
        self.text, self.query_name = text, final_query_name
        self.queries = []
        self.split_into_cte_queries()
        self.identify_dependencies_in_query_list()

    def split_into_cte_queries(self):

        tokens = sqlparse.parse(self.text)[0].tokens
        if not any([x.ttype is sqlparse.tokens.Keyword and "with" in x.value for x in tokens]):
            self.queries.append(Query(self.query_name, self.text))
            return
        ii = 0
        while ii < len(tokens):
            if type(tokens[ii]) == sqlparse.sql.IdentifierList:
                ctes = tokens[ii].get_identifiers()
                for cte in ctes:
                    cte_name = cte.value
                    cte_text = str(cte).replace(cte.value + " as", "").strip()[1:-1]
                    self.queries.append(Query(cte_name, cte_text))
                break

            if type(tokens[ii]) == type(tokens[ii]) == sqlparse.sql.Identifier:
                cte_name = tokens[ii].value
                cte_text = str(tokens[ii]).replace(tokens[ii].value + " as", "").strip()[1:-1]
                self.queries.append(Query(cte_name, cte_text))
                break

            if tokens[ii].ttype is sqlparse.tokens.DML:
                raise
            ii += 1



        final_query_text = "".join([str(x) for x in tokens[ii + 1:]])
        self.queries.append(Query(self.query_name, final_query_text))

    def identify_dependencies_in_query_list(self):

        for ii, query in enumerate(self.queries[::-1]):
            for possibleDep in self.queries[:len(self.queries) - ii - 1]:
                if possibleDep.name in query.table_names():
                    query.dependencies.append(possibleDep.name)

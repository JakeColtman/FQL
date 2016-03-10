import sqlparse
from Query import Query


def split_out_ctes(code:str, query_name = None):

    if query_name is None: query_name = "final_query"
    parsed = sqlparse.parse(code)
    print(parsed[0].tokens)
    #If there are no ctes, returns a list of just the code
    if not any([x.ttype is sqlparse.tokens.Keyword and "with" in x.value for x in parsed[0].tokens]):
        return [code]

    ii = 0
    while type(parsed[0].tokens[ii]) != sqlparse.sql.IdentifierList:
        ii += 1
    cteList = parsed[0].tokens[ii].get_identifiers()

    output = []

    for cte in cteList:
        name = cte.value
        query = str(cte).replace(cte.value, "").replace("as", "").strip()[1:-1]
        output.append(Query(name, query, []))

    final_query_text = "".join([str(x) for x in parsed[0].tokens[ii + 1:]])

    output.append(Query(query_name, final_query_text, []))

    return output


def parse_query_to_detailed(query: Query):

    state = "start"
    textQuery = query.query

    query = query._replace(query = {"columns": [], "tables": [], "where": "", "string":textQuery})

    parsed = sqlparse.parse(textQuery)
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
                        query.query["columns"].append(item.get_alias())
                    elif type(item) == sqlparse.sql.Identifier:
                        query.query["columns"].append(item.get_name())
                    else:
                        query.query["columns"].append(item.value)
                continue
            query.query["columns"].append(str(token.value))

        if state == "from":

            if type(token) is sqlparse.sql.Where:
                query.query["where"] = token.value.replace("where", "").strip()
                state = "where"
                continue

            if type(token) is sqlparse.sql.Identifier:
                query.query["tables"].append(token.get_name())

    return query

def identify_dependencies_in_query_list(query_list: list):
    for ii, query in enumerate(query_list[::-1]):
        for possibleDep in query_list[:len(query_list) - ii - 1]:
            if possibleDep.name in query.query["tables"]:
                query.dependencies.append(possibleDep.name)
    return query_list
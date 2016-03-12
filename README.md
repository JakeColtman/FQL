# FQL

FQL is a set of tools designed to support and extend a philosophy of writing SQL code.  The intended goal of combining these together 
is to allow the user to write SQL code that:

* Encapsualtes tables from logic
* Allows interface based design
* Enables code reuse
* Is testable

None of these goals are particularly controversial, indeed they are all things that we would expect in normal programming languages, but
they can be difficult to achieve in normal SQL.

### Philosophy

One of the central claims of the philosophy is that maintainability and readability are more important that speed or efficiency.  For most analytics projects most of the time, taking an efficiency hit of 2-5x is not an issue, and in those cases where it is, it can be overcome by cacheing or better query planning.  By contrast, writing code that can be easily understood and modified is crucial. 

A second claim is that sql code should be structured as closely as possible to business logic.  It is tempting to write sql code as one highly efficient block of code, but this rapidly descends into a big ball of mud that if difficult to deal with.  By keeping the code similar to the business logic, we can easily walk through the steps involved and get the involvement of domain experts who might not be coding experts

### Implementing the philosophy:

If we accept this philosophy, how should we implement it?  The main tool for doing this is the common table expression (CTE).  CTEs 
are temporary tables that are created on the fly, and they have strong similarities to functions in functional languages.  Like functions, each CTE has a type definition.  The inputs to the CTE are the CTEs and tables that it depends on and the output is a set of tuples.  Also like functions, CTEs can be composed together to prodcue arbitrarily complex logic.

If we write our sql so that each major transformation takes place in a single CTE, we can gain the same advantages that we get from breaking up a program into functions.  We can reuse the same transformation in different places and across different sql queries, we only have to change the logic in one place rather than many different places, and we can test the particular piece of logic in isolation to the rest of the code.

### FQL Tooling:

Managing all of these CTEs my hand is boring and pointless, so we needing tools to help us do this. Enter FQL

The first piece of tooling we need is a way to store queries for future use.  Using FQL we can break a big query apart into constituent parts and store it in a central repository:

```python 
sqlCode = """ with companies as
                (
                    -- description
                    select company_id, name
                    from companies
                ),
                accounts as
                (
                    /* Im the accounts */
                    select account_id, name
                    from
                    testtable
                )
                select name
                from
                accounts
        """
code = SqlCode(sqlCode)
repo = Repository("repo.pickle")
repo.add_queries(code.queries)
repo.save()
```

Note that the comments at the start of the ctes act like doc strings, they are stored as query.description

Of course, storing the queries is only half the battle, we also need the ability to retrieve them on command.  There are two ways to do this depending on whether or not you know the exact name of the CTE.

If you do, you can bring it back like:

```python 
repo = Repository("repo.pickle")
repo.retrieve_query("accounts"
```

If you don't, you can have the repoistory return the best guess as to the query you want based on keywords and the information based in the query name and description:

```python
repo = Repository("repo.pickle")
searcher = RepositorySearcher(repo)
found = searcher.get_best_guesses("accounts")
```

Once you have the CTE that you are looking for, you can turn it into a runnable piece of SQL using the QueryGenerator class:

```python 
repo = Repository("repo.pickle")
qg = QueryGenerator(self.repo)
sql = qg.generate_query(query.name)
```

This will search through the repository for the query, find all the other ctes which the query depends on and produces a sql query string needed to run the CTE.

####Testing

FQL provides a great setup to test your CTEs.  To keep the tests as closely inline with the data as possible, FQL does all of the testing through the same DB that your data sits on.  It creates a new schema (default name tests) with one table for each of your CTEs.  To add a tests, simply insert the test input data into the relevant input CTEs and the expected output values into the appropriate tables.  FQL will scan through the tables for each test and identify exactly which CTEs can be tested using the information you inserted.

The first time you use the testing, FQL provides a helper function setup_repository_test_suite to create the schema and all of the necessary tables.  You will need to rerun this if you update the CTEs.

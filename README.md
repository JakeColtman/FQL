# FQL

FQL is a set of tools designed to support and extend a philosophy of writing SQL code.  The intended goal of combining these together 
is to allow the user to write SQL code that:

* Encapsualtes tables from logic
* Allows interface based design
* Enables code reuse
* Is testable

None of these goals are particularly controversial, indeed they are all things that we would expect in normal programming languages, but
they can be difficult to achieve in normal SQL.

## Philosophy

One of the central claims of the philosophy is that maintainability and readability are more important that speed or efficiency.  For most analytics projects most of the time, taking an efficiency hit of 2-5x is not an issue, and in those cases where it is, it can be overcome by cacheing or better query planning.  By contrast, writing code that can be easily understood and modified is crucial. 

A second claim is that sql code should be structured as closely as possible to business logic.  It is tempting to write sql code as one highly efficient block of code, but this rapidly descends into a big ball of mud that if difficult to deal with.  By keeping the code similar to the business logic, we can easily walk through the steps involved and get the involvement of domain experts who might not be coding experts

## Implementing the philosophy:

If we accept this philosophy, how should we implement it?  The main tool for doing this is the common table expression (CTE).  CTEs 
are temporary tables that are created on the fly, and they have strong similarities to functions in functional languages.  Like functions, each CTE has a type definition.  The inputs to the CTE are the CTEs and tables that it depends on and the output is a set of tuples.  Also like functions, CTEs can be composed together to prodcue arbitrarily complex logic.  

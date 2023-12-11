# Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
  PostgreSQL is an open-source RDBMS, relational database management system.

- What is the difference between SQL and PostgreSQL?
  SQL is a standard programming language used to manage and control relatonal databases.  PostgreSQL is a relational database that uses SQL as it's query language.  

- In `psql`, how do you connect to a database?
  'psql' is a command-line tool used to connect to a postgrSQL
  database.  If you running a postgresSQL database on the local system and are the default user you can login by simply entering psgl. If not you will need to enter credentials.
  psql -d databasename -U username -W.  The -W will force a password prompt.  Type `psql --h` form more information. 

- What is the difference between `HAVING` and `WHERE`?
  `WHERE` is used with the SELECT, UPDATE and DELETE commands to filter individula rows of data before they are grouped or aggregated.  `HAVING` is used to filter aggregate functions after the grouping has been applied.  It can only be used after a `GROUP BY` clause.

- What is the difference between an `INNER` and `OUTER` join?
  `Inner joins` return rows that have matching values in both tables that meet a specified condition.  It contains common data from both tables.  
  `Outer joins` returns data that don't match a condition from one or both tables.  
  There's three types of Outer joins:
  LEFT OUTER JOIN - returns all data from the left table and         matching data from the right table.
  RIGHT OUT JOIN - returns all data from the right table and matching data from the left table.
  FULL OUTER JOIN - returns all rows that don't a match either table.  NULL's are returned for columns form the table without a match.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
  `LEFT OUTER` will return all colums from the left table and only matching rows from the right table. 
  `RIGHT OUTER` will retrun all rows from the right table and only matching rows from the left table.

- What is an ORM? What do they do?
  `ORM` stands for Object-Relational Mapping. It's a programming approach that allows programmers to use object-oriented lanuages to interact with relational databases. It allows programmers to work with database records as if they were objects

- What are some differences between making HTTP requests using AJAX
  and from the server side using a library like `requests`?
  `AJAX` is used on the client side (browser).  It uses JavaScript to make asynchronous requests without reloading the page.
  `requests` are used on the server side.  It allows the server to make HTTP requests to other servers or API's. 

- What is CSRF? What is the purpose of the CSRF token?
  `CSRF` or Cross-Site Request Forgery is a type of security vulnerability that performs undesired action on a website where a user is logged in. The purpose of a `CSRF token` is to make sure the request came from a valid website and was not forged by an attacker.  CSFR tokens are random and unique to the users session and cannot be duplicated by hackers. 

- What is the purpose of `form.hidden_tag()`?
  The `form.hidden_tag()` is a Flask function used to create hidden input fields inside HTML forms.  It usually contains a CSRF token.  The token protects against Cross-Site Request Forgery attacks.

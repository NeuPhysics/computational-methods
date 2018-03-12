SQL
=====================

.. admonition:: Differences between Relational and Non-Relational
   :class: note

   1. Adding a new field to data:
      1. Relational: requires a new column
      2. Non-Relational: just add the field to one single document, thus can be easily decentralized.


Basics and Background
-----------------------

1. SQL: Structured Query Language
2. Relational Database:
   1. usually in tables
   2. rows are called records
   3. columns are certain types of data. Data type of rows are specified:
      1. INTEGER
      2. TEXT
      3. DATE
      4. REAL, real numbers
      5. NULL
      6. ...
3. RDBMS: Relational Database Management System, most RDBMS use SQL as the query language. SQLite is one of the RDBMS.
   1. SQLite: open source and minimal
   2. MySQL: powerful and popular, also open source, controlled by Oracle, not really scalable.
   3. PostgreSQL: open source, even slower than MySQL.
   4. OracleDB: not open source
   5. SQL Server: from Microsoft, not open source, and only on windows.



SQL
---------------------------

.. admonition:: Semicolon
   :class: warning

   Semicolon in SQL is a statement terminator. Just use it.


.. admonition:: Capitalization Strategy
   :class: note

   For readablilty

   1. Capitalize clauses
   2. Capitalize table names etc

   On stackoverflow: `stackoverflow <https://stackoverflow.com/questions/608196/why-should-i-capitalize-my-sql-keywords>`_


Statements for Manipulation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Create table

   .. code-block:: SQL

      CREATE TABLE table_name (
          column_1 data_type,
          column_2 data_type,
          column_3 data_type
        );

   Constraints can be included when creating tables. I am using the example from `CodeAcademy <https://www.codecademy.com/courses/learn-sql-manipulation/lessons/manipulation/exercises/delete>`_.

   .. code-block:: SQL

      CREATE TABLE awards (
      --id should be integer, and is the primary key
         id INTEGER PRIMARY KEY,
      --recipient should be text and can not be null
         recipient TEXT NOT NULL,
      --default values for a column
         award_name TEXT DEFAULT "Grammy"
      );

   As mentioned in the basics section, primary keys should be unique to identify the specific row.

2. Insert new row

   .. code-block:: SQL

      INSERT INTO table_name (column_1, column_2, column_3)
      VALUES (some_value_1, some_value_2, some_value_3);

3. Select from table; select returns *result set* which is a new table.

   .. code-block:: SQL

      -- Select out everything from table
      SELECT * FROM table_name;
      -- Select out the values of a specific column
      SELECT column_1 FROM table_name;


4. Update some values

   .. code-block:: SQL

      -- Specify the table
      UPDATE table_name
      -- choose column to be updated
      SET column_1 = some_other_value_1
      -- specify row location
      WHERE column_2 = some_specific_value_to_locate_the_row;

5. Add new columns

   .. code-block:: SQL

      -- speficy table
      ALTER table_name
      -- add column and specify data type, here I use TEXT
      ADD COLUMN column_4 TEXT

6. Delete rows

   .. code-block:: SQL

      DELETE FROM celebs
      -- I use column_4 as an example
      -- Delete every row if column_4 has NULL values
      WHERE column_4 IS NULL;



Statements for Queries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~





References and Notes
----------------------


1. `What is a Relational Database Management System (RDBMS)? <https://www.codecademy.com/articles/what-is-rdbms-sql>`_
2. `List of SQL commands <https://www.codecademy.com/articles/sql-commands>`_

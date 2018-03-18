MongoDB
====================


.. admonition:: 2018-02-30
   :class: note

   I find mongoDB fascinating. I have ready written `an app that connects to mongoDB and reads out the status <https://github.com/uupers/BiliSpider/releases>`_.

   BUT it's something that worth dive deep into.


Management
-----------------------------


MongoDB Shell
~~~~~~~~~~~~~~~~~~~~~~~~


1. Collections: just like tables in SQL.



Some examples:

.. code-block:: text

   // show the databases
   show dbs

   // show collections
   show collections

   //set any database to current database
   use database_name

   // insert entry
   db.database_name.insert( an_object_2_be_the_entry )

   // read document
   db.database_name.findOne({'some_field':'value_of_field'})
   db.database_name.fidn()

   // prettify
   db.database_name.find().pretty()



References and Notes
-------------------------------


1. `MongoDB Cheatsheet <https://gist.github.com/emptymalei/8c6b4fbbf0d92ba0ffb856439ec9cc64>`_

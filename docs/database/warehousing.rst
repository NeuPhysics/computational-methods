Data Warehousing
==============================

General Approaches
-----------------------

1. OLTP
2. OLAP

ETL Process
------------------------

.. admonition:: ETL
   :class: warning

   1. Extract: extract data from sources
   2. Transform: transform it to proper format
   3. Load: load it to data storage infrastructure


E for Extract
~~~~~~~~~~~~~~~~~~~~~

1. Should not affect the source system.


T for Transform
~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Cleaning
2. Filtering
3. Enriching
4. Splitting
5. Joining


L for Load
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Deal with sync and waiting



.. admonition:: Case
   :class: note

   This is a case design for a house-renting website.


What Purpose
--------------------

To gain more users and houses.

1. What is the location characteristics for the region that has more tenants? Presumably the regions with more businesses.
2. What is the house characteristics for more tenants? Better services? Better prices?
   Need the 'amenities', 'pricing', 'services', 'bedroomCount', 'dynamicScore', 'totalScore' in HomeLike api. (What is dynamicScore anyway?)
3. What do the tenants like? Collect data about tenants. Need the house characteristics the tenants have rented.
4. How can we provide better services for the tenants? Using predictions?
5. Can we use general information about the tenants such as jobs to predict the use cases?


What Data
------------------------------------


1. General data:
2. Owner:
   1. houses and data of the houses
   2. past tenants
   3. comments on tenants
3. Tenants:
   1. houses rented and their data
   2. comments on houses
   3. job and identity data






Challenges
-------------------------------

1. Time/Data format: make sure the data format is correct.
2. NoSQL to SQL: new fields?



References and Notes
------------------------


1. `ETL (Extract, Transform, and Load) Process & Concept <http://blog.appliedinformaticsinc.com/etl-extract-transform-and-load-process-concept/>`_
2. `Designing Data-Intensive Applications <https://book.douban.com/subject/26197294/>`_
3. `Design and Build a Data Warehouse for Business  <https://www.youtube.com/playlist?list=PL73oFZbnYuix7Xi5C3oFjGlZsnMjisZ-y>`_

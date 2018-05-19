Data Warehouse
====================



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



Tools
-------------------------------

For Data
~~~~~~~~~~~~~~~~~~~~~

1. BigQuery
2. Athena
3. Redshift

Pipeline
---------------------------

1. `Apache Airflow <https://airflow.apache.org/>`_: Pipeline management
2. `mosql <https://github.com/stripe/mosql>`_: MongoDB to PostgreSQL


Data Visualization
--------------------------


1. `Apache incubator-superset <https://github.com/apache/incubator-superset>`_ (`Apache 2.0`): business intelligence web application.


Challenges
-------------------------------

1. Time/Data format: make sure the data format is correct.
2. NoSQL to SQL: new fields?



References and Notes
-----------------------


1. `Design and Build a Data Warehouse for Business  <https://www.youtube.com/playlist?list=PL73oFZbnYuix7Xi5C3oFjGlZsnMjisZ-y>`_

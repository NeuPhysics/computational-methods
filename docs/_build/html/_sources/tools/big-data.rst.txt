Big Data
==========================


In scientific computings, we are used to HDF5 or netCDF. As it is possible to use HDF5 for big data, the insdustries have built many tools for better performance.



Frameworks
------------------------

Batch-only
~~~~~~~~~~~~~~~~~~~~~~~~

Batch is for extremely large datasets and accessing the whole set of data.

1. Hadoop

Hadoop comes with

1. HDFS
2. YARN
3. MapReduce

Data processing with Hadoop will extensively read and write into the storage devices.


Stream-only
~~~~~~~~~~~~~~~~~~~~~~~

Stream processing is best for calculations on a small patch of data which is streaming through the system.

1. Storm: extremely low latency as real time
2. Samza: together with Kafka


Hybrid
~~~~~~~~~~~~~~~~~~~~~~~

1. Spark
2. Flink





References
------------------------


1. `Hadoop, Storm, Samza, Spark, and Flink: Big Data Frameworks Compared <https://www.digitalocean.com/community/tutorials/hadoop-storm-samza-spark-and-flink-big-data-frameworks-compared>`_

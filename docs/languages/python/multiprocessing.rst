Multi-Processing in Python
=============================


Python has built-in multiprocessing module in its standard library.

One simple example of using the Pool class is the following.

.. code-block:: Python

   def myfunc(myfuncargs):
       'some thing here'

   with Pool(10) as p:
       records = p.map(myfunc, myfuncargs)

However, there are limitations on this, especially on pickles. Another approach.

.. code-block:: Python

   from multiprocessing import Pool
   from multiprocessing.dummy import Pool as ThreadPool

   with ThreadPool(1) as p:
        records = p.map(myfunc, myfuncargs)

Beware that `map` function will feed in a list of args to the function. So I have to use `p.map(myfunc, [arg])` for one arg.


References
---------------------

1. `An introduction to parallel programming using Python's multiprocessing module <http://sebastianraschka.com/Articles/2014_multiprocessing.html>`_
2. `Parallelism in one line A Better Model for Day to Day Threading Tasks <http://chriskiehl.com/article/parallelism-in-one-line/>`_

Numerical
=================================

Modularize
---------------------------

1. Seperate physics from numerical stuff.


Speed
---------------------------------

1. `vectors` are convinient but slow. `Ref <http://en.cppreference.com/w/cpp/container/vector>`_
2. Do not copy arrays if not necessary. The example would be for a function return. Most of the times, we can pass pointer of array to the function and update the array itself without copying anything and no return is needed at all.
3. inline function.
4. Use `namespace` instead of class if no data structure is stored in it.

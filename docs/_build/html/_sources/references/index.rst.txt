References
=====================



C++
---------------------

Books
~~~~~~~~~

1. The C++ Programming Language
2. Programming Principles and Practice Using C++
3. The C++ Primer


Lectures
~~~~~~~~~~~~


1. `C++ Beginners Tutorial 1 (For Absolute Beginners) <https://www.youtube.com/watch?v=ki3B8a-jLrE>`_
2.  `C++ Programming <https://www.youtube.com/watch?v=Rub-JsjMhWY>`_
3. `Introduction to C++ <https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-096-introduction-to-c-january-iap-2011/>`_
4. `Coursear Course: C++ For C Programmers, Part A <https://www.coursera.org/learn/c-plus-plus-a>`_
5. `Top C++ Courses and Tutorials <https://www.udemy.com/courses/development/programming-languages/C-plus-plus-tutorials/>`_
6. `On SoloLearn: C++ Tutorial <https://www.sololearn.com/Course/CPlusPlus/>`_


Practice
~~~~~~~~~~~~~~~~~~~~

`SoloLearn <https://code.sololearn.com/#cpp>`_ provides `this code playground <https://code.sololearn.com/#cpp>`_ that we can use to test c++ codes.

Libraries
~~~~~~~~~~~~~~~


For solving differential equations:

1. http://headmyshoulder.github.io/odeint-v2/
2. http://www.mcs.anl.gov/petsc/
3. https://github.com/trilinos/Trilinos
4. http://homepage.math.uiowa.edu/~dstewart/meschach/meschach.html
5. http://www.boost.org/
6. http://www.feynarts.de/cuba/
7. https://www.gnu.org/software/gsl/


Linear algebra

1. http://www.simunova.com/mtl4


Comparison of libs

1. Boost is faster than GSL in terms of random numbers and odeint. `Source <https://dilawarnotes.wordpress.com/2016/04/21/benchmark-ode-solver-gsl-vs-boost-odeint-library/>`_


Julia
-----------------

Libraries
~~~~~~~~~~~~~~~~~~~~~~

1. https://github.com/JuliaDiffEq/DifferentialEquations.jl


Storage of Data
-----------------------

tl;dr: Use HDF5

1. HDF5
2. `BCOLZ <http://bcolz.blosc.org/en/latest/>`_ : not designed for multidimentional data.
3. `Zarr <https://github.com/alimanfoo/zarr>`_ : works with multidimensional data and also parallel computating.
4. `Blaze ecosystem <http://blaze.pydata.org/>`_

A article that compares HDF5, BCOLZ, and Zarr:`To HDF5 and beyond <http://alimanfoo.github.io/2016/04/14/to-hdf5-and-beyond.html>`_ 

I also recommend pandas. It is a python module that works very well with data. It even loads HDF5 out of box.

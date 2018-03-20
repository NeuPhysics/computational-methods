Numerical Basics
=====================

Precision, Error, etc
------------------------------------

Floating-point representation is

.. math::
   S\times M \times b^{E-e},

where S is the sign, M is the mantissa, E is the integer exponent, b is the base and e is the bias of the exponent.

**Round off** is the bias from the machine accuracy and it accumulates.

**Truncation error** is the difference between  the true answer and teh answer obtained. The reason for this is that we are doing numerical calculations by descretizing the functions. This error is the discrepancy on a ideal computer that n round off is present.

As the round off error gets magnified and finally swamp the useful answer in the calculation, the method is unstable. An algrimth like this can work on a ideal computer but not a practical one.


Recursive and Iterative
-------------------------



Solving problems with iterative and recursive methods are two different approaches somehow to the same kind of problems.

Here we are calculating the factorial of :math:`n`. Run the program on `Repl.it <https://repl.it/@emptymalei/recursive-iterative>`_ .


.. code-block:: python

   def recursiveFactorial(n):
     if n == 0:
       return 1
     else:
       return n * recursiveFactorial(n - 1)


   def iterativeFactorial(n):
     ans = 1

     i=1

     while i <= n:
       ans = ans * i
       i=i+1

     return ans


   print(recursiveFactorial(0))
   print(iterativeFactorial(0))

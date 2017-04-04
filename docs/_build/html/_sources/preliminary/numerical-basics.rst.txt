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

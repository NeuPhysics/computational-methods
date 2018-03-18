Neural Network and Finite Element Method
==============================================

We consider the solution to a differential equation

.. math::
   \mathcal L \psi - f = 0.

Neural network is quite similar to finite element method. In terms of finite element method, we can write down a neural network structured form of a function [Freitag2007]_

.. math::
   \psi(x_i) = A(x_i) + F(x_i, \mathcal N_i),

where :math:`\mathcal N` is the neural network structure. Specifically,

.. math::
   \mathcal N_i = \sigma( w_{ij} x_j + u_i ).


The function is parameterized using the network. Such parameterization is similar to collocation method in finite element method, where multiple basis is used for each location.


One of the choice of the function :math:`F` is a linear combination,

.. math::
   F(x_i, \mathcal N_i) = x_i \mathcal N_i,

and :math:`A(x_i)` should take care of the boundary condition.


.. admonition:: Relation to finite element method
   :class: note

   This function is similar to the finite element function basis approximation. The goal in finite element method is to find the coefficients of each basis functions to achieve a good approximation. In ANN method, each sigmoid is the analogy to the basis functions, where we are looking for both the coefficients of sigmoids and the parameters of them. These sigmoid functions are some kind of adaptive basis functions.



With such parameterization, the differential equation itself is parameterized such that

.. math::
   \mathcal L \psi - f = 0,

such that the minimization should be

.. math::
   \lvert \mathcal L \psi - f \rvert^2 \to 0

at each point.





References and Notes
-----------------------

.. [Freitag2007] Freitag, K. J. (2007). Neural networks and differential equations.

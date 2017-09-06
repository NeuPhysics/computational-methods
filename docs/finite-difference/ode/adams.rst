Adams' Method
===================

.. index:: Adams' Method

.. admonition:: Taylor Expansion of Functions
   :class: note

   Suppose we have a function :math:`f(x)`, Taylor expansion arround a point :math:`x_0` is

   .. math::
      f(x) = f(x_0) + f'(x_0) (x - x_0) + \cdots


   This is also named Maclaurin series.


For linear first ODE,

.. math::
   \frac{dy}{dx} = f(x, y),


This equation can always be written as a integral form

.. math::
   y(x_{n+1}) - y(x_n) = \int_{x_n}^{x_{n+1}} f(x,y) dx,

which is basically a very general idea of how to numerically solve such an equation, as long as we can solve the integral efficiently and accurately. In other words, we are dealing with

.. math::
   y(x_{n+1}) =  y(x_n) + \int_{x_n}^{x_{n+1}} f(x,y) dx.


The problem is how exactly do we calculate the integral or the iteraction. Two methods are proposed as explicit method (:index:`Adams-Bashforth Method`) and implicit method (:index:`Adams-Moulton Method`).


What can be done is to Taylor expand the integrand. At first order of :math:`f(x,y)`, we would have

.. math::
   y(x_{n+1}) = y(x_n) + \int_{x_n}^{x_{n+1}} f(x_{n},y(x_n)) dx =  y(x_n) +(x_{n+1}- x_n) f(x_{n},y(x_n)) ,


which is the Euler method. For simplicity step size is defined as

.. math::
   \delta x = x_{n+1}- x_n.
   :label: adams-method-step-size-def

Also to simplify the notation, we introduce the notation

.. math::
   y_n = y(x_n).


For second order, we have at least two different methods to approximate the integral.

.. index:: Adams-Bashforth Method
.. index:: Explicit Adams Method

- Adams-Bashforth method is to approximate the integral using

   .. math::
      \int_{x_n}^{x_{n+1}} f(x,y) dx \sim \frac{1}{2} ( 3 f( x_n - f( x_{n-1}, y_{n-1} ) , y_n) ) \delta x

   where we used the definition of step size :eq:`adams-method-step-size-def`.

.. index:: Adams-Moulton Method
.. index:: Implicit Adams Method

- Adams-Moulton method uses trapezoidal rule, which approximates the integral as

   .. math::
      \int_{x_n}^{x_{n+1}} f(x,y) dx \sim \frac{1}{2} f( x_{n+1} + f(x_n, y_n) , y_{n+1} ),

   which is similar to backward Euler method but of second order.


In fact the AB and AM methods to the first order are

- Adams-Bashforth Method First Order = Forward Euler Method;
- Adams-Moulton Method First Order = Backward Euler Method.


.. admonition:: scipy.odeint
   :class: hint

   `scipy.odeint` uses `adams` for nonstiff equations, where even higher order are used. The return infodictionary entry `nqu` shows the orders for each successful step.


Refs & Notes
--------------------

1. `Adams Methods @ MIT Web Course <http://web.mit.edu/10.001/Web/Course_Notes/Differential_Equations_Notes/node6.html>`_
2. `Adams' Method @ Wolfram MathWorld <http://mathworld.wolfram.com/AdamsMethod.html>`_

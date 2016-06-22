Euler Method
===================

.. index:: Euler Method

For linear first ODE,

.. math::
   \frac{dy}{dx} = f(x, y),

we can discretize the equation using a step size :math:`\delta x \cdot ` so that the differential equation becomes

.. math::
   \frac{y_{n+1} - y_n }{ \delta x } = f(x_n, y_n),

which is also written as

.. math::
   y_{n+1} = y_n + \delta x \cdot  f(x_n, y_n).
   :label: euler-method-discretized-form-y-n-plus-1

Generally speaking, a simple iteraction will do the work.

Integration of ODE
====================



Runge-Kutta
------------------



Adaptive Stepsize for R-K
---------------------------






Modified Midpoint Method
---------------------------------



.. math::
   z_0 &= y(x) \\
   z_1 &= z_0 + h f(x,z_0) \\
   z_{m+1} &= z_{m-1} + 2h f(x+mh,z_m) \\
   y(x+H) &\approx y_n = \frac{1}{2} \left( z_n + z_{n-1} + h f(x+H,z_n) \right) .


This method contains only the even powers of :math:`h` thus we can gain two orders of precision at a time by calculating one more correction.





Refs & Notes
-------------------

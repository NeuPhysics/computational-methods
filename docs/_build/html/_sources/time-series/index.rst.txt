Time Series Data
=====================


Short-Time-Fourier-Transform
----------------------------------


We Fourier transform the time series data using a Fourier transform, with some window function

.. math::
   \tilde Y[n,k] = \sum_m Y[n+m] W[m] e^{-i \lambda_k m},

where :math:`\lambda_k=2\pi k/N` and :math:`W[m]` is the window function at :math:`m`.






References and Notes
-----------------------------

`Cousera <https://www.coursera.org/learn/practical-time-series-analysis/lecture/pPtHq/course-introduction>`_

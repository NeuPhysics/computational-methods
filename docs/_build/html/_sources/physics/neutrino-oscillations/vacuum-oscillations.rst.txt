Vacuum Oscillations
=====================

.. admonition:: Choice of Unit
   :class: warning

   For numericall purpose, we choose to scale distance x using :math:`\omega`.

   Suppose we use MeV for energy scales, the distance :math:`\hat x = \omega x` is related to actually distance :math:`x` in km through

   .. math::
      x = \frac{\hat x}{\omega_v} = \frac{\hat x}{  1.90\times 10^{-4}  \mathrm{m}^{-1}  \frac{\delta m^2}{7.5\times 10^{-5}\mathrm{eV}^2} \frac{1\mathrm{MeV}}{E} } = \frac{\hat x}{0.190} \mathrm{km} \frac{7.5\times 10^{-5}\mathrm{eV}^2}{\delta m^2}  \frac{E}{1\mathrm{MeV}}.





The numericall system is

.. math::
   \frac{d\psi}{dx} = -i H \psi,

where :math:`\psi` is the wave function

.. math::
   \psi = \begin{pmatrix}
   \psi_0 \\
   \psi_1
   \end{pmatrix}

and :math:`H` is the vacuum Hamiltonian

.. math::
   H = \frac{\omega}{2}\begin{pmatrix}
   -\cos2\theta &\sin 2\theta \\
   \sin 2\theta & \cos 2\theta
   \end{pmatrix}.


Initial condition is set to be

.. math::
   \psi(0) = \begin{pmatrix}
   1 \\
   0
   \end{pmatrix}.

The theoretical prediction for survival probability of the first flavor is


.. math::
   P  = 1 - \sin^2 2\theta \sin^2 ( \omega x/2 ).

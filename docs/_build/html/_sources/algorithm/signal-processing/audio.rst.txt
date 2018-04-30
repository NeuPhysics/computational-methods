Audio
=======================

.. admonition:: Keywords
   :class: note

   1. Harmonic structure of sound
   2. Parson code of music
   3. Linear time-invariant theory
   4. Autocorrelation
   5. Noise
   6. Chirps
   7. DCT compression
   8. Discrete Fourier transform
   9. filtering
   10. convolution


Linear Time-Invariant System
-----------------------------

We describe the system with :math:`Y(t) = f(X(t))`, where :math:`X(t)` is the input, and :math:`Y(t)` is the output.

1. Linear: :math:`f(a X_1(t) + b X_2(t)) = a f(X_1(t)) + b f(X_2(t))`
2. Time-invariant: input :math:`X(t+\Delta t)` will produce the shifted signal :math:`Y(t+\Delta t)`.


LTI systems are memory systems, casual, real, and stable. Stable means the output won't reach infinite if the input is finite. It's bounded.




Impulse Response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Suppose we have a impulse :math:`X(t) = I(t)`, and output :math:`h(t)`.

Now we have another input :math:`X(t)`, we can ask that what would the output be if we put the input in the same environment as the previous impulse.

.. math::
   Y(t) = \int d\tau h(\tau) X(t-\tau).



Transfer Function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For the impulse response, the transfer function is obtained through the Laplace transform of the response,

.. math::
   \tilde h(s) = \mathscr L_s [ h(t) ].

With the response function, we know that the response with some other input that is set in the same environment is

.. math::
   \tilde Y(s) = \tilde h(s) \tilde X(s).






References and Notes
-------------------------

1. `Basic Sound Processing in Python | SciPy 2015 | Allen Downey <https://www.youtube.com/watch?v=0ALKGR0I5MA>`_, `AllenDowney/ThinkDSP <https://github.com/AllenDowney/ThinkDSP>`_, `Think DSP <http://greenteapress.com/wp/think-dsp/>`_
2. `freesound.org <https://freesound.org/>`_
3. `LTI Systems <https://brilliant.org/wiki/linear-time-invariant-systems/>`_

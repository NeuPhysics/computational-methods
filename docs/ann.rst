Artificial Neural Networks
================================================


Artificial neural networks works pretty well for equation solving.



Solving Differential Equations
-------------------------------------------------------------


The problem here to solve is

.. math::
   \frac{d}{dt}y(t)= - y(t),

with initial condition :math:`y(0)=1`.

To construct a single layered neural network, the function is decomposed using

.. math::
   y(t_i)& = y(t_0) + t_i v_k f(t_i w_k+u_k) \\
   &= 1+t_i v_k f(t_i w_k+u_k) ,

where :math:`y(t_0)` is the initial condition and :math:`k` is summed over.

.. admonition:: Articifial Neural Network
   :class: note

   THIS WILL BE NOTES FOR BASIC IDEAS OF ARTIFICIAL NEURAL NETWORK.



Presumably this should be the gate controlling trigering of the neuron or not. Therefore the following expit function serves this purpose well,

.. math::
   f(x) = \frac{1}{1+\exp(-x)}.

One important reason for chosing this is that a lot of expressions can be calculated analytically and easily.



.. admonition:: Fermi-Dirac Distribution
   :class: note

   Aha, the Fermi-Dirac distribution.



   
With the form of the function to be solved, we can define a cost


.. math::
   I=\sum_i\left( \frac{dy}{dt}(t_i)+y(t_i) \right)^2,

which should be minimized to 0 if our struture of networks is optimized for this problem.

Now the task becomes clear:

1. Write down the cost analytically;
2. Minimized cost to find structure;
3. Substitute back to the function and we are done.



Overfitting
-----------------------


It is possible that we could over fit a network so that it works only for the training data. To avoid that, people use several strategies.

1. Split data into two parts, one for training and one for testing. `A youtube video <https://www.youtube.com/watch?v=S4ZUwgesjS8>`_
2. Throw more data in. At least 10 times as many as examples as the DoFs of the model.  `A youtube video <https://www.youtube.com/watch?v=S4ZUwgesjS8>`_
3. Regularization by plugin a artifical term to the cost function, as an example we could add the . `A youtube video <https://www.youtube.com/watch?v=S4ZUwgesjS8>`_
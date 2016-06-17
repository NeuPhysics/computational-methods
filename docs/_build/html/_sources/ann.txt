Artificial Neural Networks
================================================


Artificial neural networks works pretty well for equation solving.



Universal Approximators
---------------------------------

Mawell Stinchcombe and Halber White proved that no theoretical constraints for the feedforward networks to approximate any measureable function. In principle one can use feedforward networks to approximate measurable functions to any accuracy.

However the convergence slows done if we have a lot of hidden units. There is a balance between accuracy and convergence rate. More hidden units means slow convergence but more accuracy.


Here is a quick review of the history of this topic.

.. admonition:: Kolmogorov's Theorem
   :class: note

   Kolmogorov's theorem shows that one can use finite number of carefully chosen continuous functions to exactly mix up by sums and multiplication with weights to a continuous multivariable fnction on a copact set.

   `Here is the exact math. <http://neuron.eng.wayne.edu/tarek/MITbook/chap2/2_3.html>`_



1. Cybenko 1989

Cybenko proved that 

.. math::
   \sum_k v_k \sigma(w_k x + u_k)

is a good approximation of continuous functions because it is dense in continous function space. In this result, :math:`\sigma` is a continuous sigmoidal function and the parameters are real.


2. Hornik 1989

"Single hidden layer feedforward networks can approximate any measurable functions arbitrarily well regardless of the activation function, the dimension of the input and the input space environment."
(http://deeplearning.cs.cmu.edu/notes/Sonia_Hornik.pdf)






.. admonition:: Dense
   :class: note

   Set A is dense in set X means that we can use A to arbitarily approximate X. Mathematically for any given element in X, the neighbour of x always has nonzero intersection.


.. admonition:: Measurable Function
   :class: note

   Basically it means continuous.




Refs
~~~~~~~~~~~~~~

1. Kolmogorov, A. N. (1957). "On the Representation of Continuous Functions of Several Variables by Superposition of Continuous Functions of one Variable and Addition," Doklady Akademii. Nauk USSR, 114, 679-681.
2. Maxwell Stinchcombe, Halbert White (1989). `"Multilayer feedforward networks are universal approximators" <http://www.sciencedirect.com/science/article/pii/0893608089900208>`_ . Neural Networks, Vol 2, 5, 359-366.




Activation Functions
--------------------------------------------------


1. Uni-Polar Sigmoid Function

.. math::
   \frac{1}{1+e^{-x}}

.. figure:: assets/sigmoidFunction.png
   :align: center

   Sigmoid function


2. Bipolar Sigmoid Function

.. math::
   \frac{1-e^{-x}}{1+e^{-x}}

.. figure:: assets/bipolarSigmoid.png
   :align: center

   Bipolar Sigmoid



3. Hyperbolic Tangent

.. math::
   \tanh(x) = \frac{\sinh(x)}{\cosh(x)} = \frac{e^{x} - e^{-x}}{e^x + e^{-x}}


.. figure:: assets/tanh.png
   :align: center

   Hyperbolic tangent


4. Radial Basis Function

.. figure:: assets/unnormalized_radial_basis_functions.svg.png
   :align: center

   Two unnormalized Gaussian radial basis functions in one input dimension. The basis function centers are located at x1=0.75 and x2=3.25. Source `Unnormalized Radial Basis Functions <https://en.wikipedia.org/wiki/Radial_basis_function#/media/File:Unnormalized_radial_basis_functions.svg>`_


5. Conic Section Function





Reffs
~~~~~~~~~~~~~~~~~~~~~~~~~~

1. `Performance Analysis of Various Activation Functions in Generalized MLP Architectures of Neural Networks  <http://www.cscjournals.org/manuscript/Journals/IJAE/volume1/Issue4/IJAE-26.pdf>`_







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




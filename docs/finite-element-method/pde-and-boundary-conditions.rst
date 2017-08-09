Differential Equations and Boundary Conditions
======================================================


Two Types of Boundary Conditions
----------------------------------

As an example, we have a partial differential equation

.. math::
   \frac{d^2u}{dx^2} + f = 0,

which describes a 1D problem.

* Dirichlet boundary condition: specify values for :math:`u`, such as :math:`u(0)=u_0` and :math:`u(L)=u_L`;
* Neumann boundary condition: specifiy values for :math:`u_{,x}`.

If we have only Neumann boundary condition, the solution is not unique. The example for it is tossing a bar, which can have both Neumann BC at both ends but it is moving.


Example Problems
-----------------------


Elasticity Problem
~~~~~~~~~~~~~~~~~~~~~


We consider the displacement :math:`u(x)` at each space coordinate :math:`x` of a elastic bar under some external force. The strain is proportional to :math:`u_{,x}`. The equation would be

.. math::
   -\frac{d\sigma}{dx} = f.


Heat Transfer
~~~~~~~~~~~~~~~~~~~~

Define temperature on a bar at each point :math:`u(x)`. Heat transfer is proportional to the head gradient, :math:`j= - \kappa u_{,x}`. The quation would be

.. math::
   - \frac{dj}{dx} = f.



Strong Form and Weak Form of PDE
----------------------------------

Strong form of differential equations is basically the original form we write down. Strong form requires each term to be well defined at each point. However, we can derive a weak form that require each part to be well defined through the whole domain only, which is a relaxed requirement.

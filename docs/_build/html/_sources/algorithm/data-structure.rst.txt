.. _data-structure:

Data Structure
==============================


Dealing with data structure is like dealing with your cloth. Some people simply randomly drop their cloth somewhere without thinking. But it takes time to retrieve a specific T-shirt. Some poeple spend some time fold and arrange their cloth. However that make it easy to find a specific T-shirt. It's always a balance between the computation time and the coding time.


Keywords
-----------------------------

This is meant for some kind of flash card keywords. I used to remind myself of the important concepts.

Binary Tree
~~~~~~~~~~~~~~~~~~~~~~~

0. Tree; Binary tree
1. Traverse a tree:

   a. Pre-order traversal: parent->left->right
   b. In-orer traversal: left->parent->right
   c. Post-order traversal: left->right->parent
   d. Level-order tranversal: top->bottom, by each level from left to right of the whole tree



Some Useful Data Structures
------------------------------

Array
~~~~~~~~~~~~

Array is accessed with indices.


Linked List
~~~~~~~~~~~~~~



The first element is **head** while the last element is **tail**.



Elements can be linked through two different ways, Signly Linked List or Doubly Linked List.

Each node of the singly linked list is assigned two fields, the first field is the value of the node, which stores the information we need, the second field is the link to the next node.

.. figure:: assets/data-structure/Singly-linked-list.svg
   :align: center

   Singly linked list illustration from `Wikipedia <https://en.wikipedia.org/wiki/Linked_list>`_.

Suppose we are solving the `Josephus problem <https://en.wikipedia.org/wiki/Josephus_problem>`_. Linked list is good for deletion, however it is computation consuming when it comes to the counting. On the other hand, array structure is good for determining which on to delete, but the deletion involves rearrangement of index the array which is time consuming.


Stack
~~~~~~~~~~~~~~~~~~~~~~~~~

Stack is good for adding new items and removing the most recent-added item. (`on Enki <https://enkipro.com//insight/58f77be3d2d15f373906a905>`_)

Stack data structure is Last in First out, aka LIFO. There are only two ways to change the stack, which are adding item to the stack and removing the item at the top.


.. figure:: assets/data-structure/Lifo_stack.png
   :align: center

   Stack from Wikipedia



Queue
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Queue is First in First out, aka FIFO. The name Queue explains itself quite well. In a line of queue, the first one in the line would be the first one served and removed from the queue. To add into the queue, we have the put the new guy at the end of the queue.

.. figure:: assets/data-structure/Data_Queue.svg
   :align: center

   Queue from Wikipedia


References and Notes
--------------------------

1. I learned some of these in enki app.

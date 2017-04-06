C++ Basics
===================



Make it Work
-------------------

Apart from the tranditional way of running C++ code, Jupyter notebook has a clingkernel that make it possibel to run C++ in a Jupyter notebook. Here is the post: `Interactive C++ for HPC <http://johntfoster.github.io/posts/interactive-c%2B%2B-for-hpc.html>`_.


Concepts
-----------------

1. Namespace

2. Operators: assignment operators (=,+=,-=,*=,/=,%=), increment/decrement operator (++x,x++,--x,x--), relational operators (>,<,>=,<=,==,!=), logicl operators (&&,||,!), left shift (<<), extration operator (>>, or right shift), understand the operator precedence
3. Variables: variable name starts with underscore or latin letters, Pascal case (PascalCase), Camel case (pascalCase)

4. if/else and Loops: if (condition is true ){ then something }

5. Data Types: string (double quote), character (char, 1 byte ASCII character, using single quote), float (4 bytes, always signed), double (8 bytes, always signed), long double (8 or 16 bytes, always signed), singed or unsigned short or long int (signed long int, unsigned int)

6. Pointers: ampersand (&) accesses the address, pointer is variable thus needs to be declared using asterisk ( * ), can be declared to be int or double or float or char (int \*pt; int\* pt; int * pt; )

7. Functions: overload, recursion

8. Class: identity, atrributes, method/behavior, access specifiers (private or public or protected, by default it is set to private), instantiation of object (creating object), constructor, destructor, encapsulation, scope resolution operator (TheClassYouNeed::somefunction() ), selection operator (dot member selection . used to access members, or arrow member selection ->, used to access members with pointer), composition (assemble a larger class using small classes), friend function (friend void aFunc(); to access private members), this pointer (this -> var, (*this).var ), operator overloading (using operator key), inheritance (Base class, Derived class), polymorphism, virtual function (using virtual key, useful in polymorphism, pure virtual function is virtual void attack() = 0;)

9. Function Templates:

10. Exceptions: try, catch, throw

Clarifications
~~~~~~~~~~~~~~~~~~~~~~~~


.. admonition:: Increment and Decrement Operator
   :class: note

   Increment/decrement operator has a very high precedence if applied from the left.

   .. code-block:: c++

      x = 2;
      y = ++x;
      // prefix: x=3, y=3; ++ is calculated first then assigned to y;

      a = 3;
      b = a++;
      // postfix: a = 4, b= 3; ++ is calculated after the asignment


.. admonition:: Omitted Curly Braces in if statement
   :class: note

   Omitted curly braces in if/else statement works if it has only one statement. If you like Python, this is an excellent practice.

   .. code-block:: c++

      #include <iostream>
      using namespace std;

      int main() {
         int i = 2, j=3;

         if (i > j)
            cout << "i>j";
         else
            cout << "j<=i";

         return 0;
      }


.. admonition:: Comparing Two Numbers
   :class: note

   .. code-block:: c++

      a < b ? a : b
      // output a if express a<b is true otherwise output b;




.. admonition:: default statement for switch
   :class: note


   default statement for swtich must be at the end of the statements of switch.


   .. code-block:: c++

      int age = 18;
      switch (age) {
        case 1:
          cout << "Baby";
          break;
        case 6:
          cout << "Boy";
          break;
        default:
          cout << "Oh yeah?";
      }


.. admonition:: strings and string library
   :class: note


   <string> library is necessay for string data type but it is also included in other libs such as <iostream>.

.. admonition:: Tips about Pointers
   :class: note

   To understand the ampersand and asterisk operators, we look at the following example.


   .. code-block:: c++

      int x = 2, y = 1, z=42;
      int  *ptrx, *ptry, *ptrz;
      ptrx = &x;
      ptry = &y;
      ptrz = &z;

      cout << z << endl;
      // 42; since it's a variable

      cout << ptrz << endl;
      // 0x28ff18; only for this run;  ptr is the memory address

      cout << *ptrz << endl;
      // 42; since dereference operator (*) is dereferencing it

      z = z + x;
      z = *ptrz + x;
      *ptrz = *ptrz + x;
      // all three are equivalent to z = z + x

      *ptrz = *ptrx + *ptry;
      // equivalent to z = x + y




.. admonition:: Function Overloading
   :class: warning

   Function overloading can be done by varying parameter types or number of parameters but not by change return type.


.. admonition:: Recursion in C++
   :class: note

   The best example for recursion is to calculate factorials.

   .. code-block:: c++

      int factorial(int n) {
         if (n==1) {
            return 1;
            // this is also called the base case;
         }
         else {
            return n * factorial(n-1);
            // recursion until the argument passed to factorial becomes 1 then it returns the base case;
         }
      }


.. admonition:: Passing Arguments to Function by Value or Reference
   :class: note

   Passing by value is what we usally do. The function essentially copies the value of the parameters. Thus any change of the parameters inside function doesn't change the original passed variables.

   Passing by reference is very different. It passes the pointer to the function and thus any change to the parameters will change the originally defiend variables.

   .. code-block:: c++

      #include <iostream>
      using namespace std;

      int addOne(int *ptr) {
         return *ptr += 1;
      }
      // defined to take pointers as parameters;

      int main() {

         int a = 42;
         // declare a variable which has a value 42;

         cout << "a is " << a << endl;
         // output the value of a before calling the function;

         cout << "addOne(a)" << addOne(&a) << endl;
         // the function return;

         cout << "a becomes " << a << endl;
         // since I used += in the function, the value of the parameters changed;

         return 0;
      }


.. admonition:: Defining Class
   :class: note

   When define class a semicolon is always attached to the end of it.

   .. code-block:: c++

      class TheClassYouNeed {

         //blablabla

      };
      // the semicolon


.. admonition:: Constructor in Class
   :class: note

   When we need to initialize some variables in the class, constructor is helpful.

   .. code-block:: c++

      #include <iostream>
      using namespace std;

      class TheClassYouNeed {

            public:
               TheClassYouNeed(int x) {
                  setWeight(x);
               }

               void setWeight(int x) {
                  weight = x;
               }

               int getWeight() {
                   return weight;
               }


            private:
               int weight;

      };

      int main() {

         TheClassYouNeed cs1(42);
         // constructor function will take the number 42 and pass it to weight;

         cout << cs1.getWeight << endl;
         // output the weight of object cs1;

         return 0;
      }



.. admonition:: Two Files to Write a New Class
   :class: note

   We usually write class seperately in different classes. In this case we need to create two files, TheClassYouNeed.h and TheClassYouNeed.cpp.

   In .h file we define the header.

   .. code-block:: c++

      #ifndef THECLASSYOUNEED_H // #ifndef = if not defined; prevents from defining twice;
      #define THECLASSYOUNEED_H // then we define this

      // the declarations of class

      #endif

   In .h file we declare everything while in .cpp we define the constructor/desctructor and functions/methods/behaviors.

   When creating object using the class in the main function, we need to

   .. code-block:: c++

      #include "TheClassYouNeed.h"


.. admonition:: Constants and Constant Objects
   :class: warning

   Constant variables have to be initialized on creation.

   Constant objects should also be initialized using constructor. So the class has to have a constructor in it even without any parameters. Constant objects can NOT call non-constant functions, thus the methods are defined to be constant functions.

   .. code-block:: c++

      /* in the header file of the class */

      // bla bla
      void yourFunctionHere() const;
      // bla bla

      /* in the source file of the class */

      // bla bla
      void TheClassYouNeed::yourFunctionHere() const {
         cout <<"Hello"<<endl;
      }
      // bla bla



.. admonition:: Initializaing Constant Variables in Class
   :class: note

   Have to use **member initializers** instead of the usual way.

   But friend function is **not** a member of the class.



.. admonition:: Passing Object to Function
   :class: note

   Need to pass the reference of the object to the function.

   .. code-block:: c++

      void yourFunction(TheClassYouNeed &anObject) {
      // bla bla
      }


.. admonition:: Derived Class Does Not Inherit All
   :class: note

   Constructors/destructors, overloaded operators and friend functions are not inherited from base class.

   Private members can not be accessed from derived class but **protected** members can be.


.. admonition:: Pure Virtual Functions in Polymorphism
   :class: warning

   When we use a pure virtual function in base class, the derived class must override it.

   Base class with pure virtual function can **NOT** be used to create objects. Thus these classes are called **abstract classes**.

   .. code-block:: c++

      virtual void attack() = 0;
      //this is a pure virtual function, which must be overrided;


Dynamic Memory
~~~~~~~~~~~~~~~~~~~~~~~~~

There are two basic concepts of memory in C++, the stack and the heap. Declared variables in all the functions used in a program use memory from stack while the heap is some pool of memory ready for dynamical allocation.

The stack memory is will be released when the function return at the last step. It is also FILO, aka first in last out.

To access the heap, we use the new operator.

.. code-block:: c++

   int *ptr = new int;
   // Allocate the memory for an integer on the heap; meanwhile returns the address for future use;
   // The memory can be accessed globally;
   // Needs to be freed later;
   // Can be resized using realloc();
   // can be deleted using delete ptr;

   cout << ptr << endl;
   // the address of the allocated memory

   *ptr = 42;
   // assign values to the memory

   cout << *ptr << endl;
   // 42; output the values at the memory

   delete ptr;
   // delete the value at the memory but the ptr is still there since it is stored in the stack memory;



.. admonition:: NULL
   :class: note

   Assign a ponter NULL when defining it is a good habbit.

   .. code-block:: c++

      int *ptr = NULL;

      cout << *ptr << endl;
      cout << ptr << endl;
      // none of them outputs anything

      ptr = new int[42];
      // allocate memory for an array of length 42;

      delete [] ptr;
      // delete the array that the pointer ptr is associated with;
      // [] means delete the array


   Functions should be declared in the file that calls the function if it's defined in another file. The declaration of function can be seperate from the definition of the function.

   .. code-block:: c++

      void goldHeart();
      // this is the declaration of the function; notice we have not defined it

      int main() {

         goldHeart();

         return 0;
      }

      void goldHeart() {
      // here is the definition of the function;
      }

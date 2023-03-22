This project is a mathematical exploration of Abstract Algebra
concepts, particularly involving polynomials operating on
different types of Python objects.  The code is all tested
using version 3.10 of Python.

The main concepts here are the following:
* commutative ring properties
* generalized single-variable polynomials
* Python dunder methods (e.g. `__add__`, `__mul__`, `__eq__`, etc.)
* abstraction under Python
* dynamic type checking
* unit testing

## Crash course in Abstract Algebra ##

If you already know what a "commutative ring" means in Abstract Algebra,
then you can skip to the next section. If not, let me assure you that
as long as you have some basic mathematical intuition, you do not need
to be scared by fancy terms.

Most of us learn basic integer arithmetic when we are fairly young.
We soon develop "number sense" after noticing that "9 + 7 == 7 + 9"
or "anything plus 0 just gives the same thing" or "3 + (7 + 20) == (3 + 7) + 20".

I can't remember which grade you learn this in, and it probably varies across
school systems, but most of us learn these properties some time during K-12:

* commutative property: a * b = b * a (e.g. 5 * 2 == 2 * 5)
* associative property: a + (b + c) == (a + b) + c (e.g. (1 + 2) + 3 == 1 + (2 + 3)) 
* distributive property: a * (b + c) == a * b + a * c

After we observe a bunch of concrete facts like 3 + 4 == 4 + 3 and 50 + 1 == 1 + 50,
we can appreciate the concepts on a more abstract level.  Algebra give us our
first real taste of abstraction in our math education, as we start stating facts
like "a + b == b + a for all a, b belonging to the class of integers".

At the university level, you can take a class called "Abstract Algebra" (or
some schools call it "Modern Algebra"), and then you just get even more formal
about the properties of numbers. And you actually get more abstract than simply
thinking about numbers--things that may not obviously look like numbers on the
surface may share properties with numbers.

A quick example of Abstract Algebra is that it gives a fancy name to a
fairly elementary concept. If you have to add a bunch of numbers together, as
long as you keep the numbers in order, it doesn't really matter how you group
the operations.  This is due to the associate property.  In Abstract Algebra
we say that integers combined with the addition operator (and the "identity"
element of 0) just exemplify a specific example of a **monoid**. (See
https://en.wikipedia.org/wiki/Monoid for more detail.)

Integers are more than just **monoidal over addition**.  The operations of
**mulitplication** and **addition** are monoidal, **commutative**, and
**distributive**.  And since we also have **additive inverses**, we call the
set of integers, along with the familiar operations of addition and multiplication,
a **commutative ring**.

It turns out you can make **rings** not only from integers, but also rational numbers,
real numbers, and complex numbers.  But **rings** don't have to even be numbers
in the traditional sense.  For example, you can form a ring from the set of
polynomials, and that is what I mostly explore in this project.

## Touring the code ##

The best place to start reading is [commutative_ring.py](./commutative_ring.py).

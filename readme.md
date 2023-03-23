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

## Dunder methods ##

We use the following "dunder" methods in Python.  "Dunder" is short
for double-underscore, and "dunder methods" are basically special
methods in Python.

* `__add__`: allow `a + b` syntax
* `__eq__`: allow `a == b` syntax
* `__mul__`: allow `a * b` syntax
* `__neg__` allow `-a` syntax
* `__pow__` allow `a ** exp` syntax

See these links for more detail:
* https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types
* https://docs.python.org/3/library/operator.html

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

* commutative property: `a * b = b * a` (e.g. 5 * 2 == 2 * 5)
* associative property: `a + (b + c) == (a + b) + c` (e.g. (1 + 2) + 3 == 1 + (2 + 3)) 
* distributive property: `a * (b + c) == a * b + a * c`

After we observe a bunch of concrete facts like `3 + 4 == 4 + 3` and `50 + 1 == 1 + 50`,
we can appreciate the concepts on a more abstract level.  Algebra give us our
first real taste of abstraction in our math education, as we start stating facts
like "a + b == b + a for all a, b belonging to the class of integers".

At the university level, you can take a class called "Abstract Algebra" (or
some schools call it "Modern Algebra"), and then you just get even more formal
about the properties of numbers. And you actually get more abstract than simply
thinking about numbers--things that may not obviously look like numbers on the
surface may share properties with numbers.

A quick example of Abstract Algebra is that it gives a fancy name (**monoid**) to a
fairly elementary concept. If you have to add a bunch of numbers together, as
long as you keep the numbers in order, it doesn't really matter how you group
the operations.  This is due to the **associate property**.  In Abstract Algebra
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

## Touring the code (warmup) ##

The best place to start reading is [commutative_ring.py](./commutative_ring.py).
That file constains verifier functions for various mathematical properties such
as the associate property (i.e monoids), the commutative property (aka symmetry),
the distributive property, and the existence of additive inverses.  When all
such properties are satisfied over a representative sample of values, you can
have some confidence that a Python value type acts as a **commutative ring**.

The next files to look at are [mod5.py](./mod5.py) and [pair.py](./pair.py),
which both implement relatively simple Python classes whose values satisfy
the properties of a ring. Both of these classes use dunder methods such
as `__add__` and `__mul__` to support natural mathematical manipulation.

And then there is [elephant.py](./elephant.py), which has the property that
it remembers how its values are constructed. Despite its lack of dunder methods
for `__add__` and `__mul__`, we will show that it can be adapted to work
with our polynomial class.

Next look at [bool.py](./bool.py), which serves as interesting counterexample
to most of our other classes.  We construct a Bool class that does not have
an additive inverse, so it does not qualify to be a ring. Instead, it is only
a **semiring**.  Nonetheless, despite `Bool` not having an additive inverse, it does
play nice with other data types in certain situations.

All of these classes are just a warmup for the main event.

## Polynomial classes

This project has several modules that allow you to construct and evaluate
polynomials with Python:

* [poly.py](./poly.py)
* [poly_bool.py](./poly_bool.py)
* [poly_elephant.py](./poly_elephant.py)
* [poly_integer.py](./poly_integer.py)
* [poly_mod5.py](./poly_mod5.py)
* [poly_pair.py](./poly_pair.py)
* [poly_poly.py](./poly_poly.py)
* [poly_poly_poly.py](./poly_poly_poly.py)

The key module here is [poly.py](./poly.py), which implements a class
called `SingleVarPoly`. It computes polynomials using **symbolic manipulation**,
and it uses **arbitrary math systems** to handle coefficients and values.
It relies on an `AbstractMath` object to provide methods for addition,
multiplication, as well as a few other things like the additive identity
(zero) and multiplicative identity.

All of the other `poly*.py` modules follow a fairly similar pattern:

* They create a subclass of `AbstractType`.
* They create a small wrapper class such as `BoolPoly` or `IntegerPoly`.
* They run some unit tests.

### Wikipedia links ###

* https://en.wikipedia.org/wiki/Additive_inverse
* https://en.wikipedia.org/wiki/Commutative_property
* https://en.wikipedia.org/wiki/Commutative_ring
* https://en.wikipedia.org/wiki/Distributive_property
* https://en.wikipedia.org/wiki/Homomorphism
* https://en.wikipedia.org/wiki/Injective_function
* https://en.wikipedia.org/wiki/Isomorphism
* https://en.wikipedia.org/wiki/Monoid
* https://en.wikipedia.org/wiki/Root_of_unity_modulo_n
* https://en.wikipedia.org/wiki/Semiring
* https://en.wikipedia.org/wiki/Surjective_function

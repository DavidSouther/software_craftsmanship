# Objects, Classes, and Object Oriented Design

In this chapter, we've looked at bundling data into objects. This allows using
a single variable to track complex data, accessing pieces of the complex data
via its properties. We looked at built-in objects representing dates and times,
and used those to build a calendar that showes us the days in a month, holidays,
weekends, and days until some event.

We then explored using classes and inheritence to describe, create, and simplify
object handling. With the rugs functions we've been using, we created a class
for each type of rug. Each rug type was able to do its own calculations on its
own contained data sets. There was still some duplication, so we introduced the
idea of inheritance - letting one class provide foundational behavior, and
several variations of that behavior in subclasses. This let us have clear,
concise, contained code for each type of rug, and our input and output utilities
didn't need large amounts of special casing.

With the understanding of creating and using objects, we added a technique to
track objects, their properties, and their lifecycle in our program traces. ...

We ended the chapter building a maze game. This gave us more practice with
classes, but more importantly, we used it as a jumping point for talking about
object and program design. We saw how using classes and objects let us write
clear code which shows its intent.

These first three chapters have given us the basic building blocks of writing
computer programs. From here, we will look at techniques for building programs
that are larger and more difficult to understand at one time. These tools will
aid in developing these larger programs in a systematic and verifiable way.

[Unit testing](../04_unit_testing/README.md)

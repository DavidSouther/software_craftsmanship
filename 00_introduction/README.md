# Introduction

Human endeavors rest on the backs of the hard-working crafters. From stone-
movers of the Egyptian pyramids to steel-workers on today's oil rigs, skilled
workers built civilization with their hands. Stone, steel, lumber, and leather
have for centuries been the foundation of human enterprise. In the 21st century,
there is a new medium demanding attention: information. The data flying across
the Internet is the backbone of international trade and commerce, and needs
skilled craftspeople to shape it. Yet even as professional carpenters build
masterwork cabinetry for law firms and movie stars, there are laymen working on
the same craft with the same tools in their garage. This is no less true for
computers  -  the relatively low cost of consumer software gives hobbyist
programmers the same tools to work with as the professional.

This book is aimed at those who are interested in this new medium as a
potential hobby or curiosity. The book begins assuming the reader knows how to
turn on and use their computer for basic tasks  -  email, word processing,
image editing, and video games, and takes them to a level where they will be
comfortable and confident in using and controlling their computers. This book
is very fast paced. Software development is a field which has undergone active
development for the past 80 years, yet did not exist beyond a dream before
then. There is a lot to learn about this craft, but readers who want to become
truly skilled at this craft will hopefully find this book gives them many of
the tools they need to feel comfortable working their computer. To get the
most out of the text,  I recommended readers work through the companion
workbook. Like any craft, to get good at software development you need to
develop software. The workbooks lead you through developing software, in a way
highlights the concepts presented in the text.

## Computers Are Tools

Information is a critical piece of today's infrastructure. How people  use
information is part of the field of Computer Science. Computer Science is on
the one hand deeply seated in mathematics, and on the other, firmly rooted in
practicality. The computer itself is simply a tool, like a band saw or plasma
torch, which does amazing things with this data. Whether used in large-scale
data mining and predictions for financial institutions, determining exactly
what websites have what content, or creating a side show of family photos. At
the end of the day, the laptop or desktop sitting in front of you is just a
piece of silicone, copper, and plastic, capable of doing only exactly what it
is told.

The task of the computer programmer is to tell the computer what to do. This
is not an easy task. When people think about a problem, we can start off being
a bit loose on how we describe the problem to ourselves. We can find issues or
errors in our assumptions, and change them on the fly. Computers cannot do
this. Every condition must be considered before hand. Say you're balancing
your check book. You add up $12.57, $52.45, and $1.99, but miss the decimal
on the $52.45, and end up with $5249.56  -  clearly an error. On paper, it
is obvious what you did wrong. The computer has no way of knowing this was an
error. Instead, it is up to the good programmer to tell the computer to verify
that any numbers typed into the financial program ends with a decimal and two
numbers. Then, the program can warn the user before making the calculation,
potentially avoiding a costly transaction.

### Using this tool

Software craftsmen use this tool by writing programs. A program is a document
both written and read by human beings, while telling the computer
unambiguously what to do. Take this example: `4 + 6 / 2`. Is the answer 7 or
5? If you remembered something like "Please Remember My Dear Aunt Sally" from
grade school, you would say 7. If you were a desk calculator in an
accountant's office, you would say 5. This statement is *ambiguous*  -  it
could mean more than one thing. The programmer's job is to decide if the
statement should be `(4 + 6) / 2 = 5` or `4 + (6 / 2) = 7`.

This is a pedantic exercise. As software gets more complex, software engineers
are responsible for deciding how the computer helps people interact with their
data. Consider the difference in organ donor rates between the United States
and Sweden. In the book [Nudge](http://nudges.org/), the authors contend the
difference is in "presumed consent" - that is, DMVs in the United States
require drivers to Opt In to being an organ donor, while Swedish DMVs require
patients to Opt Out. If you were writing a web page to take DMV registration
information, the difference in those conditions is eight characters - adding
"checked" to the Organ Donor input. With that minuscule change in a program,
the software craftsman has the potential for enormous influence on the lives
of millions of people.

### Sharing this tool

There is a whole world outside your front doorstep, and as much as some
programmers might want to deny it, at some point every craftsman's programming
will be used by someone else. It is important your code be both readable and
usable by these other craftsmen. There are many ways to do this, and many
great tools to facilitate this. While many software craftsman may want to
hoard their code, this is simply not possible. Even at companies like
Microsoft, the largest proprietary software development company on the planet,
teams are used because software projects, even most hobbyist projects, are too
large for one person to handle alone.

Many computer science courses ignore this aspect of programming, which I
believe is a real detriment to the students. Many computer science students
can go their entire undergraduate careers without ever looking at their peers'
code, and only having their program reviewed by the instructors. Craftsman of
all fields can drastically improve their work by meeting and sharing ideas.
Building partnerships with other craftsmen is one of the most rewarding ways
to practice a trade, but can also be a harrowing experience learning how to
work and interact with a completely new group of people. To work past this
impediment, I present tools for managing and sharing your programs early in
the book (Chapter 3, Source Control), and encourage you to find other
programmers and technology clubs in your area and on the Internet.


## Computer Languages

Computer languages are the tie between the world of everyday common sense
conversation and the exact stupidity of the computer. There are hundreds, if
not thousands, of different programming languages today. Many are "toy"
languages, built for a fun exercise or class project and are not intended for
wide-scale use. There are other languages that are proven as the workhorses
of computers, and are used everywhere from your cell phone to robots running
on Mars.

Languages are often classed based on their style of programming, and their
level of expressivity. There are, broadly, three styles of programming:
imperative, functional, and logical. Imperative languages are similar to a
cookbook recipe. They describe, one statement at a time, the "things" a
computer is to do - add two numbers, print those numbers to the screen, ask
the user for confirmation. C, JavaScript, and Python are all imperative
languages. Functional languages embrace the mathematics of computer science.
Functional languages often use similar syntactic constructs as imperative
languages, but with fundamental underlying differences. Haskell, Erlang, and
Lisp are functional programming languages. Logical programming languages have
little to do with either imperative or functional programming. Prolog is a
logical programming language. Logical programming will not be discussed in
this book.

Expressivity is notion for the ratio of amount of programming code written to
how much the computer does. Languages with the least amount of expressivity
are referred to as "low-level" languages  -  they must deal with all aspects
of the computer and its memory. "High-level" languages handle many of the
details of working on computer hardware, and let the programmer just focus on
expressing the logic of the program in question. This book is presented using
three different languages. These languages were chosen because they each
represent a very different approach to software craftsmanship. Each approach
is correct in  its own way, and it is important to know each of the approaches
to be a great software craftsman. Further, each of these three languages is
mature, and actively used in a variety of projects today.

### C

C started its life at Bell Labs in 1973. C was written by Dennis Kernighan and
Brian Ritchie as a language to write the Unix operating system. Before C,
operating systems (the program enabling all the other programs to run) were
written in an assembly language for each computer Unix would run on. However,
no two brands of computers had the same assembly language, so any time someone
wanted to run Unix on a new computer, they had to rewrite the entire operating
system. At the time, this could be thousands of lines of code. Today, it would
take millions of lines of assembly to code Windows or Linux. C was designed to
be a consistent language that, rather than being run on a computer as is,
would first be compiled into the appropriate assembly code.

C is widely considered the _lowest-level_ of today's common programming
languages, meaning C is as close to running "on the hardware" as you can get.
When writing C, the programmer has to deal with many aspects of computer memory
management. There are few utilities to achieve all but the most common tasks
(though there are a wealth of _libraries_ to fill the gap). C is the only
language used in this book that must be compiled before being run. This
_low-level_ nature of C makes it a very powerful language, especially when
faced with requirements to interact directly with hardware, or when hardware is
in short supply (embedded on robots or cell phones). That power comes with
great responsibility for writing the program correctly.

### Python

Python is a programming language developed by Guido van Rossum in the late
1980s. Python has gone through two major revisions since its first release,
and now is widely available on nearly any computing platform. Today, Python is
used by many Linux distributions to write a variety of their higher-level
tools. Organizations from Google to NASA use Python for numerous
mission-critical applications.

Python was designed to be a very flexible language, and as such is _high-level_
compared to C. Python was also designed to be a fun language to use - the name
Python refers not to the snake, but to Monty Python's Flying Circus. Python
has a certain culture around its use not seen in many other programming
languages. In Python, the prevailing wisdom is "there should be one - and
preferably only one - obvious way to do it."

### Javascript

Javascript is a programming language developed at Netscape in 1994 by Brandon
Eiche over the course of a week. Javascript is the de-facto standard for
writing programs served over the Internet to run in a user's web browser.
While actually a functional programming language, Javascript is often
(mis)represented as being an imperative language. This has lead to some very
poor code being written in the 15 plus years since its inception. That said,
its use in every web browser today has many people working to make Javascript
a less-maligned and better respected language.

Javascript is a very high level language. The programmer has few worries about
memory management, and no capabilities to access the computer's hardware
(though there are initiatives to enable such use). When combined with
libraries like jQuery, javascript can be the most expressive of the three
languages presented. When we start working with graphical programs later in
the book, Javascript's expressive power will really shine, in that the amount
of code needed to do the same thing (click a button) can often be an order of
magnitude less than a similar program in C.


#### Coffeescript
Coffee Script is a dialect of Javascript, developed by Jeremy Ashkenas at the
New York Times in 2009. Because of the rushed nature of the original development
of Javascript, Coffeescript aims to provide a streamlined syntax, while removing
many features of Javascript that are considered "harmful" by the community -
that is, features that allow or even encourage programmers to write code that
will perform incorrectly.

In the past five years, Coffeescript has seen tremendous growth, and is in my
opinion the most enjoyable of the languages to work in, though it does not have
quite the level of community support that Python has.

## Overview of the Text

### Syntactic Core (1-4)

The first four chapters will cover the core of writing programs. This will get
readers to the point where they can have their computer talking to them and
asking questions, though perhaps not gracefully. This section also covers the
basics of source control, and sharing code between developers.

### Programming Patterns (5-9)

The second section covers patterns in software craftsmanship - commonly used
ideas which can be the large building blocks of a program's design. This
includes discussions on modeling data, saving data, and some ideas on how to
make good program design decisions. This section also includes a chapter on
debugging - finding out what went wrong with a program (things will go wrong).

### Building Large Programs (10-13)

The last section deals with managing large pieces of software. The section
will go through building a basic "paint" application, where users can draw
lines and colors on a canvas, and save the painting to look at later. This
section also includes a chapter on how to work with other people on the same
project.

### Appendices: Tools for the Toolmakers

Any craftsman needs a workbench that suits their needs. The appendices address
several aspects around such a workbench. First and foremost, programs are
text. As such, it is important to use a text editor that facilitates looking
at and `seeing' your code. Second is a discussion of the Linux operating
system. Its open source nature encourages users to take responsibility for
their computer, and provides a wealth of tools for programming unavailable (or
at least difficult (read, costly) to acquire) on Windows. Finally, there is a
discussion on computer hardware. This is a look at what physically is going on
in your program, focusing on the CPU, memory, and some peripherals. This is
not strictly critical for learning software programming as a craft, but
hopefully you will be interested enough by the end of the book to want to take
a deeper look at what's going on.

## Practice

Like any skill, software craftsmanship takes practice. The workbooks are
designed to highlight the concepts presented in the text, while giving you an
opportunity to practice these skills. The workbooks are broken into lessons
roughly corresponding to sections of the main text. Each lesson has two parts.
The first part is a listing of code. You should type the code into your editor
exactly as written. Do not copy and paste the code. Much of programming
involves paying very close attention to a myriad of small details, and every
character has meaning. This discipline in typing code exactly as presented
will pay off in your programming future. The second part of each lesson is a
few exercises to work with the new concepts in the lesson, and combine them
with what you learned and wrote previously. Some of the lesson exercises will
involve conducting research on the Internet. Being able to find help with
programming questions is another invaluable skill as a software developer.

### Exercise: Hello World

If this is your first time programming, I'd recommend doing the exercises in
Python. If you've gotten through the book, try redoing the exercises in
Coffee, then C.

* [Intro: Python](./python/README.md)
* ~~[Intro: Coffee](./coffeescript/README.md)~~ Coming soon!
* ~~[Intro: C](./c/README.md)~~ Coming soon!

## [Next: Data Types](../01_basic_types_and_control_flow/README.md)

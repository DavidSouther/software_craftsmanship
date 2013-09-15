# Introduction

Welcome to the Software Craftsmanship Python exampels. These examples will
lead you through a variety of programming exercises in conjunction with the main
Software Craftsmanship lessons. Programming is a skill, and like any other skill,
it takes practice to become truly profficient. The exercises in these examples range
from "monkey-see-monkey-do" problems getting you used to typing exactly as a
computer expects, to free-ranging ideas on programs you might be interested in
writing for yourself. 

You will want to complete every "MSMD" section exxctly as written. Computers
are not forgiving when it comes to what you type in your program, and these
exercises are a safe way to begin exploring the world of computer programming.
The exercises for each chapter build on the MSMD section, and are opportunities
for you to apply what you've learned conceptually to a program. You should make
an attempt to complete all the exercises. Finally, projects are larger scale
ideas for programs that you would be able to write with the tools presented by
that point in the main text. The more you program, the better a programmer
you'll be, but you'll probably want to pick and choose projects that interest
you.

## python

Python is included with OSX, and every mainstream Linux distribution. 

_On Windows, you will need to [download](http://www.python.org/download/) and run
[the installer](http://www.python.org/ftp/python/2.7.5/python-2.7.5.msi)
([64-bit](http://www.python.org/ftp/python/2.7.5/python-2.7.5.amd64.msi))._


## First Program

### Terminal

Throughout the book, we will be using an editor and a command prompt almost
exclusively to write and run our programs, so we'll take some time now to work
through using each one. We'll start with the command prompt.

*Terminal? Command Prompt? Which is it?* It's both. It's a command prompt
because it's a program that Prompts you for Commands. It's a Terminal because
historically, the Terminal was at the end of a connection to a phone line that
the display and keyboard connected to the mainframe over. It is also sometimes
called a shell. The three terms are used interchangeably.

*TODO Add pictures for all of these.*

#### Linux

Most newcomers to Linux will be using Ubuntu Linux, so any linux instructions
are for Ubuntu. If you're using a different flavor, the instructions should be
straightforward to cross apply.

The command prompt in Linux is a terminal emulator. In Unity Dash, type Terminal
into the search box and the application will show up. Click it. When the program
launches, you will be prompted to enter a command with a `$ ` character. Type
`python --version`. You should see `Python 2.7.5`.

#### OSX

OSX includes an app called Terminal. It is either available under Applications /
System Tools, or through Spotlight.  When the program launches, you will be
prompted to enter a command with a `$ ` character. Type `python --version`. You
should see `Python 2.7.5`.

#### Windows

The windows terminal is a command prompt called 'command' or 'cmd', depending on
your version of Windows. To launch the command prompt in Windows Vista or later,
open the Start Menu, type cmd or command in the search box, and then click the
shortcut. When it opens, you should see `C:\Users\<your user>\ > `. Type `python
--version`. You should see `Python 2.7.5`.

### Editor


Let's write our first program. Open your text editor (gedit), and type the following:

```
print "Hello, world!"
print 2 + 3, 10/7, 152 * 12.6
```

Save the program on your hard drive with the name `hello.python`.

### Running the program
Open your console. Switch to the directory you saved the program in, and type `python hello.python`

```
Hello, world!
5 1 1915.2
```

Congratulations! You've written your first program!

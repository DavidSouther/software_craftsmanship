# Introduction
Welcome to the Software Craftsmanship Javascript Workbook. This workbook will
lead you through a variety of programming exercises in conjunction with the main
Software Craftsmanship book. Programming is a skill, and like any other skill,
it takes practice to become truly profficient. The exercises in this book range
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

## node.js
Javascript as a programming language started as a tool to make web pages
dynamic. While the web browser is still the most common platform for Javascript
to run (by an incredibly large margin), it is becoming more popular as a
general-purpose language. Still, it's not installed by default on many
computers, so we'll be installing a program called node.js to run your
Javascript.

The installer is available on Node's website for a variety of platforms. Go
to http://nodejs.org/download/ and choose the correct version, or use one of
these shortcuts.

* [Windows (64bit)](http://nodejs.org/dist/v0.10.15/node-v0.10.15-x86.msi)
* [OSX (64bit)](http://nodejs.org/dist/v0.10.15/node-v0.10.15.pkg)
* [Linux (64bit)](http://nodejs.org/dist/v0.10.15/node-v0.10.15.tar.gz)

Once node has successfully installed, you will need to install the Coffeescript
module. To do so, open a command prompt (either run.exe or command.exe on windows,
or Terminal on OSX or Linux), and type the following command:

```sh
npm install -g coffee-script
```

This will use the Node Package Manager to install coffee for use on the command
line. We will use npm again in [Chapter 5](../../05_object_extension/), when we
begin using external libraries, and cover it in depth in [Chapter 10](../../10_unit_testing)
when we begin building large programs.

## First Program
Let's write our first program. Open your text editor (gedit), and type the following:

### hello.coffee
```
console.log "Hello, world!"
console.log 2 + 3, 10/7, 152 * 12.6
```

Save the program on your hard drive with the name `hello.coffee`.

### Running the program
Open your console. Switch to the directory you saved the program in, and type `coffee hello.coffee`

```
Hello, world!
5 1.4285714285714286 1915.2
```

Congratulations! You've written your first program!

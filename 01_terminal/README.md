# The Unix Terminal

There is a world of confidence and power inside your computer, that you will
only discover when you begin learning the original tools people have been using
since the invention of the personal computer. Under the windows and webbrowser
and pretty graphics lives a world of text commands. In what would take a minute
to complete in Finder or Windows Explorer, I can do on the command line in 10
seconds (Moving some files, creating several folders). Something that would take
10 minutes could happen 10 or 20 seconds (renaming a half-dozen files). There
are still other things that are simply unexposed in a graphical format (changing
low-level system performance settings, editing every file in an entire folder
and all its subfolders at once, listing the name of every file in a folder and
its subdirectories that match some certain criteria (like having the phrase
'finalDraft' in the file's name).



## General Usage

*Terminal? Command Prompt? Which is it?* It's both. It's a command prompt because
it's a program that Prompts you for Commands. The command prompt itself is a
specific program on your computer - Unix usualy uses a program called "Bash" by
defaults. It's a Terminal because historically, the Terminal was at the end of a
connection to a phone line that the display and keyboard connected to the
mainframe over. Today, the terminal is the program that draws an actual window
on your desktop in which the command prompt runs and displays its output. The
command prompt is also sometimes called a shell. The three terms are used almost
interchangeably, and nearly lost all their nuance.

### OSX Specific 

In OSX, the first time through the book, we're going to use OSX' included
terminal program called, aptly, Terminal. It will run a shell called Bash. To
open it, find it either in the Utilities folder under the Applications folder in
Finder, or through Spotlight. It might also be a great program to pin to your
dock.

[./11_terminal_finder]

Terminal in a Finder window.

[./11_terminal_spotlight]

Terminal in Spotlight.

Once you've opened Terminal, you will see a mostly empty window.

[20_bash_Terminal]

Before we get any further, we're going to tweak this so it's much easier on the
eyes, and to work with in general. First, I would recommend expanding the window
with the plus, to take as much screen space as possible. Second, in settings,
choose a dark background color scheme. I personally like Pro - it colors well,
nothing conflicts badly, and it's easy on the eyes. Choose what you like best,
and click the "Default" button. Opacity is set at 85% on Pro, which means you
will be able to see through it a bit to the windows behind it. I don't like
this, so I set the opacity to 100%. It is also easier to program with a larger
font, I use Consolas at 18pt. It's easier to use a larger font for two reasons -
eyestrain goes down the larger the texts is, and fewer lines on the screen
encourages you implicitly to keep parts of your code smaller.

[21_color_scheme]

[22_opacity]

[23_fonts]

That covers the Terminal settings. Now we'll go and change some bash settings.
This is a little more indepth. Start by opening a file name `~/.bash_profile`
with gedit; the full command is `/Applications/




## File System

Now that the terminal has some reasonable settings, let's use it! The file
system is what you usually think about when you think of files and folders.
Since this is where all the computer's long-term data is stored, it's one of the
most common and basic things to work on in your computer. Nearly every thing you
do will involve in the file system in some way. Having a basic understanding of
the file system command will be your bread and butter throughout your future
Terminal experience.

### ls

The first command we'll use is called `ls`, short for 'List Directory Contents.'
It is one of the most 

### cd

### cwd

### mkdir

### touch

## Running Programs

### Path

### ./

### arguments

## Working with files

### grep

### find

## Shortcuts

### tab completion

# Installing gcc on Windows

On Windows, gcc is provided by a larger suite of programs called
[MinGW](http://www.mingw.org/). Get the latest version of the [MinGW
installer](http://sourceforge.net/projects/mingw/files/Installer/mingw-get-inst/)
that's available.

Run the installer. When you get to the screen called "Repository Catalogues",
choose the second option "Download latest repository catalogues". Choose the
default install folder, or choose your own location (I install to
`C://Program Files/MinGW`). On the "Select Components" screen, choose the
"C Compiler". When you run the install, you will see a command window open,
that will download the most up-to-date of each of the MinGW tools.

After the installer has completed, you will need to edit your system's path.
The path is a bit of information the computer keeps track of, that tells it
where to find programs that you want to run from the command line. To edit,
right-click on the "My Computer" icon (either on the desktop or in the start
menu), and click "Properties". In Windows 7, under the section "Computer name",
there is a link called "Change settings". Click that. Select the "Advanced" tab
(in the middle), and click the "Environment Variables..." button toward the
bottom. In the lower part of the window, under "System Variables", scroll down
the table until you see "PATH" in the Variable column. Double click that row.
An edit window will open. Copy the text in "Variable Value" into your text
editor. At the very end, add `;C://Program Files/MinGW/bin` (change the `Program
Files` part depending on where you installed MinGW). Paste this line over the old
value in the variable edit window, and click "OK" on each window until you're
back to the System window. Your MinGW installation is now complete.

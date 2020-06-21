# Libraries

In its three decades of life, Python has had a huge number of libraries written
for its systems. **Libraries** are bundles of code released by other teams,
companies, and developers to handle specific pieces of programming in a
consistent, shareable way. Libraries are released under a variety of
**licenses**, legal descriptions of how and when code may be used and
distributed by other developers who didn't author the code. All code we used is
released under a _permissive_ license which grants us the permission to
download, use, and in some cases modify the library _so long as_ we include a
copyright notice of & a link to the library.

Managing libraries can be a hassle. Libraries aren't just released one time and
then forgotten (usually). Instead, a library will be released. The developers
will continue adding new features, and release it a second time. Users will find
bugs, which will get fixed, but also need new releases. Over time, the
developers will remove old functionality that's no longer necessary to the
library - and release another version!

All these releases are different **versions** of the library with different
functionalities. While many versions of a library are interchangable, because
they have the same interface and not all users will be affected by all bugs.
However, some programs might rely on a bug being fixed in the library, or a
particular feature added.

## venv & pip

In python, we use two helper programs to manage libraries. The first of these
is `virtual environments`, or `venvs` for short. Up to this point in the book,
you've been able to get away with having all your programs as single files, and
all those files in a single folder. From here on, we're going to want to create
individual folders for each program so that they can be managed separately.

Within each folder, we will need to run a command to "initialize the virtual
environment". For any folder, this means one time running a command on the
command line. As an exercise, we'll start a new `rugs` folder. We're going to
add a library to handle _command line flags_ to set the area and perimeter
prices.

> If you need additional help working with your command line, I recommend
[this tutorial](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Understanding_client-side_tools/Command_line).

When you've made your `rug` folder, navigate there and run this python command:

```
python3 -m venv .venv
```

This will use python to set up a new virtual environment for this project. This
is a folder within our project that will keep all the libraries we install for
this program. Those libraries are kept in the folder `.venv`, which is the
argument at the end of the command. While you can change that folder, `.venv` is
pretty common.

> **Source Control** If you're using source control, you do not want to include
the .venv folder in your commits. If you're using `git`, you want to include the
line `.venv` in your `.gitignore` file. It you're using a different source
control tool, check your documentation.

For each project, you'll need to set up the venv once. After that, every time
you start working on a project in a new terminal session, you will need to
_activate_ the venv to use it.

On windows `cmd`, use the command

```
.\.venv\Scripts\activate.bat
```

On windows `powershell`, use the command

```
.\.venv\Scripts\activate.ps1
```

On Linux or Mac using the default terminal, use the command

```
source ./.venv/bin/activate
```

On other systems, [check the documentation](https://docs.python.org/3/library/venv.html).

You will need to run this activate command every time you open a new terminal
and begin working with the program.

### Installing libraries

With our virtual environment configured, we can install our first library. We
are going to use the [`absl`](https://pypi.org/project/absl-py/) library
(pronounced "ab-suhl" or "ab-sail") which provides features to process flags
from the command line. This will let us run our rug program and change the price
per area or perimeter for each run:

```
python3 rugs.py --area_price=3.5 --perimeter_price=2
```

To install this library, we use a tool called `pip`.

```
python3 -m pip install absl-py
```

When this has finished, we will be able to load the `absl` library in our python
file and use it for our flags.

# absl flags

```python
from absl import app
from absl import flags

flags.DEFINE_float("area_price", 5, "Price per square foot of a rug")
flags.DEFINE_float("perimeter_price", 1.5, "Price per foot of rug fringe")

FLAGS = flags.FLAGS

class Rug():
    # ... All methods except `cost` are the same

    def cost(self):
        area_cost = self.area() * FLAGS.area_price
        if self.has_fringe:
            perimeter_cost = self.perimeter() * FLAGS.perimeter_price
        else:
            perimeter_cost = 0
        
        total_cost = area_cost + perimeter_cost
        return total_cost

# Other classes are the same

def main(argv):
    # Input loop is the same, just add the `argv` above.

if __name__ = "__main__":
    app.run(main)
```

```
PS software_craftsmanship\05_input_output\01_flags> python3 rugs.py --area_price=12.5
Price another rug (Y/n): Y
1) Square Rug
2) Rectangular Rug
3) Circular Rug
Which type of rug? 1
Should this rug have fringe (y/N)?
Side length of this square rug? 5
This square rug costs $312.50 without fringe.
```
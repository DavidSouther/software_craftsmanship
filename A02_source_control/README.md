# Source Control

"But my program was working yesterday!"

A scream of anguish heard many times in many computer labs throughout the world.

"What did you change since then?" is the common reply. But of course, "I don't
know!" is the invariable conclusion.

Software engineering is the art and craft of creating text documents which
precisely specify the behavior of a computer program. That text changes over
time, and is changed by numerous authors. A critical piece of tooling that the
craft has developed is **Source Control**. Source control is a set of tools and
practices which track who made what changes to a program file over time, and
allow reviewing, auditing, and automating a number of aspects of a software
project.

You are going to learn how to make effective use of these tools from the very
beginning of your journey!

## Tracking

At its core, source control is about tracking changes to a code base over time.
It does this by recording every file's contents at various points in time, and
keeping all those versions and changes over time in order. Because code is often
authored by a number of contributors, source control also helps teams organize
and resolve any conflicts - changes to the same part of the codebase by
different authors. Today's source control tools also allow you to track
individual streams of work as you go about your development.

For this book, I'm going to recommend using the git source control tool. It is
widely used across the industry, has extensive support from a number of
different organizations, and many more aspects of source control and project
management than you will need at this point in your journey. In addition to the
git tool itself, I'll suggest using github.com to share your project, the GitHub
desktop client to interface with git itself, and will also point out that VSCode
has phenomenal support for using git built-in. You'll never need to leave VSCode
if you don't want to!

Before we get started with git and GitHub Desktop, let's go over a few concepts.
Git tracks source code in a **repository**. This is really just a fancy way of
saying a folder and all the directories inside of it that are managed by git. A
project can have any number of git repositories - one on your computer, one that
is backed up and shread on github.com, one on each of your colleagues'
computers, and in some cases, one copy on github for every colleague! Each copy
of a repository like this is called a **fork**.

As you edit code, you will likely save your files often. But we don't capture
every single save in the repository. Instead, you decide when you've made a good
amount of progress, and then you decide to snapshot some or all of those changes
at once. This is called a **commit**, and is the basic unit of tracking changes
in a project or repository. When you create a commit, you give it a one-line
short summary, and optionally a longer description. Learning to write a good
_commit message_ is an artform in itself, and if you look at the git history of
this book, you'll see that yours truly is sometimes very good about commit
messages. Other times... "Update README.md" does show up a lot!

Working alone, the only person you (in)convenience with a short message is
yourself, but as you start to work in teams, you should spend time thinking
about your commit message and the other people who will need to read it. 

So now you've edited some code (a chapter or two's worth at this point!) and you
are ready to makr your commit. Using your tool of choice, you'll first review
the **diff** (short for difference) in the files you've edited. This will show
up in all our tools as (usually in light red) lines you'd removed and (usually
in light green) lines you've added. If you only removed or added a line, it will
be red or green. If you modified one or more lines, you will see pairs of red
and green lines - the red line that was the old version of the code, and the
green line that is your updated version. 

Let's get started!

[GitHub Desktop](https://desktop.github.com) - you will probably want to create
an account on github as well, as you will be encouraged to share your work - but
certainly not required to do so!

I'm going to leave you with GitHub Desktop's excellent
[documentation](https://help.github.com/en/desktop). Install it and set up a new
local project (either one for the book, or better (to get more practice) one for
each chapter). Commit the current state of your code as-is. Edit your code a bit
and see how it changes.

[VSCode git](https://code.visualstudio.com/docs/editor/versioncontrol#_git-support)
is also excellent documentation, if you want to use VSCode's built in git tool,
in the lefth-hand icon menu.

## Branching

At this point, you probably only have one stream of work you want to do, and
this workflow will serve you just fine for most of the book. However, there are
times when you might have two different things you want to be working on in a
project at the same time (we're talking over a few hours or days). Maybe you're
developing a new feature, and you come across a bug that you want to fix that's
unrelated to this feature. To make this possible without needing to constantly
be focused on keeping the two parts of work in tandem, you can creat a
**branch**. A branch is like a mini-fork - you choose some commit to start from,
you add commits based on that (which branch out from the main set of code), and
then you can switch branches to put that work aside and come back to it later.
When you are finished with a branch, you can perform a **merge** to bring all
the changes from one branch back into another. This will create a new commit in
the main branch (the one you started from) which includes all the commits that
happend concurrently between the two. It might also need you to resolve any
_merge conflicts_, if both branches edited the same bit of code.

The first time you see a merge conflict it can be a bit scare and daunting. Take
a deep breath, and carefully think through what's happening. On two separate
streams of work, one file was edited in contradictory ways. The tooling will
show you both original versions, as well as what it thinks is the best guess to
resolve them. Your task is to either agree with the tools, or come up with an
edit that choose the correct behavior between the options available. It sounds
like a lot, but with a bit of thought and patience you'll be merging with
confidence!

Once you start using branches, there are a huge number of "workflows" which
advertise various benefits and drawbacks for managing a project. For now, I'd
recommend sticking with one master branch (the default branch when you start a
project), and just working in it as you develop one feature at a time. Then,
when you find a bug that you want to go back and fix, start a new branch
`bug-whatever`, do your work to fix the bug, merge the branch back into master,
and delete the branch.

When we get towards the end of the course and begin working in teams, we'll look
at more complex workflows that help teams collaborate effectively.
 
## Sharing

There are many reasons to share your code. For personal projects, it's good to
have a safe backup in the cloud. For team projects, you need to use some kind of
sharing to send and review changes among the team members. If you're following
this book as part of a classroom setting, your instructor will likely have you
submit exercises using a shared git repository. If you're uncomfortable about
sharing your code publicly, GitHub offers individual users unlimited free
private repositories.
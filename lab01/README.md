# Lab 01

## Due: Week 1, Sunday, 5:00 pm

## Value: 2 marks

## Aim

* Become familiar with course practices for labs
* Learn how to use GitLab effectively
* Learn how to create and run a Python program via the command-line.
* Introduce simple Python exercises based on topics covered in week 1

# Preamble

For this and all future labs you *must* submit your lab work by the deadline in order to get marked. Each lab is worth 2 marks. For this and many of the future labs, you will need to show your work to your tutor or assistant tutor in either the lab in which it is done or the subsequent lab. They will provide you feedback and give you your marks.

Submission instructions are at the end of the exercise below.

# Setup

## 1. GitLab

An individual repository for you for this lab has been created for you on the CSE GitLab server. You can find it at this URL (substituting z5555555 for your own zID):

https://gitlab.cse.unsw.edu.au/z5555555/19T3-cs1531-lab01

You will need to log in with your zID and zPass. If you are unable to login please speak to your tutor or lab assistant.

If you're familiar with GitHub then you should find GitLab very similar. You'll observe that there is a copy of these instructions in the repository (`README.md`) as well as a few files and folders relating to this lab exercise.

Feel free to browse GitLab in order to familiarise yourself with it. If you're not familiar with git, the following sections should help get you started with learning it.

## 2. Adding Your SSH Key to GitLab

The following steps **must** be performed by running the commands on the CSE system. If you wish to work from your own computer, you must **also** do the same from there.

1. You need to add your CSE ssh key to your gitlab.cse.unsw.edu.au account. Here is how you do that:
First print your CSE ssh key. If you have one, this command should should work.

    ```
    $ cat ~/.ssh/id_rsa.pub
    ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAyNSzIDylSPAAGLzUXdw359UhO+tlN6wWprSBc9gu6t3IQ1rvHhPoD6wcRXnonY6ytb00GpS4XRFuhCghx2JNVkXFykJYt3XNr1xkPItMmXr/DRIYrtxTs5sn9el3hHZIgELY8jJZpgIo303kgnF0MsB7XpqCzg7Iv6JGkv7aEoYC/MNr07hXE8iQjYIHDMdO9HxGI80GyMqb1hF+RSpQTNvXQvH56juu9VXt5OwJjOqSVa4SfsEICqdn+3k9w8Z4EaD93Eeog3hz0RoTrme8h/sJenXydJ0w9ZOs0By4fjqKFYPsYEs1K6SHma+kPByZM9COgKHZwOZHH1m24HOITQ== z5555555@williams
   ```

2. If you couldn't print an ssh key with the above command, you need to generate a new ssh key. You can do it like this (just hit return for each question).

    ```
    $ ssh-keygen
    Generating public/private rsa key pair.
    Enter file in which to save the key (/import/kamen/3/z5555555/.ssh/id_rsa):
    Created directory '/import/kamen/3/z5555555/.ssh'.
    Enter passphrase (empty for no passphrase):
    Enter same passphrase again:
    Your identification has been saved in /import/kamen/3/z5555555/.ssh/id_rsa.
    Your public key has been saved in /import/kamen/3/z5555555/.ssh/id_rsa.pub.
    The key fingerprint is:
    b8:02:31:8b:bf:f5:56:fa:b0:1c:36:89:ad:e1:cb:ad z5555555@williams
    The key's randomart image is:
    ...
    ```

3. To add your key to GitLab go to https://gitlab.cse.unsw.edu.au/profile/keys/
4. If you're asked to log in again, do so.
5. Cut-and-paste your ssh-key (the entire 200+ character line printed by cat ~/.ssh/id_rsa.pub) into the "Key" field. Don't cut-and paste z5555555's ssh key above - cut-and-paste your ssh-key! The title field should be filled in automatically.
6. Click the green **Add Key** button

# Using git

This exercise is intended to help you familiarise yourself with git. If you've not used git before, it can take a while to get used to it and learn how it works. Make sure you understand exactly what you're doing in the following exercise. **DO NOT BLINDLY ENTER IN THE COMMANDS WITHOUT KNOWING WHAT THEY DO.**

## Getting git

Git is a distributed version control system. It allows you to record changes to a set of files over time and synchronise those changes across many *repositories*. You've already seen one git repository earlier in the lab: the one stored at `gitlab.cse.unsw.edu.au`. You don't have direct access to that computer, so in order to make changes to files contained within it, you need to copy it to a *local* repository. You can make changes to this local repository then "push" those changes to GitLab. To do that however, git needs to be installed and configured:

1. If git is installed on the computer you are using. You can do this by running:
    ```bash
    $ git status
    ```
    If it is installed you will see something like
    ```
    fatal: Not a git repository (or any of the parent directories):
    ```
    If you do not have git installed, you will see something like
    ```
    bash: git: command not recognized
    ```
    If this is the case, you will have to set it up using the following instructions
    - **Linux** - Follow instructions at https://git-scm.com/download/linux
    - **Mac** - Either download from https://git-scm.com/download/mac or install via Homebrew or similar.
    - **Windows** - Download from https://gitforwindows.org/

    There are other means of getting git for all of these platforms. You are free to use whatever means works best for you.

2. Configure git if you have not used it before. The following commands will do that.
    ```bash
    $ git config --global user.name "Your Name"
    $ git config --global user.email "email@example.com"
    ```

## Cloning

Cloning a *repository* (a repository or repo is just a directory that is linked with git) copies to your computer all the files in the repo as well as a complete history of what changes, or *commits*, created those files. Cloning a repo is necessary before you can start making your own changes.

For each lab and assignment in this course, a repo will be created for you on *GitLab*. You will use it to store your work as you complete it. To clone this week's repo run (once again, replacing z5555555 with your own ZID):

```
$ git clone gitlab@gitlab.cse.unsw.EDU.AU:z5555555/19T3-cs1531-lab01.git
$ cd 19T3-cs1531-lab01 # To navigate into the directory
```

## Making a commit

Now that you have cloned the repo, you are ready to work on the codebase locally.

A commit represents a set of changes to the files in a repository as well as a message describing those changes for human readers. A good use of git involves a lot of commits with detailed messages.

Before you can commit, you have to *stage* your changes, effectively telling git what changes you actually want to commit and what changes you don't.

Making commits doesn't actually replicate your changes to the remote repository on GitLab. For that you need to *push* your commits, uploading them to the remote server. When collaborating with others, it is important not only to commit frequently, but also to push often.

In general, the commands to commit and push are as follows:
```bash
$ git add [files_to_commit] # Stage
$ git commit -m"Detailed message describing the changes" # Commit
$ git push # Push
```

Follow these steps to see them in action:

1. Add a new file called `first.txt` in the repo directory
2. Add a line of text to the first.txt file using your favourite text editor and save.
3. Go back to your terminal and enter the following commands:

    ```bash
    git add first.txt
    git commit -m "Added a line to the first file"
    git push
    ```

4. **MAKE SURE YOU UNDERSTAND THE PURPOSE OF EACH OF THE 3 ABOVE COMMANDS!** If you are unsure about any of them, ask your tutor or lab assistant.
5. Go back to GitLab and confirm that your changes have been pushed to the server.

## Working with others

Usually when you are using git, it is in a team. That means that you will not be the only one who is making the changes. If someone else makes a change and pushes it to the server, your local repo will not have the most up to date version of the files. Luckily, git makes it easy to update our local copy with the `git pull` command.

This command checks the remote server that your local repo is linked to and makes sure that all of your files are up to date. This ensures that you don't accidentally do things like implement the same thing someone else has already done and also lets you use other people's work (e.g. new functions) when developing.

Pulling regularly is one of the **most important** practices in git!

Unfortunately, at the moment you are just working individually. But GitLab still gives us a nice way to practice a `git pull`.

**Summary:**

1. View your repo on GitLab.
2. Click on the `first.txt` file
3. Click 'Edit' on the right-hand side.
4. Make some small change to the line of text and click the ‘Commit Changes’ button at the bottom of the screen.
5. This will have changed the `first.txt` file on the server but not on your local environment. To fetch these changes use the git pull command from your terminal
6. Confirm that your version of `first.txt` now has the changes you made on the web site

## Branching

**Branches** are a vital part of git and are used so people can work on separate parts of the codebase and not interfere with one another or risk breaking a product that is visible to the client. Breaking something on one branch does not have an impact on any other.

Good use of git will involve separating parts of the project that can be worked on separately and having them in their own feature branch. These branches can then be merged when they are ready.

Useful commands for branches:

```bash
$ git checkout -b [new_branch_name] # Create a new branch and switch to it
$ git branch                        # List all current branches
$ git checkout [branch_name]        # Switch to an existing branch
```

Follow these instructions to create a branch:

1. Make your new branch with: `git checkout -b first_new_branch`
2. List your branches to see that you have indeed swapped (use the above commands)
3. Make another change to the `first.txt` file
4. Try to push your changes to the server using the commands you learnt in the _Make your first commit_ section
5. The above step should have given you the following error:

    `fatal: The current branch first_new_branch has no upstream branch.`
    This means that the branch you tried to make a change on doesn't exist on the server yet which makes sense because we only created it on our local machine.
6. To fix this, we need to add a copy of our branch on the server and link them up so git knows that this new branch maps to a corresponding branch on the server. This command will do that:

    `git push -u origin first_new_branch`

**Note:** The final step only needs to be done for the first time you try to push using a new branch. After you have run this once, you should go back to simply using git push

## Merging

Merging branches is used to combine the work done on two different branches and is where git's magic really comes in. Git will compare the changes done on both branches and decide (based on what changes were done to what sections of the file and when) what to keep. Merges are most often done when a feature branch is complete and ready to be integrated with the master branch.

Since we have finished all that we are going to do (and believe there are no bugs) on our *first_new_branch* we can merge it back into master.

**NOTE**: It is strongly recommended, both in this course and in general, to always ensure the code on the `master` branch works correctly and is free of bugs. This is not always easy to achieve, but you should endeavour to keep master as *stable* as possible.

Another recommendation is to merge master into your branch *before* merging your branch into master as this will ensure that any merge into master will go smoothly.

In general, merges are done by:

```bash
git merge [target] # Merge the target branch into the current branch
```

**Note:** A successful merge automatically uses the commits from the source branch. This means that the commits have already been made, you just need to push these to the server (`git push`)

To merge your changes from above:
1. Switch back to the `master` branch using one of the commands from the above section
2. Merge in the changes you made in the other branch

    `git merge first_new_branch`

3. Push the successful merge to the server to update the master branch on the server

## Merge conflicts

Merge conflicts are the one necessary downside to git. Luckily, they can be avoided most of the time through good use of techniques like branches and regular commits, pushes and pulls. They happen when git cannot work out which particular change to a file you really want.

For this step we will engineer one so you can get a taste of what they are, how they occur and how to fix them. This will be the LAST time you will want one. The process may seem involved but it is quite common when multiple people are working at a time.

Follow these steps:

1. Add a line to the top of the `first.txt` file (on *master branch*)
2. Add, commit and push your changes
3. Switch to your `first_new_branch`
4. Add a different line to the top of the `first.txt` file
5. Add, commit and push your changes
6. Merge master into your current branch
7. This sequence of steps should made a merge conflict at the top of the `first.txt` with the following output
`Auto-merging first.txt`
``CONFLICT (content): Merge conflict in first.txt``
``Automatic merge failed; fix conflicts and then commit the result.``

## Resolving a merge conflict

Resolving a merge conflict is as simple as editing the file normally, choosing what you want to have in the places git wasn't sure.

A merge conflict is physically shown in the file in which it occurs.
`<<<<<<<` marks the beginning of the conflicting changes made on the **current** (merged into) branch.
`=======` marks the beginning of the conflicting changes made on the **target** (merged) branch.
`>>>>>>>` marks the end of the conflict zone.

E.g.

```
This line could be merged automatically.
There was no change here either
<<<<<<< current:sample.txt
Merges are too hard. This change was on the 'merged into' branch
=======
Merges are easy. This change was made on the 'merged' branch
>>>>>>> target:sample.txt
This is another line that could be merged automatically
```

This above example could be solved in many ways, one way would be to just use the changes made on the target branch and delete those made on the current branch. Once we have decided on this we just need to remove the syntax. The resolved file would be as follows

```
This line could be merged automatically.
There was no change here either
Merges are easy. This change was made on the 'merged' branch
This is another line that could be merged automatically
```

We would then just commit the resolved file and the merge conflict is finished!

To fix the conflict you created:
1. Open the `first.txt` file and decide which change you want to keep
2. Remove the merge conflict syntax
3. Add, commit and push the resolved merge conflict

## Testing

Checkout `master` and merge `first_new_branch` back into it. You can now run the `test_git.sh` file to check whether you have done most of the git exercises.

# Python Introduction

## Setup

To proceed to the second part of this lab, you must have access to Python version 3.7. It is available on the CSE computers via the `python3` command, which is what these instructions assume you will be using, but you're encouraged to set up Python on your personal computer.

While it's your responsibility to determine the best way to install software on your own devices, we provide the following information to give some guidance.

For **Mac** users:
 * Mac OSX comes with a version of Python already installed, but it is v2.7 so is **NOT** suitable for this course.
 * [This guide](https://docs.python-guide.org/starting/install3/osx/) describes how to install Python 3 via Homebrew and is a popular means of doing so.
 * Alternatively, you can get it from the [Python website](https://www.python.org/downloads/release/python-374/).

For **Windows** users:
  * There are various means to get a UNIX like environment on Windows ([CSE Ubuntu](http://mirror.cse.unsw.edu.au/pub/cseubuntu-vm/) in a VM, Cygwin, WSL, etc.). It's usually not hard to install Python 3.7 into one of them.
  * The official release is available from the [Python website](https://www.python.org/downloads/release/python-374/), if you don't know how to install software in your existing set up.

For **Linux** users:
  * On newer Debian and Ubuntu-based systems Python 3.7 can be obtained via `sudo apt-get install python3.7`.
  * If you're using something else, we assume you already know how to install the right version of Python.

## Hello Python

Create a new branch called `python_exercises` to complete the following exercises. Remember to merge back into master when you are finished.

You have been introduced to python in week 1 so we will just get familiar with creating and running simple python programs. Python is an interpreted language so does not require compilation like C does. That means executing python programs is as simple as one command.

**Summary:**

1. Open the `hello.py` file.
2. Complete the file so it prints "Hello World"
3. Run it from the command line

    ```bash
    python3 hello.py
    ```

4. Commit your changes

## Integer addition

Python lists are probably the most used data structure that comes out of the box with python. Assuming you are familiar with arrays in C, they are similar in that they are an ordered data structure supporting efficient random access. Unlike arrays, however, they are able to grow dynamically meaning their size does not need to be declared up front.

We will use a list to add up some integers in this exercise. (HINT: the python documentation is extensive and tells you how to use much of the built-in functionality. [https://docs.python.org/3.7/tutorial/datastructures.html](https://docs.python.org/3.7/tutorial/datastructures.html) )

**Steps:**

1. Open the `integers.py` file
2. Line 1 has declared a list of integers. You are required to add the number 6 to the list (using the `append` function) and then add all of the numbers up using a `for` loop and print out the result
3. Make the required edits to complete the above goal and run the `integers.py` in the same way you ran `hello.py`
4. At the bottom of the file add the line

    ```python
    print(sum(integers))
    ```

5. Note that the answers should be the same. This is an example of one of Python's inbuilt functions. It is important to remember that Python comes with many built-in functions for common operations. They should be favoured over "reinventing the wheel" and implementing them yourself.

## Strings

Unlike a C string, a string in Python is not merely a pointer to a block of NULL-terminated characters (Python does not have pointers), but rather a built-in datatype similar to a list. They also have a lot of in built functionality like concatenation (appending one string to another) and making all characters lower case, for example.

Strings can be indexed with both positive and negative indices. Positive indices work like you would expect, starting at 0 and ending at 1 minus the length of the string. Negative indexes start at -1 and work their way from the back of the strings.

You can also get a range of characters from a string using the syntax `[begin:end]` (begin is included and end is excluded).

```python
test = "hey there you!"
print(test[0]) # Will print 'h'
print(test[1]) # Will print 'e'
print(test[-1]) # Will print '!'
print(test[-2]) # Will print 'u'

print(test[0:3]) # Will print 'hey'
print(test[:3]) # Will print 'hey' since an empty begin defaults to 0

print(test[:-1]) # Will print 'hey there you'
print(test[1:]) # Will print 'ey there you!' since empty end defaults to the end
```

**NOTE:** The same syntax can be used for elements in a list

The file `strings.py` has a list of strings that you will need to print out space separated. The **expected output** is:

> This list is now all together

Note that there is **NO** trailing space in the output.

**Summary:**

1. Open the `strings.py` file
2. Use a `for` loop to join all of the strings, separated by a space.
3. Print the new string such that the output matches the above (no trailing space in output)
4. Now concatenating a list of strings seems like something that people would want to do often. So, as you may have been suspecting after the previous exercise, there is an in-built function to do this for you. Add the following line to the bottom of your `strings.py` file

    ```python
    print(' '.join(strings))
    ```

# Submission

Commit your changes then merge your `python_exercises` branch into `master`. Checkout `master` and push your changes.

Check that your GitLab repo contains all your work then submit your lab by running:

```
$ 1531 submit lab01
```

This command will submit the contents of the `master` branch on your GitLab repo. It must be run on a CSE computer (either remotely via vlab or ssh, or on a physical lab computer), but it can be run from any directory as it does not depend on any local files. If you're working on a computer other than a CSE computer it is **NOT** necessary to copy files to you CSE account.

As part the the submission, some tests are run on your work. If you fail the tests, you may want to go back and check you followed the steps correctly.

Once you have submitted, a record of it is created on GitLab. In your repo, if you click on **Tags**

![GitLab tags](https://www.cse.unsw.edu.au/~cs1531/19T3/labs/gitlab_tags.jpeg)

you will see a `submission` tag

![GitLab tags](https://www.cse.unsw.edu.au/~cs1531/19T3/labs/gitlab_submission_tag.jpeg)

clicking on that will show a log for your submission.

![Submission log](https://www.cse.unsw.edu.au/~cs1531/19T3/labs/gitlab_submission_log.jpeg)

For this and future labs, you **MUST** submit by the deadline in order to get marks.

# Prologue

If you finished the lab task early, well done! Talk to some of the other people in your lab. Maybe help them out if they need it. Also, think about who you'd like in your group for the project. Groups will be formed in week 2!

# Lab 02

## Due: Week 2, Sunday, 5:00 pm

## Value: 2 marks

## Aim

* Practice programming in python
* Practise using pytest
* Gain experience writing user stories
* Learn how to accept a merge request

## Setup

An individual repository for this lab has been created for you here (replace z5555555 with your own zID):

https://gitlab.cse.unsw.edu.au/z5555555/19T3-cs1531-lab02

## Preamble

You may find the following information useful for this lab:

* You can use the command `py.test-3` to run pytest. It will automatically find your tests and run them.
* Dictionaries can be indexed with `[` and `]`. For example, `a['b']`.
* Dictionaries have a `get()` method you may find useful. The documentation for it is [here](https://docs.python.org/3/library/stdtypes.html#dict.get).

## Python Exercises

### Exercise 1

Open `list_exercises.py` and implement the function stubs using only one line of python.

Some basic tests have been added in `test_list_exercises.py`. Run these tests with pytest to ensure they pass.

Now, add more to each test to make the test suite more exhaustive. Try to add at least two more assert statements for each test.

### Exercise 2

Open `reverse.py` and complete the function `reverse_words()` according to its documentation.

After completing this, write at least 5 tests using pytest, and include them in the same file.

Be prepared to demonstrate to your tutor how to run your tests.

### Exercise 3

Open `password.py` and implement the function `check_password()` according to its documentation.

After completing this, write at least 5 tests using pytest, and include them in the same file.

### Exercise 4 (Bonus)

Open `count.py` and read the documentation for stub function `count_char()`. To better understand what the function needs to do, write further tests in `test_count.py`. Each test should be its own function.

Once you're satisfied you have a good set of tests, implement the `count_char()` function.

Run your tests to ensure they pass.

## Requirements and user stories

Complete this question in your **project groups**.

Your friend Janette has shown you an app they think is really wonderful, and has asked you (a Macquarie University student), to produce a copy of this app: https://crossangles.app/

Before you can begin, it's important you follow standard software engineering principles - in particular - forming requirements for what you want to build.

Your task: Write out all necessary user stories to describe the requirements of building a clone of crossangles. If you need clarification on anything, ask your tutor.

Write your user stories in a text file called `stories.txt`. Make sure this file is commited to git!

## Project preparation

This section deliberately isn't complete. You will have to merge the merge request created at Week 1 Sunday 10pm to see the full instructions. This is practice in receiving project specification and lab updates from the course staff.

## Submission

Make sure that all your work has been pushed to GitLab then submit it with:

```bash
$ 1531 submit lab02
```

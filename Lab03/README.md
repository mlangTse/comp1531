# Lab 03

## Due: Week **4**, Sunday, 5:00 pm

**NOTE: You have two weeks to do this lab**

## Value: 2 marks

## Aim

* Further practice programming in python
* Further practise using pytest
* Working with objects in python

## Setup

An individual repository for this lab has been created for you here (replace z5555555 with your own zID):

https://gitlab.cse.unsw.edu.au/z5555555/19T3-cs1531-lab03

## Python Exercises

## Exercise 1

Open `president.py` and write some python code to make the following changes to the dictionary:
 * Remove "Hayden" from the list of "staff" in the `president` structure (we don't like him)
 * Sort the list of "staff" in the president structure in alphabetical order
 * Add a new key to the president structure called "marks", which itself consists of a dictionary that contains a key => value mapping of 'term' => mark. E.G. { "19T1" : 78 }. Add the following marks:
   * 19T1: 77
   * 19T2: 88
   * 19T3: 99

Note: You are not allowed to edit the structure directly. You must write your code between the two comments specified in `president.py`

## Exercise 2

Open `marks.py`. Currently, the program outputs the average homework, quiz, and test marks across all of the students as 0. Modify the main component of the code (underneath line 22) to accurately computer the averages from the dictionary at the top of the file. The averages are for the average of homework, quizzes, and tests, across ALL students.

### Exercise 3

Open `prefix.py` and complete the function `prefix_search()` according to its documentation.

Some tests have been added in `prefix_test.py`. Ensure your solution passes those tests then write some of your own such that you have complete test coverage.

## Exercise 4

In the lecture you were introduced to the `date` class and objects constructed from it. Python also comes with classes for `time`, a time independent of a particular day, and `datetime`, a combination of a date and a time.

Open `timetable.py` and complete the function `timetable()` according to its documentation.

Write some tests in a new file you create called `timetable_test.py`.

## Exercise 5

In `house.py` complete the definition of the `House` class such that:

* It has an attribute for its owner, address, last-sold-for price, number of bedrooms and a boolean flag indicating whether it is for sale.
* When first constructed, it is not for sale and its last-sold-for price is `None`.
* It contains an `advertise()` method that puts the house up for sale.
* It contains a `sell(...)` method that, if the house is for sale, transfers ownership of the house, updates the last-sold-for price and removes it from sale. If this method is called when the house is no longer for sale, an exception is raised

The file contains an example of how the class might be used and how the methods should work.

## Submission

Make sure that all your work has been pushed to GitLab then submit it with:

```bash
$ 1531 submit lab03
```

# Lab 09

## Due: Week **11**, Monday, 8:00 pm

## Value: 2 marks

## Aim

* Revise python programming skills
* Revise automated testing for the exam
* Gain experience writing property-based tests
* Writing non-trivial generators

## Setup

An individual repository for this lab has been created for you here (replace z5555555 with your own zID):

https://gitlab.cse.unsw.edu.au/z5555555/19T3-cs1531-lab09

## Hints

Some useful things to know:

* In python, `list(...)` takes any iterator and makes a list of all elements it "contains".
* The `integers()` strategy provided by the hypothesis library supports setting minimum and maximum values for the integers it generates with the `min_value` and `max_value` keyword arguments. Similarly, the `text()` strategy has the keyword arguments `max_size` and `min_size` that control the length of strings it will produce. You may need these to ensure your tests complete in a reasonable amount of time.
* Marks are not awarded for efficiency.

## Structure

This lab will be entirely automarked. In addition to covering week 8 material, it also gives you an opportunity to practise answering automarked questions for the exam.

It is divided into 2 parts:

* **Part A** - Tests are given for these questions. If you can pass the given tests, you should receive the marks. No further testing is required. When marking, additional tests may be used, but only to ensure you're not trying to cheat the tests by hardcoding test data in your solution.
* **Part B** - Some tests may given for these questions, but you will also need to write your own tests. **Ensure all your tests can be run in under 1 minute**. Marking will be based both on the correctness of your solution and the effectiveness of your tests. The latter will be measured by code coverage as well as running them against other, possibly incorrect, solutions. Your tests should fail for incorrect solutions and pass for correct ones. **Write your tests only in the included test file. Do not create additional files.**

## Part A

1. In `bad_interview.py`, complete the definition of the generator according to its documentation. A test is in `bad_interview_test.py`
2. In `inverse.py`, complete the definition of the function according to its documentation. A property-based test is located in `inverse_test.py`.
3. In `divisors.py`, complete the definition of the generator according to its documentation. Tests are located in `divisors_test.py`.

## Part B

1. In `factors.py`, complete the definition of `factors()` according to its documentation. In `factors_test.py` write your own tests as property-based tests and/or conventional unit tests.
2. In `permutations.py`, complete the definition of the generator according to its documentation. In `permutations_test.py`, write your own tests as property-based tests and/or conventional unit tests. Your tests should pass for any valid implementation of `permutations()`, not just *your* implementation.
3. **Challenge bonus question (only attempt if you have completed all other questions)** In `balanced.py`, complete the definition of the generator according to its documentation. In `balanced_test.py`, write your own tests as property-based tests and/or conventional unit tests. Your tests should pass for any valid implementation of `balanced()`, not just *your* implementation.

## Submission

Make sure that all your work has been pushed to GitLab then submit it with:

```bash
$ 1531 submit lab09
```

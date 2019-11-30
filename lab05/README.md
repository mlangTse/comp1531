# Lab 05

## Due: Week **6**, Tuesday, 11:59 am

## Value: 2 marks

## Aim

* Further practice programming in python
* Further practise using pytest
* Working with objects in python

## Setup

An individual repository for this lab has been created for you here (replace z5555555 with your own zID):

https://gitlab.cse.unsw.edu.au/z5555555/19T3-cs1531-lab05

## Project Exercises

## Exercise 0

Submit a document team.md where you explain how you're breaking up work between you all for the coming section, and how your separate pieces of work intersect

## Python Exercises

## Exercise 1

This exercise should be be worked on individually. It may be in your exam, so practice it.

In `simple.py`, build a basic flask server to store a list of names using a global variable as a list. It should have routes:
 * POST /name/add
   * input { name: 'example' }
   * output { }
 * GET /names
   * input { }
   * output { names: [ 'example1', 'example2' ] }
 * DELETE /name/remove
   * input { name: 'example' }
   * output { }

For example, if the following was done:
 * POST request made to /names/add with data { name: 'Asus' }
 * POST request made to /names/add with data { name: 'Acer' }
 * POST request made to /names/add with data { name: 'Dell' }
 * GET request made to /names would return { names: [ 'Asus', 'Acer', 'Dell' ]}
 * DELETE request made to /names/remove with data { name: 'Dell' }
 * GET request made to /names would return { names: [ 'Asus', 'Acer' ]}

## Exercise 2

This exercise should be be worked on individually. It may be in your exam, so practice it.

Build a flask server in `auth.py` that will:
 * Allow for the creation of a user based on a password, and when they register, they give a secret that they want to retrieve later
 * Allow for the user to authenticate themselves again with their password, which they are given a token to allow them to be authorised for future requests
 * Allow for the collection of their secret given their token

Here are some endpoints to help you out:
 * POST /user/create
   * input { password: 'example', secret: 'mySecret' }
   * output { token: 'example12345abcd' }
 * PUT /user/connect
   * input { password: 'example' }
   * output { token: 'example12345abcd' }
 * GET /user/secret
   * input { token: 'example12345abcd' }
   * output { secret: 'mySecret' }

You aren't required to use JWTs as tokens. You can just use a raw string if you want for this exercise. However, since you have to understand JWT tokens for project, we encourage you to try them out.

## Exercise 3

This exercise should be be worked on individually. It may be in your exam, so practice it.

Observe the following jwt

*eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1X2lkIjoiMTIzNDUifQ.lBTAPFU1xxDAi2Vrusfo67ypBai0vBr6O7KOt6CJf1s*

What data is stored in this JWT? Write it down inside `jwt.md`

This payload was originally encoded with a secret of "comp1531". Is the JWT above appropriately signed with this secret, or has it been tampered? Justify your answer in `jwt.md`

## Exercise 4

You may work on this question in groups.

Write a class in `tictac.py` to represent a game of tic-tac-toe. It should store the state of the board, and have methods for:

* Placing noughts (`O`) and crosses (`X`) into the squares (two separate methods)
* Getting the value (`X`, `O` or `None`) of a particular square
* Determining whether there is a winner and who that winner is

Don't try to account for players taking turns (e.g. it should be possible to place a `X` then immediately place another `X` without having placed a `O` in between).

A suitable exception should be thrown if an attempt is made to fill a square that already contains a `O` or a `X`.

Write tests, using pytest, such that you achieve 100% code coverage with branch coverage checking.

## Exercise 5 (Bonus / Challenge)

You are not expected to complete this exercise.

Use [pycurl](http://pycurl.io/docs/latest/quickstart.html) to write python-based tests for Question 2 in a file `authtest.py`.

Note: pycurl **does not work** on UNSW CSE machines due to libraries required. However, you can easily play around with this on your own laptop using command line (or in the case of linux, using WSL). Remember this is not a required activity, so if you don't want to make the effort, don't stress, as you can still get full marks on the lab without this.

## Exercise 6 (Bonus / Challenge)

You are not expected to complete this exercise.

Setup a flask server `imgsneak.py` that serves a 1px x 1px transparent png at a path /email/img.png?code=ABCDEFG

Where ABCDEFG is a unique code that can be anything.

When this route is accessed (via GET method), the unique code ABCDEFG should be printed to terminal.

Demonstrate to your tutor how you can send yourself an email (via any email account on the CSE machine) with an image in the email and how when they open the email your running flask server prints out the code.

Note: (you'll have to send a raw email with the code:
```html
<img src="http://127.0.0.1/email/img.png?code=yourname" />
```

## Submission

Make sure that all your work has been pushed to GitLab then submit it with:

```bash
$ 1531 submit lab05
```

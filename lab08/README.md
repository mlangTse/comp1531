# Lab 08

## Due: Week **10**, Tuesday, 12:00 pm

## Value: 2 marks

## Aim

* Practice refactoring python code to adhere to stronger design
* Gain experience developing a domain model

## Setup

An individual repository for this lab has been created for you here (replace z5555555 with your own zID):

https://gitlab.cse.unsw.edu.au/z5555555/19T3-cs1531-lab08

## Exercise 1

Look at `encapsulate.py`. There are design imperfections with this code. relating to encapsulation (in terms of the class), and something to do with how age is calculated being rigid (in terms of it only works for 2019, and will break next year). Improve the design of this code, and add a short comment or two up the top explaining what you've done and why.

## Exercise 2

Look at `decorator.py`. When you run it like the following:

```bash
python3 decorator.py CrocodileLikesStrawberries
```

The token "CrocodileLikesStrawberries" allows you to interact with the functions.

This code is OK, but there is repetition with the checks for `auth_token`. We could pull this out into it's own function, but what is even better design is to use a decorator. Create an *authorise* decorator and use it with the refactored code given below.

```python
import sys

MESSAGE_LIST = []

@authorise
def get_messages():
    return MESSAGE_LIST

@authorise
def add_messages(msg):
    global MESSAGE_LIST
    MESSAGE_LIST.append(msg)

if __name__ == '__main__':
    auth_token = ""
    if len(sys.argv) == 2:
        auth_token = sys.argv[1]

    add_messages(auth_token, "Hello")
    add_messages(auth_token, "How")
    add_messages(auth_token, "Are")
    add_messages(auth_token, "You?")
    print(get_messages(auth_token))
```

## Exercise 3

The code `drykiss.py` is unnecessarily complicated, and there is a lot of repetition. Take some time to refactor this code focusing on DRY and KISS to create a beautiful and concise piece of well understood code.

Improve the design of this code, and add a short comment or two up the top explaining what you've done and why.

## Exercise 4

Consider this description of fruit wholesalers:
* Each order made to a wholesaler is for a type and quantity (in kilograms) of a particular fruit.
* Orders can only be fulfilled if there are sufficient quantities of fruit available.
* Pending orders are fulfilled after new fruit has been delivered.
* If there are multiple pending orders, the customer with the most previous orders has theirs fulfilled first.
* Fruit is priced at a fixed amount per kilogram.

By first performing noun/verb analysis, create a domain model in the form of a UML class diagram. Include this UML diagram as a pdf file in your repo.

Once you're satisfied with your model, implement it in python, accounting for all described behaviour.

## Submission

Make sure that all your work has been pushed to GitLab then submit it with:

```bash
$ 1531 submit lab08
```

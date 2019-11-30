# Lab 06

## Due: Week **8**, Tuesday, 12:00 pm

## Value: 2 marks

## Aim

* Further practice programming in python
* Further practise using pytest
* Working with objects in python

## Setup

An individual repository for this lab has been created for you here (replace z5555555 with your own zID):

https://gitlab.cse.unsw.edu.au/z5555555/19T3-cs1531-lab06

## Exercise 1

A pickled file with data in it is stored in `shapecolour.p`. Write a program `unpickle.py` that un-pickles this file, and analyses the data to print what the most common shape-colour pair is.

The output of `unpickle.py` should be (for example, if the most common dictionary pair is red circle):
```txt
Colour: red
Shape: circle
```
## Exercise 2

With the unpickled files from exercise 1, wrap the shape colour data in a bigger data structure:

```json
{
    "mostCommon" : {
        "colour" : "[most-common-colour]",
        "shape" : "[most-common-shape]"
    },
    "rawData" : [insert-raw-data-from-shapecolour.p]
}
```

Write a file `process.py` that creates this new data structure, then outputs it as JSON to a file `processed.json`

### Exercise 3

Convert the JSON file `data_1.json` to YAML in `data_1.yml`
Convert the YAML file `data_2.yml` to JSON in `data_2.json`

Of course, you can do this with [simple online tools](https://www.json2yaml.com/). However, we encourage you to try and do this manually because during the exam if we test you on these items you need to be prepared!

## Exercise 4

Work in your group to draw an accurate data model (as an ER diagram) that reflects how you've decided to store your data for iteration 2.

Save this as an PDF `er.pdf`.

## Submission

Make sure that all your work has been pushed to GitLab then submit it with:

```bash
$ 1531 submit lab06
```

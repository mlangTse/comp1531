president = {
    'name' : 'Ian Jacobs',
    'age' : 54,
    'staff' : [ 'Sally', 'Bob', 'Rob', 'Hayden' ]
}

if __name__ == "__main__":
## TODO: Write code below this line
    president['staff'].remove('Hayden')
    print(president)


## TODO: Write code above this line
    president['staff'].sort()
    print(president)

    president['mark'] = {"19T1": 77}
    president['mark']["19T2"] = 88
    president['mark']["19T3"] = 99
    print(president)
    
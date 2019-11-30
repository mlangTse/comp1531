'''
TODO Complete this file by following the instructions in the lab exercise.
'''

strings = ['This', 'list', 'is', 'now', 'all', 'together']
new = ""

for word in strings:
    new += word
    if word is not strings[-1]:
        new += " "

print(new)

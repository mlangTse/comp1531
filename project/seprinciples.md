**DRY (DON'T REPEAT YOURSELF)**

**Message\_function.py**

- Our team created a helper function called get\_new\_message\_id() and add\_message(). This avoids us repeating the code in the sendlater() and send() functions since we realised that for it was always necessary to get the message id to test for value and access errors, as well as adding it to the database if no errors were raised.
- [PLEASE CHECK] Almost all functions had the same access error of the user trying to perform an action inside a channel that they were not a member of, so we decided to create a helper function called "invalid\_channel\_error" that returns the same error message which was included in the functions.

**­Channel\_function.py**

- Even though we have our own data structure in the back end, we have to follow the structure of the data requests made by the front end. Thus, we created a handy helper function, user\_detail(), which takes in the details of a user and returns it as a dictionary object. This helper function significantly shortened our code and eliminated repetition as it was required in multiple functions inside channel\_function.py

[EXAMPLE]

For example, in invite(), we used user\_detail() to create a dictionary object based on the information of the invitee. Not only does it meet the data structure requirements of the front end, it also makes it very easy to append it to the members list of the channel they were invited to. Included is a snippet of our code for visual reference:

![](https://i.ibb.co/nDB4xPT/1.png)


**KISS (KEEP IT SIMPLE STUPID)**

**Auth\_function.py**

- In the past, we created a reset code with a custom formula based on the microsecond, minute, day, month, year and email of the user when they requested to change their password. We did this to ensure absolute certainty that the reset code generated will be unique across different users, as well as the same user who requests a password reset at different points in time. However, it was a relatively complex formula which was vulnerable to privacy issues (since their email was appended to the end of the reset code) and the entire formula of the code was visible. Learning from Hayden's example in his lecture, we simply created a one-line code to simplify the code generation which required us to import the 'random' module which helped to improve security too since people who have access to our source code won't know the algorithm under the hood.

[EXAMPLE]

Here is a screenshot of a 'before' and 'after' comparison of that section of code once we applied the KISS principle.

Before:

![](https://i.ibb.co/vVw92wr/2.png[/img])



After:

![](https://i.ibb.co/kXFNB7d/3.png[/img])


**ENCAPSULATION**

- we use token to hide user's id and eamil to prevent hacker get the private information. 

**TDT (TOP-DOWN-THINKING)**

- Top-down thinking proved to be very helpful when we were redesigning our back-end data structure. Originally, we considered having a separate data structure for 'user', 'message' and 'channel'. However, we considered what the purpose of the data structure was as well as how it will be implemented practically in our code across the different functions and quickly realised that it was much cleaner to have our data as a dictionary with 3 primary 'key:value' pairs
- From this, our team quickly realised that we need to be able to source the right information about a user and that using the archaic method of a for-loop to iterate through our data structure every time was just too slow and inefficient. Since the user\_id is in ascending order with a starting value of 0, we decided that we can use it as an array index which makes it a 1-step process to scan the right data from our 'database'
- We also applied top-down thinking when we approached the problem of having to rerun the flask server multiple times in order to run tests and debug. This helped us to realise that the main difficulty with rerunning a flask server is that we lose all our data which means we have to arduously process the registration of a user again before we can test certain functionalities that require the user to be inside the Slackr application. Hence, we created a file called UserData.p that stores the database of the server beyond the lifetime of it running, which means that we can conveniently call a single function to retrieve all our data every time to refresh the flask server.

****CONCLUSION****


- Fragility: if a deletion is applied,  there is high possibility that code won't break because the our code is separated in lots of little function, so the remove of one function will cause front end's not functioning but the code can still run.

- Immobility: the verification part of u\_id, token, email, channel\_id, message\_id can be repeatedly used in lots of function. Also the part of raising the corresponding error when it's necessary.

- Opacity: we added comment when we think the particular part of coding will confuse other people, plus we try our best to use clear variable name

- Needless complexity:  for function resetcode, we use year month day hour min second microsecond and email to generate the reset code which is complex and unnecessary, therefore, we use th4e random function in python to generate the resetcode.

- Needless repetition: we wrote a lot helper function in helper\_server.py to avoid needless repeating.

- Coupling: Interdependence between components: channel is built on the user part and message is built on the channel part, so it's not possible to totally separate the data of channel user and message.

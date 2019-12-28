TEAMWORK

 MEETINGS

As a team, we originally intended to have at least 2 physical meetings a week to discuss progress. However, due to conflicts in availability and other commitments, we quickly realized that 2 meetings a week were unlikely to be successful. We then decided to hold online voice calls with screen sharing to discuss the project,  which we held twice a week. We felt that consultations such at these helped make sure everyone was on the right track with what our goals were. We did not feel like more meetings would have been useful, as any problems that occurred could be asked in our team group chat.

To ensure meetings were successful, we made sure to prepare any questions for the team in advance before calling, so our time together would be more efficient. Again, the use of screen sharing helped made our meetings more efficient and effective as problems such as incorrect output could be displayed instantly.

During iteration 3, we found that less meetings we required as we had already nearly finished most tasks during iteration 2. However, we still called once a week during iteration 3 and twice a week in the last week it was due.

 PROBLEMS AND SOLUTIONS

Our team initially had miscommunications regarding our dictionary and data structures as we did not clarify it in our first meeting. This resulted in major issues in our first few functions that we had written individually. When this issue was realized, we quickly decided that we had to standardize our data structures. In our next online meeting, we drafted a data structure that we all had to follow and slowly added to it as we did more functions, so we had a standardized reference.

During the design of the token, we realized the token shouldn't be save in the data structure and for every user there need to be a unique and unchangable token, the solve for this problem. Thus, to generate the token, we encode the u\_id with secret "W17A-Credible-4" which is team name, because the u\_id is unique and changeable.

When we are doing designing the reset code, we need to make sure nobody using the same reset code at the same time, and user is able to get different reset code when he forgets the password, so we encode his email, year, data, time, hours, seconds, microseconds to generate a very long resetcode.

User

    'u\_id': integer,

    'email': string,

    'password': string,

    'first\_name': string,

    'last\_name': string,

    'handle': string,

    'image': string,

    'permission': integer,

    'user\_channel': [{'channel\_id': integer, 'name': string}],

    'reset\_code': string,

    'loggedIn': boolean,

Channel

    'channel': {'channel\_id': integer, 'name': string},

    'owners': [{'u\_id': integer, 'name\_first': string, 'name\_last': string}]

    'members': [{'u\_id': integer, 'name\_first': string, 'name\_last': string}],

    'is\_public': boolean,

    'standup' : boolean,

    'message\_buffer': []

Message

    'channel\_id': integer,

    'message\_id': integer,

    'u\_id': integer,

    'message': string,

    'time\_created': datetime,

    'reacts': [{'react\_id': integer, 'u\_id': integer, 'is\_this\_user\_reacted': boolean}],

    'is\_pinned': boolean,

Another possible problem that our team considered during iteration 3 was code confliction. As we had 4 members that needed to work on the project together, we needed a way to distribute sections in a way which we would not have conflictions. We ultimately decided each individual should work on the functions that they wrote tests for in iteration 1 as we would have a much stronger understanding of those functions. This resulted in some confusion however where some functions within the same group of functions (ie, auth, message etc) conflicted. We also later noticed that this did not turn out to be a major problem as we had already mostly finished the coding aspects of iteration 3 during iteration 2.


About Agile:


- Satisfy the Customer:

We make the front_end the highest priority


- Welcome Change:

Once somebody post their improvement about code, we will discuss and make the change ASAP


- Measure of Progress:

in the group chat we will keep updating each other's progress also discuss what's the next step.


- Reflect for Effectiveness:

We sometime will share some useful website or function of VS code wich can yield higher efficiency, such as a website which can convert word document into markdown file-----"https://word2md.com/"


- Organized team:

Everybody in the team has high EQ, and we understand when somebody's progression is slower due to his other two subject, we will always help each other out by communication.
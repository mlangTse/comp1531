**Main idea for validation and verification:**

**To make sure the function works fine,**

**We test them by pytest and sub app postman in the chrome, test functions by using the pytest. The reason why we test from both pytest and postman is sometime function pass the pytest but don't return the current data structure on the postman.**

**For pytest part, we basically check is the function returning the right value when the input value is valid and correct for all the condition we can think of, and if the function raises right type of error when the input is invalid(ValueEerror) or the user don't have right to have an operation(AccessError).**

**For the postman part, we check if a function returns correct structure of data, or to see if the change added to the data base when we change a function to make a change.**

**We also use pylint to see if the function we wrote has good style and structure.**

**To see if the right functions has been built, we will frequently refer to main-page's requirements, user stories, and the assumptions we made. After the implementation, we connect the channel part and user part to the front end to see all the function for user, auth and channel following user's request on the front end.**

**In the end we have all functions except user\_photo\_upload got 100% coverage for pytest.**

**Function:** auth\_login

**User stories:**

As a user, I want to login to the app, so that

- I can use the app
- I can control my account, and increase safety factor of my account

**User Acceptance Criteria:**

- If the text that is typed in the email box is not the correct format, an error message will pop-up to notify the user and provide an example
- In the case that the email and password are registered and correspond to the same account, the user will successfully login and be able to view the internal Slackr interface
- Upon successful login, a valid token will be returned for the user to remain authenticated
- If the email is not registered in the system, an error message will pop-up to notify the user that their email is not found
- If the password is incorrect, an error message will pop-up to notify the user to retry
- There will be a button on the top bar with a placeholder saying &quot;Log In&quot; which will prompt the user to provide login details
- When the user starts typing, the placeholder will disappear
- If login details are incorrect, the user will be prompted with an error message asking them to try again

**Strategy to Test Function:**

Main idea:

**       ** There is a boolean type variable called &quot;loggedIn&quot; to show the logging status of a user.

        Once somebody logged in, the loggedIn flag will be &quot;True&quot;.

Pytest:

- For normal functioning: check if a user login with correct and registered email and a registered password can login into the function.
- We try different kinds of invalid email to see will the function return a ValueError
- We try different kinds of invalid password to see will the function return a ValueError
- Check if the token returned when login same as the token returned when register

Postman:

- To see if the function returns a token and user id if we input a valid password and registered email, we already test if the token returned is correct by using pytest, so we didn't verify it on the postman

Frontpage:

- We connect to the front page to see if a registered user can login

 Hey Zach, I think you need to add something to the acceptance criteria. U don't need to add a new topic, we just fake some thing we think front page will have, like the&quot;The search field is placed on the top bar&quot; &quot;Search starts once the user clicks &quot;Search&quot; &quot;The placeholder disappears once the user starts typing&quot;

=================================================================================

**Function:** auth\_logout

**User stories:**

- As a user, I want to logout of the app, so that my secure information is preserved when I am no longer using the app

**User Acceptance Criteria:**

- When user with an active token clicks on the logout button, their token will be invalidated
- Upon successful logout, the user will no longer see the internal Slackr interface
- There will be a button on the top bar thats says &quot;Log out&quot;
- When the button is pressed, a message will be displayed that prompts the user that they are now logged out

**Strategy to Test Function:**

Main idea:

        There is a boolean type variable called &quot;loggedIn&quot; to show the logging status of a user.

        Once somebody logged out, the loggedIn flag will be &quot;False&quot;.

Pytest:

- After successfully logged the user in, to see if the function returns {&quot;is\_success&quot;: True} after we logged the user out
- Register the valid user, to see will the function return {&quot;is\_success&quot;: False}, if we logged the user out without logging in first

Postman:

- To see if the function returns correct data structure of data if we logged the user out, we already test if the token returned is correct by using pytest, so we didn't verify it on the postman

Frontpage:

- We logged in by using valid password and email, then logged out to see is there anything unreasonable happen.

=================================================================================

**Function:** auth\_register

**User stories:**

- As a user, I want to build up my own account with my email and password so that
- details of my chats, my channel, and my personal information can be stored in the my account
- nly I can access these information
- I can create my idenitity on the e-society based on the software.

**User Acceptance Criteria:**

- If the first or last name given by the user includes numbers or symbols, an error message will pop up to advise the user to only user roman alphabetical characters
- Password must be no longer than XX characters long
- Email address provided must be a registered email in the correct format
- Upon creation of a new account, a new token is returned to the user to authenticate their session
- Upon creation of a new account, a handle must be generated that concatenates the first and last name
- Handle must be no longer than 20 characters long
- A unique handle is generated
- There will be a button on the top bar with a placeholder saying &quot;Register&quot; which will prompt the user to provide details
- When the user starts typing, the placeholder will disappear
- If details are invalid, the user will be prompted with an error message asking them to try again

**Strategy to Test Function:**

Pytest:

- Use an invalid email or a password or shorter than 5 or first\_name longer than 50 characters or last\_name longer than 50 characters to see will the function gives a value error
- Logged the user in after register to see if the email and password remembered by the system
- Logged out the user after logged in to see is the initial information correct
- After successfully register a user, use the same information to registered again to see if a value error returned
- Check if the token returned when login same as the token returned when register

Postman:

- Check if the correct type of data is returned on the post man if we register successfully
- Check if we can use the data registered to logged in.

Frontpage:

- See if we can logged in after the registered on the front page

=================================================================================

**Function:** auth\_passwordreset\_request

**User stories:**

As a user, I want to be able to request a password reset using my email address so that

I can regain access to my account if I forget my password

I can change my password regularly as a standard personal professional security practice

I know I am the only person who can reset the password using the secret, specific code in my email inbox

As a user, I want to reset my password after a period of time, so that

my account will be in high security

**User Acceptance Criteria:**

- Only registered email in our database will be accepted for a password reset request
- A unique reset code is sent to the user's email
- New password entered follows the protocol for a valid password. If not, error message reminds them of the criteria for a valid password
- Upon successful submission of a valid new password, the user's password is updated immediately in the database
- There will be a button on the top bar when a user has logged in, with a placeholder saying &quot;Reset Password&quot; which will prompt the user to provide a new password
- When the user starts typing, the placeholder will disappear
- If the new password is not valid, the user will be prompted with an error message asking them to try again

**Strategy to Test Function:**

Main idea:

        In the data structure we created, there is a variable inside user to store the reset code.

        We use the u id ,registered first name and last name to create a unique handle string

Pytest:

- Use the function to generate the reset code then check the user detail ,and use the new password to log in to see if the system changed
- Use the invalid password with correct reset code to see if a value error raised
- Use the qualified password with incorrect reset code to see if a value error raised

Postman:

- Call the function then use the reset code set on email to change the password to see if it's successful

Frontpage:

**       ** Click on forget the password and to see if we can use the reset code sent to change password

=================================================================================

**Function:** channel\_invite

**User stories:**

As a user, I want to invite users to join a channel, so that

The users can view information shared in the channel

**User Acceptance Criteria:**

- User must be part of the channel in order to invite other users to join
- User is only able to invite other users that are not already a member of the channel
- When the user searches for a user that is not registered on Slackr, there will be no results that show
- Upon successful invitation, the user is immediately added to the channel as a member
- There will be a button with  a placeholder displaying the words &quot;Invite&quot; on the side bar, which when pressed, will allow users to invite other users to join the channel.
- When invited, a notification will be displayed for the invited user, asking them to join the new channel

**Strategy to Test Function:**

Pytest:

- Make a user who is not in the channel invite other people to this channel to see if access error raised
- Invite a invalid user to the channel to see if value error raised
- Invite a valid user who is already in the channel to see if access error raised
- Invite a user into the channel and let this user invite another use in the channel then check the database to see if the change added in the database

Postman:

- Invite a user into the channel and let this user invite another use in the channel then check the database to see if the change added in the database

Frontpage:

- See if it works right on the frontend

Invite user into channel

=================================================================================

**Function:** channel\_details

**User stories:**

As a user, I want to know the detail about channel, so that

I can know who are the owner of the channel\_addowner

I can know who are also in the channel

As a channel owner, I want to know the detail about channel, so that

I can know who's in my channel

I can see how many people are in my channel

**User Acceptance Criteria:**

- User must be part of the channel in order to request to view it's details
- User must request for a valid channel that exists on Slackr
- Pressing the channel details button will show the basic details of the channel including the channel name, as well as all members in the channel. Owners of the channel are also explicitly flagged.
- There will be a button on the side bar with the place holder &quot;Details&quot;
- When clicked, the details will be shown in a pop up box with another button in the top right corner with a placeholder &quot;x&quot; that will close the details when clicked.

**Strategy to Test Function:**

Pytest:

- If a user wants to know detail of a channel he doesn't belong to, check if an access error raised
- If the channel id doesn't refer to any existing channel, check if value error raised

Postman:

- Run function with valid input, to see if the correct return is shown on the postman

Frontpage:

- See if it works right on the frontend

=================================================================================

**Function:** channel\_messages

**User stories:**

As a user in a channel, I want to be able to view messages sent previously so that

I don't have to remember all the details of any information that was sent through

I can reference it if there ever happens to be any new disagreements that was discussed in the channel earlier

I catch up to speed with the team by reading the chat history while I was inactive / offline

**User Acceptance Criteria:**

- User requesting to view channel messages must be at least a member of the channel
- Returns a maximum of 50 messages for the user to view
- Function returns a new index &quot;end&quot; which is the value of &quot;start + 50&quot;, with the start index specified by the user
- If the most recent function is returned, then the &quot;end&quot; value is &quot;-1&quot;
- After 50 messages have been displayed, the user can view more messages by scrolling up, which will trigger 50 more messages to be loaded.

**Strategy to Test Function:**

Pytest:

- If the channel id doesn't refer to any existing channel, check if value error raised
- Send 50 messages to see if the output correct
- Send 51 messages to see if the output correct
- Send 50 messages to see if the output correct

Postman:

- Run function with valid input, to see if the correct return is shown on the postman

Frontpage:

- See if it works right on the frontend

=================================================================================

**Function:** channel\_leave

**User stories:**

As a user, I want to be able to leave the channel which I don't like it anymore, so that

I won't receive any messages from this channel anymore

**User Acceptance Criteria:**

- User can only request to leave a channel that they are originally a member of
- User can only leave a channel that exists on their Slackr app
- User will be removed from the channel immediately.
- User handle will be immediately unauthorised to perform basic functions that a member of a channel are usually able to
- There will be a button on the side bar with the placeholder &quot;Leave Channel&quot; if the user is currently in a channel. Clicking the button will result in a confirmation pop up box with buttons with placeholders displaying &quot;Yes&quot; and &quot;No&quot;. If &quot;Yes&quot; is clicked, the user will leave the channel.
- The button will then disappear.

**Strategy to Test Function:**

Pytest:

-check is the function returning the right value when the input value is valid and correct for all the condition we can think of

-if the function raises right type of error when the input is invalid(ValueEerror) or the user don't have right to have an operation(AccessError)

Postman:

- After the function run, go the database to see if the change added on the database

Frontpage:

- See if it works right on the frontend

=================================================================================

**Function:** channel\_join

**User stories:**

As a user, I want to be able to join a authorised channel, so that

I can receive information that is intended for me inside the channel

**User Acceptance Criteria:**

- User can only request to join a channel that is public
- User can only request to join a channel that they are not currently a member of
- User can only request to join a valid channel that exists on their Slackr app
- There will be a button on the channel side bar which will allow a user to submit a join request.

**Strategy to Test Function:**

Pytest:

-check is the function returning the right value when the input value is valid and correct for all the condition we can think of

-if the function raises right type of error when the input is invalid(ValueEerror) or the user don't have right to have an operation(AccessError)

Postman:

- After the function run, go the database to see if the change added on the database

Frontpage:

- See if it works right on the frontend

=================================================================================

**Function:** channel\_addowner

**User stories:**

As an channel owner, I want to add more owner into my channel so that

they can help me maintain the channel

I can build up relation with them

**User Acceptance Criteria:**

- Only an owner of the channel can add other owners
- User must be a member of the channel before they can be added as an owner
- You cannot attempt to perform this function on a user that is already the channel owner
- The channel that the user is attempting to remove owner from must be a valid channel that exists on their Slackr app
- The owner of a channel will have access to a settings page in which there will be a button with a tag that says &quot;Add Owner&quot;
- Clicking this button reveals a text input bar with a place holder that says &quot;Name&quot;. The owner can then search for a user to add as an owner.

**Strategy to Test Function:**

Pytest:

-check is the function returning the right value when the input value is valid and correct for all the condition we can think of

-if the function raises right type of error when the input is invalid(ValueEerror) or the user don't have right to have an operation(AccessError)

Postman:

- After the function run, go the database to see if the change added on the database

Frontpage:

- See if it works right on the frontend

=================================================================================

**Function:** channel\_removeowner

**User stories:**

As a channel owner, I want to be able to remove other owners in the channel so that

I can undo the mistake of changing the permission of a member to owner by accident

I have the authority to enforce responsible use of power by other owner(s) of the channel

**User Acceptance Criteria:**

- You can only perform this function on a user that is currently an owner of the channel
- User that is requesting to remove another owner must themselves be an owner of the channel
- The channel that the user is attempting to remove owner from must be a valid channel that exists on their Slackr app
- The owner will have access to a page that displays all the users of the channel. Each user will have a button next to their name in the form of a cross. If the button is clicked, the user will be asked to confirm removal. If confirmation is given, the  user is then removed from the channel

**Strategy to Test Function:**

Pytest:

-check is the function returning the right value when the input value is valid and correct for all the condition we can think of

-if the function raises right type of error when the input is invalid(ValueEerror) or the user don't have right to have an operation(AccessError)

Postman:

- After the function run, go the database to see if the change added on the database

Frontpage:

- See if it works right on the frontend

=================================================================================

**Function:** channel\_list

**User stories:**

As a user, I want to know what channel I had, and channel's information, so that

I can access to a channel immediately by channel's id

I can determine some action for the channel I was in, such as leave a channel, send a message, etc.

**User Acceptance Criteria:**

- Lists all the channels that the user is part of, including their associated details which include channel name and members of the channel with the channel owners explicitly flagged

**Strategy to Test Function:**

Pytest:

-check is the function returning the right value when the input value is valid and correct for all the condition we can think of

-if the function raises right type of error when the input is invalid(ValueEerror) or the user don't have right to have an operation(AccessError)

Postman:

- Run function with valid input, to see if the correct return is shown on the postman

Frontpage:

=================================================================================

**Function:** channel\_create

**User stories:**

As an user, I want to create channel so that

I can have control of this channel

I can develop a chat circumstance vased on my preference

**User Acceptance Criteria:**

- The name of the channel can include characters, numbers or symbols
- User cannot create a channel name that is more than 20 characters long
- The channel name will turn into lower case regardless of what the user types
- If the user creates a public channel, then the channel should be visible for all other valid Slackr users to join
- If the user creates a private channel, then the channel will not be visible to other Slackr users
- The user that created the channel will immediately be assigned as channel owner
- There will be a &quot;+&quot; button next to the channel list. If this button is pressed, a window will be revealed requesting for more information such as the name, etc. After the information has been validated, a new channel will be made that is listed on the side bar.

**Strategy to Test Function:**

Pytest:

-check is the function returning the right value when the input value is valid and correct for all the condition we can think of

-if the function raises right type of error when the input is invalid(ValueEerror) or the user don't have right to have an operation(AccessError)

Postman:

- Run function with valid input, to see if the correct return is shown on the postman

Frontpage:

- See if it works right on the frontend

=================================================================================

**Function:** message\_sendlater

**User stories:**

As a member inside a channel, I want to be able to schedule messages to send later so that

I can set reminders for the group, whether it be a deadline for work, meeting time etc. closer to the date

I can work at unconventional hours and schedule messages so that it sends when others are active / online

I won't have the mental burden of remembering everything I want to send to the group

**User Acceptance Criteria:**

- The time specified must be in the future relative to the moment they press the 'send later' button
- User must be an authorised user of the channel that they want to send the message to
- Message cannot be more than 1000 characters

**Strategy to Test Function:**

Pytest:

-check is the function returning the right value when the input value is valid and correct for all the condition we can think of

-if the function raises right type of error when the input is invalid(ValueEerror) or the user don't have right to have an operation(AccessError)

Postman:

- Run function with valid input, to see if the correct return is shown on the postman

Frontpage:

-not tested

=================================================================================

**Function:** message\_send

**User stories:**

As a user, I want to send a message to the channel, so that

I can communicate with other people in the channel

**User Acceptance Criteria:**

- User attempting to send the message must be an authorised user of the channel
- Message cannot be more than 1000 characters
- There will be a button with an arrow sign that when clicked, will send the message written in the textbox next to the button.

**Strategy to Test Function:**

Pytest:

-check is the function returning the right value when the input value is valid and correct for all the condition we can think of

-if the function raises right type of error when the input is invalid(ValueEerror) or the user don't have right to have an operation(AccessError)

Postman:

- Run function with valid input, to see if the correct return is shown on the postman

Frontpage:

-not tested

=================================================================================

**Function:** message\_remove

**User stories:**

As a user, I want to remove messages in a channel, so that

I can remove typos

I can remove messages that were not intended to be sent.

**User Acceptance Criteria:**

- User can only remove a message if they sent the message themselves, or they are an owner of the channel or admin of Slackr app
- User must still be an authorised user of the channel in which the message resides
- The message must not have been removed previously
- The message must be removed immediately and be no longer visible by other authorised users in the channel
- A message pops up that says &quot;Message is removed&quot; in the channel to notify other channel members
- There will be a more details tab next to each message sent. Users can click on this tab to reveal a button that says &quot;remove message&quot;. When this button is pressed, a confirmation pop up box will be revealed. If confirmation is received, the message is removed.

**Strategy to Test Function:**

=================================================================================

**Function:** message\_edit

**User stories:**

As an poster of message, I want to edit the message so that

I can correct it when it's wrong

**User Acceptance Criteria:**

- User must be either the original user who sent the message, or is an admin or owner of this channel or the Slackr
- User must still be in the channel in which the message resides
- The message will immediately update with the new text
- A short caption underneath the edited message will appear: &quot;Edited message&quot;
- New message must be no more than 1000 characters
- There will be a more details tab next to each message sent. Users can click on this tab to reveal a button that says &quot;edit message&quot;. When this button is pressed, a new text box will be revealed with place holder &quot;edit&quot;. The user can then send this new message which will edit the original message sent.

**Strategy to Test Function:**

Pytest:

-check is the function returning the right value when the input value is valid and correct for all the condition we can think of

-if the function raises right type of error when the input is invalid(ValueEerror) or the user don't have right to have an operation(AccessError)

Postman:

- After the function run, go the database to see if the change added on the database

Frontpage:

- **Not tested**

=================================================================================

**Function:** message\_react

**User stories:**

As a user, I want to use button to decorate the message with certain emotion so that I can show what I feel about a single message without saying it in words,

**User Acceptance Criteria:**

- User must be an authorised user of the channel in which the message resides
- The user cannot react with the same reaction on the same message more than once
- User can only react with a valid reaction specified on the Slackr app
- Hovering the mouse over a message will reveal a option to react to a message. If the button is clicked, the user will react to the message and a thumbs up button will be displayed next to the message.

**Strategy to Test Function:**

=================================================================================

**Function:** message\_unreact

**User stories:**

As a user, I want to be able to unreact messages so that

I can undo the mistake of accidentally reacting to a message to avoid miscommunication

I can undo the mistake of accidentally using the wrong react emoticon

**User Acceptance Criteria:**

- User must be an authorised user of the channel in which the message resides
- The user can only unreact to a message that they previously reacted to
- Hovering the mouse over a message will reveal a option to unreact to a message if it has already been reacted to. If the button is clicked, the user will unreact to the message and the thumbs up button will be removed from next to the message.

**Strategy to Test Function:**

Pytest:

-check is the function returning the right value when the input value is valid and correct for all the condition we can think of

-if the function raises right type of error when the input is invalid(ValueEerror) or the user don't have right to have an operation(AccessError)

Postman:

- After the function run, go the database to see if the change added on the database

Frontpage:

- See if it works right on the frontend

=================================================================================

**Function:** message\_pin

**User stories:**

As a user, I want to pin important messages, so that

I can highlight the importance of this message

Others are more likely to see this message

**User Acceptance Criteria:**

- User cannot pin a message that is removed
- User must be an admin and be part of the channel that the message resides in order to pin it
- User cannot pin a message that is already pinned
- Hovering over a message will reveal a button to pin the message. If the button is clicked, a confirmation message box will appear. If confirmation is received, the message will be fixed on the top bar and will stay there until taken down.

**Strategy to Test Function:**

=================================================================================

**Function:** message\_unpin

**User stories:**

As the user who pin the message, I want to unpin the message so that

I can cancel the special display treatment when I think the mesage is not important anymore.

**User Acceptance Criteria:**

- User cannot unpin a message that is not currently pinned
- User must be an admin and be part of the channel that the message resides in order to unpin it
- Hovering over a message will reveal a button to unpin a message. If the button is clicked, the message that was displayed on the top bar will be removed.

**Strategy to Test Function:**

Pytest:

-check is the function returning the right value when the input value is valid and correct for all the condition we can think of

-if the function raises right type of error when the input is invalid(ValueEerror) or the user don't have right to have an operation(AccessError)

Postman:

- After the function run, go the database to see if the change added on the database

Frontpage:

- See if it works right on the frontend

=================================================================================

**Function:** user\_profile

**User stories:**

As a user, I want to be able to check the details of my user profile anytime so that:

I can confirm that the personal details I set for my user profile during registration is correct and accurate

I can check if my details updated whenever I reset it (e.g. email, handle)

I don't have to remember my details

**User Acceptance Criteria:**

- User can only view the profile of other registered users on the Slackr app
- Returns information about the user requested, including their email, first name, list name, and handle
- Clicking on a user will reveal their user profile.

**Strategy to Test Function:**

pytest:

- Use the handle which has length smaller than 3 to see if a value error raised
- Use the handle which has length longer than 20 to see if a value error raised
- Register two user who shares the same first name and same last name to see if there handle str are different

Postman:

- We wee if a user's profile build up after register
- Change the name, email or handlestr to see if the user profile changed

Frontpage:

Register a user then open his profile to see if the information correct.

=================================================================================

**Function:** user\_profile\_setname

**User stories:**

As a user, I want to have the ability to change my name, which I don't like anymore, so that

I can change it to something that I want in that period of time

**User Acceptance Criteria:**

- User can only update their own name
- The first name and last name can only be in between 1 to 50 characters long
- The first name and last name cannot contain numbers or characters
- The first name and last name entered must be different to the current name registered with their profile
- Handle is immediately updated to reflect the new first and last name
- First name and last name is immediately updated when the user themselves, or others, view their profile
- The user can click on their profile in the top left hand corner. This will open a new page on which there will be a button that says &quot;New Name&quot; with the current name in a textbox next to the button.
- This textbox can be edited with the new name, and after confirmation, the name will be changed.

**Strategy to Test Function:**

Pytest:

- Use the first name and last name which has length longer than 20 to see if a value error raised
- Change the first name or the last name to see if the change added on the database

Postman:

- Change the first name or the last name to see if the change added on the database

Frontpage:

- See if it works right on the frontend

=================================================================================

**Function:** user\_profile\_setemail

**User stories:**

As a user, I want to have the ability to change my email, which I don't like anymore, so that

I can change it to one which I use more regularly.

**User Acceptance Criteria:**

- User can only update their own email
- Email must be valid as per the method described in the project specifications
- Email must be different to the current email registered with their profile
- Email is immediately updated on their user\_profile and will be the main email user for other account activities such as password reset
- The user can click on their profile in the top left hand corner. This will open a new page on which there will be a button that says &quot;Set Email&quot; with the current name in a textbox next to the button.
- This textbox can be edited with the new email address, and after confirmation, the email will be updated.

**Strategy to Test Function:**

Pytest:

- Use the invalid email to see if value error raised
- Change the user's email to see if the change added on the profile

Postman:

- Change the user's first name and second name to see if the change added on the profile

Frontpage:

- Change the first name or last name after registered to see if it's successful

=================================================================================

**Function:** user\_profile\_sethandle

**User stories:**

As a user, I want to set my handle so that

I can change it when I have a better handle

**User Acceptance Criteria:**

- User can only update their own handle
- The text for the new handle must be between 3 and 20 characters
- Handle must be unique and not currently used by other members
- Handle is immediately updated and displayed on the Slackr app to be seen by other authorised users
- The user can click on their profile in the top left hand corner. This will open a new page on which there will be a button that says &quot;New Handle&quot; with the current name in a place holder textbox next to the button.
- This textbox can be edited with the new handle, and after confirmation, the handlewill be changed.

**Strategy to Test Function:**

Pytest:

- Change the user's handle to see if the change added on the profile
- Change the handle to same handle which other people already using to see if the value error  raised
- Change the handle to some string which has wrong length to see if the value error raised

Postman:

- Run the function then access to user's detail to see if the change added successfully

Frontpage:

- Change the user handle to see if the change can be made successfully if the handle is not used by other people
- To see if is not available to change the handle if the handle is already used by other people

=================================================================================

**Function:** user\_profiles\_uploadphoto

**User stories:**

As a user I want to be able to upload a correctly cropped photo so that

It makes it easier to visually identify who I am in the channel, especially if there are a lot of users

The image uploaded is in the right dimensions to keep the app interface consistent and professional

**User Acceptance Criteria:**

- URL provided by the user must be of an image
- URL must be valid and return an HTTP status of 200
- All of x\_start, y\_start, x\_end, y\_end must be within the dimensions of the image at the URL

**Strategy to Test Function:**

We didn't test this function because lecture told us not.

=================================================================================

**Function:** standup\_start

**User stories:**

As a user, I want to start a standup, so that

I can sent a collection of message, which sent by other user who is using standup\_sent

**User Acceptance Criteria:**

- User must be an authorised user of the channel in which they request a standup
- There must be no other active standups currently being hosted in the channel
- The standup period will last for exactly 15 minutes from the moment the stand\_up start button is pressed

**Strategy to Test Function:**

Pytest:

-

Postman:

-

Frontpage:

- **Not tested**

=================================================================================

**Function:** standup\_send


**User Acceptance Criteria:**

- An active standup must be running in the channel that the user is a part of
- The message cannot be more than 1000 characters in length
- The message will immediately be buffered in the standup queue during the 15-minute timeframe

**Strategy to Test Function:**

Pytest:

-Check if the function gives correvt type of error

Postman:

- Run the function then check if the message sent at eh correct time

Frontpage:

- **Not tested**

=================================================================================

**Function:** search

**User stories:**

As a user, I want to search messages I send before so that

I can find out the content and time of message I sent before in short time

I can get a list of message relevant to a certain topic.

**User Acceptance Criteria:**

- If the query string is not in the collection of messages in all of the channels that the user is joined, the function will still operate with no error message
- The user must be an authorised user that is a part of at least one or more channels on the Slackr app
- Only the collection of messages in the channels that the user has joined will be crawled through to match the query string
- The query string can not be longer than 1000 characters
- There will be a textbox in the top bar with the place holder &quot;Search&quot;. When the user clicks on the textbox, the place holder will disappear.
- The user can type in a string. After pressing the button next to the search bar, a list will be shown with all instances of that string displayed.

**Strategy to Test Function:**

Pytest:

- Check if the correct type of error returned
- Check if the function works well when the input is valid

Postman:

- Check if the function on postman return the right list of the message

Frontpage:

**         Not tested**

=================================================================================

**Function:** admin\_userpermission\_change

**User stories:**

As an admin, I want to be able to change the permission of other users so that

I can improve the priviledges of other members who I believe should be an owner / admin of a channel

I can restrict the priviledges of other members if they abuse the use of their power at the detriment of others

I have peace of mind knowing that the permission status of any user is not permanent

**User Acceptance Criteria:**

- The user requesting to change the permissions of other users must be an admin or owner of the channel
- The user having their permission changed must be a valid user in the Slackr app
- Only the 3 permissions are allowed (admin, owner, member)
- The permission change must be different to the current permission status of the user

**Strategy to Test Function:**

Pytest:

- Change the permission id to a number bigger than4 or smaller than 1 to see if the function raise value error
- Let a normal member to change other's permission id to check if an access error raised
- Make the owner of slacker to change a normal member's id form 1 to 2 then see if this new admin can change other's permission code
- Make owner change an admin into a normal member, and let this new member to change other person's permission id to see if a value error raised

Postman:

- Change the permission id  from a normal member by function than access to database to see if the permission id changed
- Make this new admin change other normal member's admin then check the database to see if the change added

Frontpage:

- Not tested

# Project Assumption
Every member in the group is writing assumption for their responsible function, while they are writing pytest.

## Auth
1. We have a database for all email and its matching password, user_info
2. User_info is the same as email address
3. The length of password is greater than 0
4. Password will change after calling the function "auth_passwordreset_reset", and the user will be able to login with new password
5. Reset_code is "RESET##"

## Channel
1. Channel_id always a positive number
2. Channel id is unique
3. A user can have 0 or more channels
4. The user need to login first to access channel details
5. The user don't need to login to be invited into a channel
6. The email in the channel_detail must be the valid
7. The creater need to login to create channel
8. The user need to login to add another owner
9. The owner of channel don't need to be logged on to be set as onwer by other
10. If you create the channel, you are automatically an owner
11. You have to be added into the channel before you can become an owner
12. If you are removed as owner, you still exist in the channel

## Message
1. This is not testable for success since we have not function to get a "react" list
2. React_id is between 1 - 10
3. Normal user in a channel only have 1-8 active reaction, and the owner of the channel have 1 - 10 active reaction
4. The user need to login, in order to sent message
5. Admin is the original owner of the channel 
6. The message_id sent is always from the request
7. Login before search the message
8. Can only search the message from any channel

## User
1. User need to login to change handle str
2. User need to login to change name
3. User need to login to change email
4. User need to login to check profile
5. User need to login to change photo

## Standup
1. "It is buffered" means the message is not sent until stand_up finish

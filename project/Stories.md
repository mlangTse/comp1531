<!--priority : low middle high-->
# Auth
## auth_login:
### stories:
As a user, I want to login to the app, so that
* I can use the app
* I can control my account, and increase safety factor of my account

priority: high

## auth_logout:
### stories:
As a user, I want to logout of the app, so that
* My secure information is preserved when I am no longer using the app

priority: high

## auth_register:
### stories:
As a user, I want to build up my own account with my email and password so that 
* details of my chats, my channel, and my personal information can be stored in the my account
* only I can access these information
* I can create my idenitity on the e-society based on the software.

priority: high

## auth_passwordreset_request:
### stories:  
As a user, I want to be able to request a password reset using my email address so that 
* I can regain access to my account if I forget my password
* I can change my password regularly as a standard personal professional security practice
* I know I am the only person who can reset the password using the secret, specific code in my email inbox 

priority: high

## auth_passwordreset_reset:
### stories:
As a user, I want to reset my password after a period of time, so that
* my account will be in high security

priority: high

# Channel
## channel_invite:
### stories:
As a user, I want to invite users to join a channel, so that
* The users can view information shared in the channel

priority: middle


## channel_details:
### stories: 
As a user, I want to know the detail about channel, so that
* I can know who are the owner of the channel_addowner
* I can know who are also in the channel

As a channel owner, I want to know the detail about channel, so that
* I can know who's in my channel
* I can see how many people are in my channel

priority: middle 
 
## channel_messages:
### stories:
As a user in a channel, I want to be able to view messages sent previously so that
* I don't have to remember all the details of any information that was sent through
* I can reference it if there ever happens to be any new disagreements that was discussed in the channel earlier
* I catch up to speed with the team by reading the chat history while I was inactive / offline

priority: high

## channel_leave:
### stories:
As a user, I want to be able to leave the channel which I don't like it anymore, so that 
* I won't receive any messages from this channel anymore

priority: low

## channel_join:
### stories:
As a user, I want to be able to join a authorised channel, so that
* I can receive information that is intended for me inside the channel

priority: middle

## channel_addowner:
### stories:
As an channel owner, I want to add more owner into my channel so that
* they can help me maintain the channel
* I can build up relation with them

priority: middle

## channel_removeowner:
### stories: high
As a channel owner, I want to be able to remove other owners in the channel so that
* I can undo the mistake of changing the permission of a member to owner by accident 
* I have the authority to enforce responsible use of power by other owner(s) of the channel

priority: high

## channels_list:
### stories:
As a user, I want to know what channel I had, and channel's information, so that
* I can access to a channel immediately by channel's id
* I can determine some action for the channel I was in, such as leave a channel, send a message, etc.

priority: low

## channels_listall:
### stories:
As a user, I want to see a list of all the channels with information, so that
* I can determine what channels exist
* I can view information regarding all channels easily

priority: low

## channel_create:
### stories:
As an user, I want to create channel so that
* I can have control of this channel
* I can develop a chat circumstance vased on my preference

priority: high
 
# Message
## message_sendlater:
### stories: medium
As a member inside a channel, I want to be able to schedule messages to send later so that
* I can set reminders for the group, whether it be a deadline for work, meeting time etc. closer to the date
* I can work at unconventional hours and schedule messages so that it sends when others are active / online 
* I won't have the mental burden of remembering everything I want to send to the group 

priority:
 
## message_send:
### stories:
As a user, I want to send a message to the channel, so that
* I can communicate with other people in the channel

priority: middle
  
## message_remove:
### stories:
As a user, I want to remove messages in a channel, so that
* I can remove typos
* I can remove messages that were not intended to be sent.

priority: low

## message_edit:
### stories:
As an poster of message, I want to edit the message so that 
* I can correct it when it's wrong

priority: middle
 
## message_react:
### stories:

priority:
 
## message_unreact:
### stories: high
As a user, I want to be able to unreact messages so that
* I can undo the mistake of accidentally reacting to a message to avoid miscommunication 
* I can undo the mistake of accidentally using the wrong react emoticon

priority: middle
  
## message_pin:
### stories:
As a user, I want to pin important messages, so that
* I can highlight the importance of this message
* Others are more likely to see this message

priority: middle


## message_unpin:
### stories:
As the user who pin the message, I want to unpin the message so that
* I can cancel the special display treatment when I think the mesage is not important anymore.

priority: middle

# Standup
## standup_start:
### stories:
As a user, I want to start a standup, so that
* I can sent a collection of message, which sent by other user who is using standup_sent

priority: low
 
## standup_send:
### stories:

priority: low
 
# User
## user_profile:
### stories: high
As a user, I want to be able to check the details of my user profile anytime so that:
* I can confirm that the personal details I set for my user profile during registration is correct and accurate 
* I can check if my details updated whenever I reset it (e.g. email, handle)
* I don't have to remember my details

priority: middle
 
## user_profile_setname:
### stories:
As a user, I want to have the ability to change my name, which I don't like anymore, so that
* I can change it to something that I want in that period of time

priority: low
 
## user_profile_setemail:
### stories:
As a user, I want to have the ability to change my email, which I don't like anymore, so that
* I can change it to one which I use more regularly.

priority: middle

 
## user_profile_sethandle:
### stories:
As a user, I want to set my handle so that 
* I can change it when I have a better handle

priority: middle
  
## user_profiles_uploadphoto:
### stories: low
As a user I want to be able to upload a correctly cropped photo so that
* It makes it easier to visually identify who I am in the channel, especially if there are a lot of users
* The image uploaded is in the right dimensions to keep the app interface consistent and professional 

priority:
 
# Other
## search:
### stories:
As a user, I want to search messages I send before so that
* I can find out the content and time of message I sent before in short time
* I can get a list of message relevant to a certain topic.

priority: low

## admin_userpermission_change:
### stories: high
As an admin, I want to be able to change the permission of other users so that
* I can improve the priviledges of other members who I believe should be an owner / admin of a channel
* I can restrict the priviledges of other members if they abuse the use of their power at the detriment of others
* I have peace of mind knowing that the permission status of any user is not permanent 

priority: high

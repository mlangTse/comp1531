''' message function '''
from datetime import datetime as dt, timedelta, timezone
from server.help_server import getData, getUserFromToken, save, find_channel, find_message, inChannel
from server.help_server import AccessError, Value_Error

def add_message(channel_id, message_id, u_id, message, time_sent):
    ''' add a new message to data '''
    data = getData()
    data['messages'].append({'channel_id': channel_id, 'message_id': message_id,
                             'u_id': u_id, 'message': message,
                             'time_created': time_sent, 'reacts': [{'react_id': 1, 'u_ids': [], 'is_this_user_reacted': None}], 'is_pinned': False})
    return data

def get_new_message_id():
    ''' return a new message id '''
    data = getData()
    if len(data['messages']) == 0:
        return 0
    return (int(data['messages'][len(data['messages']) - 1]['message_id']) + 1)

def sendlater(token, channel_id, message, time_sent):
    ''' Send a message from authorised_user to the channel specified
    by channel_id automatically at a specified time in the future '''
    data = getData()
    user_id = getUserFromToken(token)
    user = data['users'][user_id]
    right_channel_index = find_channel(channel_id)

    if type(time_sent) != dt:
        time_sent = dt.utcfromtimestamp(int(time_sent))

    if right_channel_index is None:
        raise Value_Error(f"Channel ID: {channel_id} is not a valid channel")

    message_id = get_new_message_id()

    if len(message) > 1000:
        raise Value_Error("Message is more than 1000 characters")

    if not inChannel(token, channel_id):
        raise AccessError("the authorised user has not joined the channel they are trying to post to")

    now = dt.utcnow()
    if now > time_sent:
        raise Value_Error("Time sent is a time in the past")

    data = add_message(channel_id, message_id, user['u_id'],  message, time_sent)

    save(data)
    return {'message_id': message_id}

def send(token, channel_id, message):
    ''' Send a message from authorised_user to the
    channel specified by channel_id '''
    data = getData()
    user_id = getUserFromToken(token)
    user = data['users'][user_id]
    message_id = get_new_message_id()
    if len(message) > 1000:
        raise Value_Error("Message is more than 1000 characters")

    if not inChannel(token, channel_id):
        raise AccessError("the authorised user has not joined the channel they are trying to post to")

    data = add_message(channel_id, message_id, user['u_id'], message, dt.utcnow())

    save(data)
    return {'message_id': message_id}

def remove(token, message_id):
    ''' Given a message_id for a message, this
    message is removed from the channel '''
    data = getData()
    user_id = getUserFromToken(token)
    user = data['users'][user_id]
    message_index = find_message(message_id)

    if message_index is None:
        raise Value_Error(f"Message (based on ID) no longer exists")
    message = data['messages'][message_index]

    if user['u_id'] != message['u_id'] and int(user['permission']) not in range(1, 3):
        raise Value_Error("Message with message_id was not sent by the authorised user making this request and The authorised user is not an admin or owner of this channel or the slackr")

    data['messages'].remove(message)
    save(data)
    return {}

def edit(token, message_id, message):
    ''' Given a message, update it's text with new text '''
    data = getData()
    user_dict = data['users'][getUserFromToken(token)]
    msg_dict = data['messages'][find_message(message_id)]

    if msg_dict['u_id'] != user_dict['u_id'] and user_dict['permission'] != 1 and user_dict['permission'] != 2:
        raise AccessError("Unauthorised user making edit request")

    msg_dict['message'] = message
    save(data)
    return {}

def react(token, message_id, react_id):
    ''' Given a message within a channel the authorised user is
    part of, add a "react" to that particular message '''
    data = getData()
    user_id = getUserFromToken(token)
    user_dict = data['users'][user_id]
    msg_dict = data['messages'][find_message(message_id)]
    channel_id = msg_dict['channel_id']

    '''Check if the user is in this particular channel_id of the message'''
    user_channel_list = user_dict['user_channel']
    error_flag = 1
    for i in user_channel_list:
        if i['channel_id'] == channel_id:
            error_flag = 0

    if error_flag == 1:
        raise Value_Error("Not a valid message within a channel that the authorised user has joined")

    if react_id != 1:
        raise Value_Error("Not a valid react_id")

    reacts_list = msg_dict['reacts']

    if user_id in reacts_list[int(react_id) - 1]['u_ids']:
        raise Value_Error("Message already contains active react with the same react_id")

    reacts_list[int(react_id) - 1]['u_ids'].append(user_id)

    save(data)
    return {}

def unreact(token, message_id, react_id):
    ''' Given a message within a channel the authorised user is
    part of, remove a "react" to that particular message '''
    data = getData()
    user_id = getUserFromToken(token)
    user_dict = data['users'][user_id]
    msg_dict = data['messages'][find_message(message_id)]
    reacts_list = msg_dict['reacts']
    channel_id = msg_dict['channel_id']

    '''Check if the user is in this particular channel_id of the message '''
    user_channel_list = user_dict['user_channel']
    error_flag = 1
    for i in user_channel_list:
        if i['channel_id'] == channel_id:
            error_flag = 0

    if error_flag == 1:
        raise Value_Error("Not a valid message within a channel that the authorised user has joined")

    if react_id != 1:
        raise Value_Error("Not a valid react_id")

    reacts_list = msg_dict['reacts']

    if user_id not in reacts_list[int(react_id) - 1]['u_ids']:
        raise Value_Error("Message with ID message_id does not contain an active React with ID react_id")

    reacts_list[int(react_id) - 1]['u_ids'].remove(user_id)
    save(data)
    return {}

def pin(token, message_id):
    ''' Given a message within a channel, mark it as "pinned" to
    be given special display treatment by the frontend '''
    data = getData()
    user_id = getUserFromToken(token)
    user_dict = data['users'][user_id]
    msg_id = find_message(message_id)

    if msg_id is None:
        raise Value_Error("Message_Id is not a valid message")

    msg_dict = data['messages'][msg_id]

    if user_dict['permission'] == 3:
        raise Value_Error("The authorised user is not an admin")

    if not inChannel(token, msg_dict['channel_id']):
        raise AccessError("The authorised user is not a member of the channel that the message is within")

    if msg_dict['is_pinned'] is True:
        raise Value_Error(f"Message with ID message_id: {message_id} already pinned")

    msg_dict['is_pinned'] = True
    save(data)
    return {}

def unpin(token, message_id):
    ''' Given a message within a channel, remove it's mark as unpinned '''
    data = getData()
    user_id = getUserFromToken(token)
    user_dict = data['users'][user_id]
    msg_id = find_message(message_id)

    if msg_id is None:
        raise Value_Error("Message_Id is not a valid message")

    msg_dict = data['messages'][msg_id]

    if user_dict['permission'] is 3:
        raise Value_Error("Message with message_id was not sent by the authorised user making this request and The authorised user is not an admin or owner of this channel or the slackr")

    if not inChannel(token, msg_dict['channel_id']):
        raise AccessError("you need to be in the channel to pin the message")

    if msg_dict['is_pinned'] is False:
        raise Value_Error(f"Message with ID message_id: {message_id} already unpinned")

    msg_dict['is_pinned'] = False
    save(data)
    return {}

def standup_start(token, channel_id, length):
    '''For a given channel, start the standup period whereby for the
    next 15 minutes if someone calls "standup_send" with a message,
    it is buffered during the 15 minute window then at the end of the
    15 minute window a message will be added to the message queue in
    the channel from the user who started the standup.'''
    data = getData()
    right_channel_index = find_channel(channel_id)
    now_time = dt.utcnow()

    if right_channel_index is None:
        raise Value_Error(f"Channel ID: {channel_id} is not a valid channel")

    right_channel = data['channels_list'][right_channel_index]

    if not inChannel(token, channel_id):
        raise AccessError('The authorised user is not a member of the channel that the message is within')

    if standup_active(token, channel_id)['is_active'] is False:
        time_finish = now_time + timedelta(seconds=int(length))
        message = sendlater(token, channel_id, '', time_finish)

        # update data
        data = getData()
        right_channel_index = find_channel(channel_id)
        right_channel = data['channels_list'][right_channel_index]
        right_channel['standup']['finish_time'] = time_finish
        right_channel['standup']['message_id'] = message['message_id']
    else:
        raise Value_Error('An active standup is currently running in this channel')

    save(data)
    return {'time_finish': time_finish.replace(tzinfo=timezone.utc).timestamp()}

def standup_active(token, channel_id):
    ''' For a given channel, return whether a standup is active in it,
    and what time the standup finishes. If no standup is active,
    then time_finish returns None '''
    data = getData()
    right_channel_index = find_channel(channel_id)

    if right_channel_index is None:
        raise Value_Error(f"Channel ID: {channel_id} is not a valid channel")

    right_channel = data['channels_list'][right_channel_index]
    finish_time = right_channel['standup']['finish_time']
    is_active = True
    if right_channel['standup']['finish_time'] < dt.utcnow():
        is_active = False

    return {'is_active': is_active, 'time_finish': finish_time.replace(tzinfo=timezone.utc).timestamp()}

def standup_send(token, channel_id, message):
    '''Sending a message to get buffered in the standup queue,
    assuming a standup is currently active'''
    data = getData()
    user_id = getUserFromToken(token)
    user = data['users'][user_id]
    right_channel_index = find_channel(channel_id)

    if right_channel_index is None:
        raise Value_Error(f"Channel ID: {channel_id} is not a valid channel")

    right_channel = data['channels_list'][right_channel_index]

    if len(message) > 1000:
        raise Value_Error("Message is more than 1000 characters")

    if right_channel['standup']['finish_time'] < dt.utcnow():
        raise Value_Error('An active standup is not currently running in this channel')

    if not inChannel(token, channel_id):
        raise AccessError('The authorised user is not a member of the channel that the message is within')

    message_id = right_channel['standup']['message_id']
    msg_id = find_message(message_id)
    old_message = data['messages'][msg_id]['message']
    old_message += str(user['handle']) + ': ' + message + ' '
    edit(token, message_id, old_message)

    # update data after edit
    data = getData()
    save(data)
    return {}

def search(token, query_str):
    '''Given a query string, return a collection of
    message_list that match the query'''
    if query_str == '':
        return {'messages': []}

    data = getData()
    user_id = getUserFromToken(token)
    user = data['users'][user_id]

    search_list = []
    for user_channel in user['user_channel']:
        for message_info in data['messages']:
            if int(message_info['channel_id']) == int(user_channel['channel_id']) and int(message_info['u_id']) == user_id:
                if str(query_str) in str(message_info['message']):
                    message_info['time_created'] = message_info['time_created'].replace(tzinfo=timezone.utc).timestamp()
                    for reaction in message_info['reacts']:
                        reaction['is_this_user_reacted'] = (user_id in reaction['u_ids'])
                    search_list.append(message_info)
    return {'messages': search_list}

''' channel function '''
import pytest
from datetime import datetime as dt, timezone
from server.auth_function import login, register
from server.help_server import getData, getUserFromToken, save, inChannel, find_channel
from server.help_server import AccessError, Value_Error, clear_data, generateToken

def user_detail(u_id, name_first, name_last, profile_img_url):
    ''' return user infomation '''
    return {'u_id': u_id, 'name_first': name_first,
            'name_last': name_last, 'profile_img_url': profile_img_url}

def invite(token, channel_id, u_id):
    '''
    Invites a user (with user id u_id) to join a channel with
    ID channel_id. Once invited the user is added to
    the channel immediately
    '''
    data = getData()
    right_channel_index = find_channel(channel_id)
    if right_channel_index is None:
        raise Value_Error(f"Channel ID: {channel_id} is not a valid channel")
    right_channel = data['channels_list'][right_channel_index]

    if int(u_id) >= len(data['users']):
        raise Value_Error(f"u_id: {u_id} does not refer to a valid user.")

    if not inChannel(token, channel_id):
        raise AccessError("the authorised user is not already a member of the channel.")

    invitee = data['users'][int(u_id)]
    invitee_info = user_detail(u_id, invitee['name_first'], invitee['name_last'], invitee['profile_img_url'])

    if invitee_info not in right_channel['members']:
        right_channel['members'].append(invitee_info)
        invitee['user_channel'].append(right_channel['channel'])
    save(data)
    return {}

def details(token, channel_id):
    '''
    Given a Channel with ID channel_id that the authorised
    user is part of, provide basic details about the channel
    '''
    data = getData()
    right_channel_index = find_channel(channel_id)
    if right_channel_index is None:
        raise Value_Error(f"Channel ID: {channel_id} is not a valid channel")
    right_channel = data['channels_list'][right_channel_index]

    if not inChannel(token, channel_id):
        raise AccessError("Authorised user is not a member of channel with channel_id.")

    return {
        'name': right_channel['channel']['name'],
        'owner_members': right_channel['owners'],
        'all_members': right_channel['members']
    }

def messages(token, channel_id, start):
    '''Given a Channel with ID channel_id that the authorised user is part of,
    return up to 50 messages between index "start" and "start + 50".
    Message with index 0 is the most recent message in the channel.
    This function returns a new index "end" which is the value of "start + 50",
    or, if this function has returned the least recent messages in the channel,
    returns -1 in "end" to indicate there are no more messages to load after this return.'''
    data = getData()
    u_id = getUserFromToken(token)
    right_channel_index = find_channel(channel_id)
    if right_channel_index is None:
        raise Value_Error(f"Channel ID: {channel_id} is not a valid channel")
    right_channel = data['channels_list'][right_channel_index]
    now = dt.utcnow()
    message_list = []
    total_message = 0
    for message in data['messages']:
        if int(message['channel_id']) == int(channel_id) and now >= message['time_created']:
            tmp = message
            tmp['time_created'] = message['time_created'].replace(tzinfo=timezone.utc).timestamp()
            for reaction in tmp['reacts']:
                reaction['is_this_user_reacted'] = (u_id in reaction['u_ids'])
            message_list.append(tmp)
            total_message += 1
        if message['message'] == '':
            data['messages'].remove(message)

    if int(start) != 0 and int(start) >= total_message:
        raise Value_Error("start is greater than or equal to the total number of messages in the channel")

    if not inChannel(token, channel_id):
        raise AccessError("Authorised user is not a member of channel with channel_id")

    end = int(start) + 50
    if end > total_message:
        end = -1
    return {'messages': message_list[int(start):int(start)+50], 'start': int(start), 'end': end}

def leave(token, channel_id):
    ''' Given a channel ID, the user removed as a member of this channel '''
    data = getData()
    user_id = getUserFromToken(token)
    right_channel_index = find_channel(channel_id)
    if right_channel_index is None:
        raise Value_Error(f"Channel ID: {channel_id} is not a valid channel")
    right_channel = data['channels_list'][right_channel_index]

    # remove channel from user's channel list
    if right_channel['channel'] in data['users'][user_id]['user_channel']:
        data['users'][user_id]['user_channel'].remove(right_channel['channel'])

    # remove user from channel's member list
    for member in right_channel['members']:
        if data['users'][user_id]['u_id'] == member['u_id'] and member in right_channel['members']:
            right_channel['members'].remove(member)
            break

    save(data)
    return {}

def join(token, channel_id):
    ''' Given a channel_id of a channel that the authorised
    user can join, adds them to that channel '''
    data = getData()
    joiner_id = getUserFromToken(token)
    joiner = data['users'][joiner_id]
    right_channel_index = find_channel(channel_id)
    if right_channel_index is None:
        raise Value_Error(f"Channel ID: {channel_id} is not a valid channel")
    right_channel = data['channels_list'][right_channel_index]

    if not right_channel['is_public']:
        raise AccessError("a private channel can only be joined by invitation")

    if right_channel['channel'] not in joiner['user_channel']:
        joiner['user_channel'].append(right_channel['channel'])

    joiner_info = user_detail(joiner['u_id'], joiner['name_first'], joiner['name_last'], joiner['profile_img_url'])

    if joiner_info not in right_channel['members']:
        right_channel['members'].append(joiner_info)

    save(data)
    return {}

def addowner(token, channel_id, u_id):
    ''' Make user with user id u_id an owner of this channel '''
    data = getData()
    maker_id = getUserFromToken(token)
    maker = data['users'][maker_id]
    joiner = data['users'][int(u_id)]
    right_channel_index = find_channel(channel_id)
    if right_channel_index is None:
        raise Value_Error(f"Channel ID: {channel_id} is not a valid channel")
    right_channel = data['channels_list'][right_channel_index]

    joiner_detail = user_detail(joiner['u_id'], joiner['name_first'], joiner['name_last'], joiner['profile_img_url'])
    maker_detail = user_detail(maker['u_id'], maker['name_first'], maker['name_last'], maker['profile_img_url'])

    if (maker_detail not in right_channel['owners']) and (maker['permission'] != 1):
        raise AccessError("you don't have the right to access")

    if joiner_detail in right_channel['owners']:
        raise Value_Error("the user id is already an owner")

    right_channel['owners'].append(joiner_detail)
    save(data)
    return {}

def removeowner(token, channel_id, u_id):
    ''' Remove user with user id u_id an owner of this channel '''
    data = getData()
    maker_id = getUserFromToken(token)
    maker = data['users'][maker_id]
    unlucky = data['users'][int(u_id)]
    right_channel_index = find_channel(channel_id)
    if right_channel_index is None:
        raise Value_Error(f"Channel ID: {channel_id} is not a valid channel")
    right_channel = data['channels_list'][right_channel_index]

    unlucky_detail = user_detail(unlucky['u_id'], unlucky['name_first'], unlucky['name_last'], unlucky['profile_img_url'])
    maker_detail = user_detail(maker['u_id'], maker['name_first'], maker['name_last'], maker['profile_img_url'])

    if (maker_detail not in right_channel['owners']) and (maker['permission'] != 1):
        raise AccessError("you don't have the right to access")

    if unlucky_detail in right_channel['owners']:
        if len(right_channel['owners']) > 1:
            right_channel['owners'].remove(unlucky_detail)

    save(data)
    return {}

def user_channel_list(token):
    ''' Provide a list of all channels (and their associated
    details) that the authorised user is part of '''
    data = getData()
    user_id = getUserFromToken(token)
    return {'channels': data['users'][user_id]['user_channel']}

def listall(token):
    ''' Provide a list of all channels (and their associated details) '''
    tmp = list()
    data = getData()
    for channel in data['channels_list']:
        tmp.append(channel['channel'])
    return {'channels': tmp}

def create(token, name, is_public):
    ''' Creates a new channel with that name that is either
    a public or private channel '''
    data = getData()
    user_id = getUserFromToken(token)

    if user_id not in range(len(data['users'])):
        raise Value_Error("the token doesn't exist")

    if len(name) > 20:
        raise Value_Error("the name is longer than 20 character")

    user = data['users'][user_id]
    user_info = user_detail(user_id, user['name_first'], user['name_last'], user['profile_img_url'])

    ch_id = len(data['channels_list'])
    data['channels_list'].append({'channel': {'channel_id': ch_id, 'name': name},
                                  'owners': [user_info],
                                  'members': [user_info],
                                  'is_public': is_public,
                                  'standup': {'finish_time': dt.utcnow(), 'message_id': None}})
    user['user_channel'].append({'channel_id': ch_id, 'name': name})

    save(data)
    return {'channel_id': ch_id}

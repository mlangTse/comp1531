import os
import pickle
from datetime import datetime as dt, timezone, timedelta
from json import dumps
from werkzeug.exceptions import HTTPException
import jwt

'''Users
    'u_id': integer,
    'email': string,
    'password': string,
    'name_first': string,
    'name_last': string,
    'handle': string,
    'profile_img_url': string,
    'permission': integer,
    'user_channel': [{'channel_id': integer, 'name': string}],
    'reset_code': string,
    'loggedIn': boolean,
'''
'''Channels_list
    'channel': {'channel_id': integer, 'name': string},
    'owners': [{'u_id': integer, 'name_first': string, 'name_last': string}]
    'members': [{'u_id': integer, 'name_first': string, 'name_last': string}],
    'is_public': boolean,
    'standup' : {'finish_time': datetime, 'u_id: integer},
'''
'''Messages
    'channel_id': integer,
    'message_id': integer,
    'u_id': integer,
    'message': string,
    'time_created': datetime,
    'reacts': [{'react_id': integer, 'u_id': integer, 'is_this_user_reacted': boolean}],
    'is_pinned': boolean,
'''

data = {
    'users': [],
    'channels_list': [],
    'messages': [],
}

SECRET = 'W17A-credible4'
timer = None

def defaultHandler(err):
    response = err.get_response()
    response.data = dumps({
        "code": err.code,
        "name": "System Error",
        "message": err.get_description(),
    })
    response.content_type = 'application/json'
    return response

class Value_Error(HTTPException):
    code = 400
    message = 'No message specified'

class AccessError(HTTPException):
    code = 400
    message = 'No message specified'

def getData():
    global data
    if os.path.exists('UserData.p'):
        data = pickle.load(open('UserData.p', 'rb'))
    return data

# please use this function to save data
def save(data):
    with open('UserData.p', 'wb') as FILE:
        pickle.dump(data, FILE)

def clear_data():
    global data
    data = {
        'users': [],
        'channels_list': [],
        'messages': [],
    }
    save(data)
    return data

def generateToken(u_id):
    global SECRET
    return jwt.encode({'uers_id': u_id}, SECRET, algorithm='HS256').decode('utf-8')

def getUserFromToken(token):
    global SECRET
    decoded_jwt = jwt.decode(token.encode(), SECRET, algorithms=['HS256'])
    u_id = int(decoded_jwt['uers_id'])
    return u_id

def inChannel(token, channel_id):
    data = getData()
    user_id = getUserFromToken(token)
    right_channel_index = find_channel(channel_id)
    right_channel = data['channels_list'][right_channel_index]
    if right_channel['channel'] in data['users'][user_id]['user_channel']:
        return True
    return False

def find_channel(channel_id):
    data = getData()
    i = 0
    for channel in data['channels_list']:
        if int(channel['channel']['channel_id']) == int(channel_id):
            return int(i)
        i += 1
    return None

def find_message(message_id):
    data = getData()
    i = 0
    for message in data['messages']:
        if int(message['message_id']) == int(message_id):
            return int(i)
        i += 1
    return None


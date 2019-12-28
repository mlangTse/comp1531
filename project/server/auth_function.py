""" Auth function """
import random
import string 
import os
import re
import urllib.request
from hashlib import sha256
from datetime import datetime as dt
from PIL import Image
from server.help_server import getData, getUserFromToken, save, generateToken, AccessError, Value_Error

CHECK_EMAIL = "^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"

def user_info(u_id, email, name_first, name_last, handle_str, profile_img_url):
    ''' return user infomation '''
    return {'u_id': u_id, 'email': email, 'name_first': name_first,
            'name_last': name_last, 'handle_str': handle_str, 'profile_img_url': profile_img_url}

def login(email, password):
    """ Given a registered users' email and password and generates
    a valid token for the user to remain authenticated """
    data = getData()
    len_user = len(data['users'])
    right_user = None
    if len_user > 0:
        len_user -= 1

    if re.search(CHECK_EMAIL, email):
        for user in data['users']:
            if user['email'] == email:
                right_user = user

        if right_user is None:
            raise Value_Error("Email entered does not belong to a user")

        if right_user['password'] != str(sha256(password.encode()).hexdigest()):
            raise Value_Error("Password is not correct")
    else:
        raise Value_Error("Email entered is not a valid email")

    right_user['loggedIn'] = True
    save(data)
    return {'u_id' : right_user['u_id'], 'token': generateToken(right_user['u_id'])}

def logout(token):
    ''' Given an active token, invalidates the taken to log the user out.
    If a valid token is given, and the user is successfully logged out,
    it returns true, otherwise false. '''
    data = getData()
    user_id = getUserFromToken(token)

    if user_id in range(len(data['users'])) and data['users'][user_id]['loggedIn'] == True:
        data['users'][user_id]['loggedIn'] = False
        save(data)
        return{
            'is_success': True
        }
    else:
        return {'is_success': False}

def register(email, password, name_first, name_last):            
    ''' Given a user's first and last name, email address, and password,
    create a new account for them and return a new token for authentication
    in their session. A handle is generated that is the concatentation of a
    lowercase-only first name and last name. If the handle is already taken,
    a number is added to the end of the handle to make it unique. '''
    data = getData()
    token = generateToken(len(data['users']))
    if not (re.search(CHECK_EMAIL, email)):
        raise Value_Error("the email is invalid")

    for user in data['users']:
        if user['email'] == email:
            raise Value_Error("Email address is already being used by another user")

    if len(password) in range(1, 6):
        raise Value_Error("password is below 6 characters characters in length")

    if len(name_first) not in range(1, 51):
        raise Value_Error("name_first is not between 1 and 50 characters in length")

    if len(name_last) not in range(1, 51):
        raise Value_Error("name_last is not between 1 and 50 characters in length")

    user_id = len(data['users'])

    permission_id = 3
    if user_id == 0:
        permission_id = 1

    handle = (name_first + name_last).lower()
    if len(handle) < 3:
        handle = str(user_id) + handle
        handle = handle[:(20 - len(str(user_id)))] + str(user_id)

    for user in data['users']:
        if user['handle'] == handle[:20]:
            handle = str(user_id) + handle
            handle = handle[:(20 - len(str(user_id)))] + str(user_id)
            break

    data['users'].append({
        'u_id': user_id,
        'email': email,
        'password': str(sha256(password.encode()).hexdigest()),
        'name_first': name_first,
        'name_last': name_last,
        'handle': str(handle[:20]),
        'profile_img_url': '/user_image?file=default.jpg',
        'permission': permission_id,
        'user_channel': [],
        'reset_code': None,
        'loggedIn': False
        })

    save(data)
    return {'u_id': user_id, 'token': token}

def passwordreset_request(email):
    ''' Given an email address, if the user is a registered user,
    send's them a an email containing a specific secret code,
    that when entered in auth_passwordreset_reset, shows that the
    user trying to reset the password is the one who got sent this email. '''
    data = getData()
    reset_code = None

    for user in data['users']:
        now_time = dt.now()
        N = 200
        reset_code = "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))
        user['reset_code'] = reset_code

    save(data)
    return {'reset_code': reset_code}

def passwordreset_reset(reset_code, new_password):
    ''' Given a reset code for a user, set that user's
    new password to the password provided '''
    data = getData()

    if len(new_password) in range(6):
        raise Value_Error("Password entered is not a valid password")

    valid_code = True
    for user in data['users']:
        if user['reset_code'] == reset_code:
            valid_code = False
            user['password'] = str(sha256(new_password.encode()).hexdigest())
            user['reset_code'] = None

    if valid_code:
        raise Value_Error("reset_code is not a valid reset code")
    save(data)
    return {}

def all_user(token):
    ''' return all user '''
    data = getData()
    user_id = getUserFromToken(token)

    if user_id not in range(len(data['users'])):
        return

    all_list = []
    for user in data['users']:
        user_detail = user_info(user['u_id'], user['email'], user['name_first'],
                                user['name_last'], user['handle'], user['profile_img_url'])
        all_list.append(user_detail)

    return {'users': all_list}

def profile(token, u_id):
    ''' For a valid user, returns information about their email,
    first name, last name, and handle '''
    data = getData()
    if int(u_id) not in range(len(data['users'])):
        raise Value_Error(f"u_id: {u_id} does not refer to a valid user.")

    user = data['users'][int(u_id)]
    return {
        'email': user['email'],
        'name_first': user['name_first'],
        'name_last': user['name_last'],
        'handle_str': user['handle'],
        'profile_img_url': user['profile_img_url']
    }

def setname(token, name_first, name_last):
    '''Update the authorised user's first and last name'''
    data = getData()
    user_id = getUserFromToken(token)

    if len(name_first) not in range(1, 51):
        raise Value_Error("name_first is not between 1 and 50 characters in length")
    if len(name_last) not in range(1, 51):
        raise Value_Error("name_last is not between 1 and 50 characters in length")

    data['users'][user_id]['name_first'] = name_first
    data['users'][user_id]['name_last'] = name_last

    save(data)
    return {}

def setemail(token, email):
    ''' Update the authorised user's email address '''
    data = getData()
    user_id = getUserFromToken(token)

    for user in data['users']:
        if user['email'] == email:
            raise Value_Error("Email address is already being used by another user")

    if (re.search(CHECK_EMAIL, email)):
        data['users'][user_id]['email'] = email
    else:
        raise Value_Error("Email entered is not a valid email")

    save(data)
    return {}

def sethandle(token, handle):
    ''' Update the authorised user's handle (i.e. display name) '''
    data = getData()
    user_id = getUserFromToken(token)

    for user in data['users']:
        if user['handle'] == handle:
            raise Value_Error("handle is already used by another user")

    if len(handle) < 3 or len(handle) > 20:
        raise Value_Error("handle_str must be between 3 and 20 characters")

    data['users'][user_id]['handle'] = handle

    save(data)
    return {}

def uploadphoto(token, img_url, x_start, y_start, x_end, y_end):
    ''' Given a URL of an image on the internet, crops the image within
    bounds (x_start, y_start) and (x_end, y_end). Position (0,0) is the top left. '''
    if urllib.request.urlopen(img_url).getcode() != 200:
        raise Value_Error("img_url is returns an HTTP status other than 200.")

    if not img_url.lower().endswith('.jpg'):
        raise Value_Error("img_url is returns an HTTP status other than 200.")

    img_addr = './server/user_image/' + str(token) + '.jpg'
    urllib.request.urlretrieve(img_url, img_addr)
    imageObject = Image.open(img_addr)
    width, height = imageObject.size

    if x_end not in range(width + 1) or y_end not in range(height + 1) or x_start not in range(x_end) or y_start not in range(y_end):
        os.remove(img_addr)
        raise Value_Error("any of x_start, y_start, x_end, y_end are not within the dimensions of the image at the URL.")

    cropped = imageObject.crop((x_start, y_start, x_end, y_end))
    cropped.save(img_addr)
    data = getData()
    user_id = getUserFromToken(token)
    data['users'][user_id]['profile_img_url'] = '/user_image?file=' + str(token) + '.jpg'
    save(data)
    return {}

def permission(token, u_id, permission_id):
    ''' Given a User by their user ID, set their permissions to
    new permissions described by permission_id '''
    data = getData()
    if permission_id not in range(0, 4):
        raise Value_Error("permission_id does not refer to a value permission")

    if u_id not in range(len(data['users'])):
        raise Value_Error(f"u_id: {u_id} does not refer to a valid user.")

    user_id = getUserFromToken(token)
    admin_or_owner = data['users'][user_id]
    if admin_or_owner['permission'] == 3:
        raise Value_Error("The authorised user is not an admin or owner")

    data['users'][int(u_id)]['permission'] = permission_id
    save(data)
    return {}

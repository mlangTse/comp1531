''' server pytest '''
import os
from time import sleep
from datetime import datetime as dt, timedelta, timezone
import pytest
from server.auth_function import login, logout, register, passwordreset_request, passwordreset_reset
from server.auth_function import profile, setname, setemail, sethandle, permission, uploadphoto, all_user
from server.channel_function import invite, details, messages, leave, join
from server.channel_function import addowner, removeowner, user_channel_list, listall, create
from server.message_function import sendlater, send, remove, edit, react, unreact, standup_active
from server.message_function import pin, unpin, standup_start, standup_active, standup_send, search
from server.help_server import AccessError, Value_Error, getData, save, clear_data, generateToken


""" BELOW TEST IS TESTING AUTH FUNCTION """
def test_login():
    #normal functioning
    user_info = register("minglang@gmail.com", "12345678", "minglang", "xie")
    assert login("minglang@gmail.com", "12345678") == user_info
    save(clear_data())

    # Email entered is not a valid email
    user_info = register("minglang@gmail.com", "12345678", "minglang", "xie")
    with pytest.raises(Value_Error):
        login("minglang_gmail.com", "12345678")
    save(clear_data())

    # Email entered is not a valid email
    user_info = register("minglang@gmail.com", "12345678", "minglang", "xie")
    with pytest.raises(Value_Error):
        login("minglang@gmailcom", "12345678")
    save(clear_data())

    # Password is not correct
    user_info = register("minglang@gmail.com", "12345678", "minglang", "xie")
    with pytest.raises(Value_Error):
        login("minglang@gmail.com", "87654321")
    save(clear_data())

    # Email entered does not belong to a user
    user_info = register("minglang@gmail.com", "12345678", "minglang", "xie")
    with pytest.raises(Value_Error):
        login("w17a.credible4@gmail.com", "12345678")
    save(clear_data())

    # we also need to see if user is able to log out after they log in, nad these case ius covered in the test_logout

def test_logout():
    # normal functioning
    user_info = register("minglang@gmail.com", "12345678", "minglang", "xie")
    login("minglang@gmail.com", "12345678")
    assert logout(user_info['token']) == {'is_success': True}
    save(clear_data())
        # logout without login
    user_info = register("minglang@gmail.com", "12345678", "minglang", "xie")
    assert logout(user_info['token']) == {'is_success': False}
    save(clear_data())
    # login, logout, then logout again
    user_info = register("minglang@gmail.com", "12345678", "minglang", "xie")
    login("minglang@gmail.com", "12345678")

    assert logout(user_info['token']) == {'is_success': True}
    assert logout(user_info['token']) == {'is_success': False}

    save(clear_data())

def test_register():
    # normal functioning with one user
    user_info = register("minglang@gmail.com", "12345678", "minglang", "xie")
    assert user_info == {'u_id': 0, 'token': generateToken(0)}
    assert login("minglang@gmail.com", "12345678") == user_info

    # create another user to see if the user successful joined into list
    user_info2 = register("Phranqueli@gmail.com", "abcd1234", "Yun", "Li")
    assert user_info2 == {'u_id': 1, 'token': generateToken(1)}
    assert login("Phranqueli@gmail.com", "abcd1234") == user_info2

    data = getData()    # see i the total number of user increased
    assert len(data['users']) == 2
    save(clear_data())

    # the email is invalid
    with pytest.raises(Value_Error):
        register("minglang_gmail.com", "12345", "minglang", "xie")
    save(clear_data())

    # Email address is already being used by another user
    register("minglang@gmail.com", "12345678", "minglang", "xie")
    with pytest.raises(Value_Error):
        register("minglang@gmail.com", "23456456", "xie", "minglang")
    save(clear_data())

    # password is below 6 characters characters in length
    with pytest.raises(Value_Error):
        register("minglang@gmail.com", "12345", "minglang", "xie")
    save(clear_data())

    # name_first is not between 1 and 50 characters in length
    with pytest.raises(Value_Error):
        register("minglang@gmail.com", "12345678", "Y" * 51, "Li")
    save(clear_data())

    # name_last is not between 1 and 50 characters in length
    with pytest.raises(Value_Error):
        register("minglang@gmail.com", "12345678", "Yun", "L" * 51)
    save(clear_data())

def test_password_request_and_reset():
    user_info = register("minglang@gmail.com", "12345678", "minglang", "xie")
    reset_code = passwordreset_request("minglang@gmail.com")
    passwordreset_reset(reset_code['reset_code'], '87654321')
    assert login("minglang@gmail.com", "87654321") == user_info
    save(clear_data())

    # Password entered is not a valid password
    register("minglang@gmail.com", "12345678", "minglang", "xie")
    reset_code = passwordreset_request("minglang@gmail.com")
    with pytest.raises(Value_Error):
        passwordreset_reset(reset_code['reset_code'], '123')
    save(clear_data())

    # reset_code is not a valid reset code
    register("minglang@gmail.com", "12345678", "minglang", "xie")
    reset_code = passwordreset_request("minglang@gmail.com")
    with pytest.raises(Value_Error):
        passwordreset_reset('aaaaa', '87654321')
    save(clear_data())

def test_all_user():
    user_info = register("minglang@gmail.com", "12345678", "minglang", "xie")
    assert all_user(user_info['token']) == {
                'users': [{
                    'u_id': user_info['u_id'],
                    'email': "minglang@gmail.com",
                    'name_first': "minglang",
                    'name_last': "xie",
                    'handle_str': "minglangxie",
                    'profile_img_url': '/user_image?file=default.jpg'
                }]
            }
    save(clear_data())

def test_profile():
    # normal case
    user_info = register("minglang@gmail.com", "12345678", "minglang", "xie")
    assert profile(user_info['token'], user_info['u_id']) == {
        'email': "minglang@gmail.com",
        'name_first': "minglang",
        'name_last': "xie",
        'handle_str': "minglangxie",
        'profile_img_url': '/user_image?file=default.jpg'
    }
    save(clear_data())
    # complex normal case with repeated user name, capital user name
    user_info = register("minglang@gmail.com", "12345678", "minglang", "xie")
    assert profile(user_info['token'], user_info['u_id']) == {
        'email': "minglang@gmail.com",
        'name_first': "minglang",
        'name_last': "xie",
        'handle_str': "minglangxie",
        'profile_img_url': '/user_image?file=default.jpg'
    }
    user_info2 = register("Phranqueli@gmail.com", "asdfdsas", "minglang", "xie")
    assert profile(user_info2['token'], user_info2['u_id']) == {
        'email': "Phranqueli@gmail.com",
        'name_first': "minglang",
        'name_last': "xie",
        'handle_str': "1minglangxie1",
        'profile_img_url': '/user_image?file=default.jpg'
    }
    user_info3 = register("liyun8185@126.com", "asdfdsas", "MINGLANG", "Xie")
    assert profile(user_info2['token'], user_info3['u_id']) == {
        'email': "liyun8185@126.com",
        'name_first': "MINGLANG",
        'name_last': "Xie",
        'handle_str': "2minglangxie2",
        'profile_img_url': '/user_image?file=default.jpg'
    }
    save(clear_data())
    # two same name, made second one diff
    user_info = register("minglang@gmail.com", "12345678", "minglang", "xie")
    user_info2 = register("w17a.credible4@gmail.com", "12345678", "minglang", "xie")
    assert profile(user_info2['token'], user_info2['u_id']) == {
        'email': "w17a.credible4@gmail.com",
        'name_first': "minglang",
        'name_last': "xie",
        'handle_str': "1minglangxie1",
        'profile_img_url': '/user_image?file=default.jpg'
    }
    save(clear_data())
    # the first name and last name registered is too short, so we need to modify them to make them long enough
    user_info = register("minglang@gmail.com", "12345678", "m", "x")
    assert profile(user_info['token'], user_info['u_id']) == {
        'email': "minglang@gmail.com",
        'name_first': "m",
        'name_last': "x",
        'handle_str': "0mx0",
        'profile_img_url': '/user_image?file=default.jpg'
    }
    save(clear_data())
    # complex case, two people who use different first and last name but after cut off to 20 characters, their stirng user name is same, we check is the handle str generateed is different
    user_info = register("minglang@gmail.com", "12345678", "m" * 20, "x")
    assert profile(user_info['token'], user_info['u_id']) == {
        'email': "minglang@gmail.com",
        'name_first': "m" * 20,
        'name_last': "x",
        'handle_str': "mmmmmmmmmmmmmmmmmmmm",
        'profile_img_url': '/user_image?file=default.jpg'
    }
    user_info = register("liyun8185g@126.com", "12345678", "m" * 19, "mx")
    assert profile(user_info['token'], user_info['u_id']) == {
        'email': "liyun8185g@126.com",
        'name_first': "m" * 19,
        'name_last': "mx",
        'handle_str': "1mmmmmmmmmmmmmmmmmm1",
        'profile_img_url': '/user_image?file=default.jpg'
    }
    save(clear_data())
    # too short first and last name
    user_info = register("minglang@gmail.com", "12345678", "m", "x")
    with pytest.raises(Value_Error):
        profile(user_info['token'], 1)
    save(clear_data())

def test_setname():
    # normal functioning
    user_info = register("minglang@gmail.com", "12345678", "minglang", "xie")
    setname(user_info['token'], 'li', 'yu')
    assert profile(user_info['token'], user_info['u_id']) == {
        'email': "minglang@gmail.com",
        'name_first': "li",
        'name_last': "yu",
        'handle_str': "minglangxie",
        'profile_img_url': '/user_image?file=default.jpg'
    }
    save(clear_data())
    # normal functioning with exactly 50 character's last name and first name
    user_info = register("minglang@gmail.com", "12345678", "minglang", "xie")
    setname(user_info['token'], 'l' * 50, 'y' * 50)
    assert profile(user_info['token'], user_info['u_id']) == {
        'email': "minglang@gmail.com",
        'name_first': 'l' * 50,
        'name_last': 'y' * 50,
        'handle_str': "minglangxie",
        'profile_img_url': '/user_image?file=default.jpg'
    }
    save(clear_data())

    # name_first has no length
    user_info = register("minglang@gmail.com", "12345678", "minglang", "xie")
    with pytest.raises(Value_Error):
        setname(user_info['token'], '', 'yu')
    save(clear_data())

    # name_first is longer than 50 characters in length
    user_info = register("minglang@gmail.com", "12345678", "minglang", "xie")
    with pytest.raises(Value_Error):
        setname(user_info['token'], "y" * 51, 'yu')
    save(clear_data())

    # name_last has no length
    user_info = register("minglang@gmail.com", "12345678", "minglang", "xie")
    with pytest.raises(Value_Error):
        setname(user_info['token'], 'li', '')
    save(clear_data())

    # name_last has length longer tan 50 characters
    user_info = register("minglang@gmail.com", "12345678", "minglang", "xie")
    with pytest.raises(Value_Error):
        setname(user_info['token'], 'li', '')
    save(clear_data())

def test_setemail():
    user_info = register("minglang@gmail.com", "12345678", "minglang", "xie")
    setemail(user_info['token'], 'w17a.credible4@gmail.com')
    assert profile(user_info['token'], user_info['u_id']) == {
        'email': "w17a.credible4@gmail.com",
        'name_first': "minglang",
        'name_last': "xie",
        'handle_str': "minglangxie",
        'profile_img_url': '/user_image?file=default.jpg'
    }
    save(clear_data())

    # Email address is already being used by another user
    user_info = register("minglang@gmail.com", "12345678", "minglang", "xie")
    with pytest.raises(Value_Error):
        setemail(user_info['token'], 'minglang@gmail.com')
    save(clear_data())

    # Email entered is not a valid email
    user_info = register("minglang@gmail.com", "12345678", "minglang", "xie")
    with pytest.raises(Value_Error):
        setemail(user_info['token'], 'w17a.credible4_gmail.com')
    save(clear_data())

def test_sethandle():
    user_info = register("minglang@gmail.com", "12345678", "minglang", "xie")
    sethandle(user_info['token'], 'lol')
    assert profile(user_info['token'], user_info['u_id']) == {
        'email': "minglang@gmail.com",
        'name_first': "minglang",
        'name_last': "xie",
        'handle_str': "lol",
        'profile_img_url': '/user_image?file=default.jpg'
    }
    save(clear_data())

    # handle is already used by another user
    user_info = register("minglang@gmail.com", "12345678", "minglang", "xie")
    sethandle(user_info['token'], 'lol')
    with pytest.raises(Value_Error):
        sethandle(user_info['token'], 'lol')
    save(clear_data())

    # handle_str must be between 3 and 20 characters
    user_info = register("minglang@gmail.com", "12345678", "minglang", "xie")
    with pytest.raises(Value_Error):
        sethandle(user_info['token'], 'ab')
    save(clear_data())

    # handle_str must be between 3 and 20 characters
    user_info = register("minglang@gmail.com", "12345678", "minglang", "xie")
    with pytest.raises(Value_Error):
        sethandle(user_info['token'], 'minglang' * 20)
    save(clear_data())

def test_uploadphoto():
    user_info = register("minglang@gmail.com", "12345678", "minglang", "xie")
    assert profile(user_info['token'], user_info['u_id']) == {
        'email': "minglang@gmail.com",
        'name_first': "minglang",
        'name_last': "xie",
        'handle_str': "minglangxie",
        'profile_img_url': '/user_image?file=default.jpg'
    }
    uploadphoto(user_info['token'],
                'https://assets1.ignimgs.com/2019/04/23/doraemon-story-of-seasons---button-01-1556056822190.jpg',
                0, 0, 720, 720)
    assert profile(user_info['token'], user_info['u_id']) == {
        'email': "minglang@gmail.com",
        'name_first': "minglang",
        'name_last': "xie",
        'handle_str': "minglangxie",
        'profile_img_url': '/user_image?file=' + str(user_info['token']) + '.jpg'
    }
    img_addr = './server/user_image/' + str(user_info['token']) + '.jpg'
    os.remove(img_addr)

    # any of x_start, y_start, x_end, y_end are not within the dimensions of the image at the URL
    with pytest.raises(Value_Error):
        uploadphoto(user_info['token'],
                    'https://assets1.ignimgs.com/2019/04/23/doraemon-story-of-seasons---button-01-1556056822190.jpg',
                    0, 0, 800, 800)

    # img_url is returns an HTTP status other than 200
    with pytest.raises(Value_Error):
        uploadphoto(user_info['token'],
                    'https://images-na.ssl-images-amazon.com/images/I/71hEb5HHBTL.png',
                    0, 0, 512, 512)

    save(clear_data())

def test_permission():
    # normal functioning
    user_info1 = register("minglang@gmail.com", "12345678", "minglang", "xie")
    user_info2 = register("w17a.credible4@gmail.com", "12345678", "minglang", "xie")
    # 3 to 2
    permission(user_info1['token'], user_info2['u_id'], 2)
    data = getData()
    assert data['users'][user_info2['u_id']]['permission'] == 2

    # 2 to 1
    permission(user_info1['token'], user_info2['u_id'], 1)
    data = getData()
    assert data['users'][user_info2['u_id']]['permission'] == 1

    # 1 to 2
    permission(user_info1['token'], user_info2['u_id'], 2)
    data = getData()
    assert data['users'][user_info2['u_id']]['permission'] == 2
    save(clear_data())

    # if a member is able to change other's permission after a he become an a owner,
    user_info1 = register("minglang@gmail.com", "12345678", "minglang", "xie")
    user_info2 = register("w17a.credible4@gmail.com", "12345678", "minglang", "xie")
    user_info3 = register("Phranqueli@gmail.com", "12345678", "Yun", "Li")
    # 3 to 1
    permission(user_info1['token'], user_info2['u_id'], 1)
    data = getData()
    assert data['users'][user_info2['u_id']]['permission'] == 1

    # 3 to 1 by new owner
    permission(user_info2['token'], user_info3['u_id'], 1)
    data = getData()
    assert data['users'][user_info3['u_id']]['permission'] == 1

    # 1 to 3 by new owner
    permission(user_info3['token'], user_info1['u_id'], 3)
    data = getData()
    assert data['users'][user_info1['u_id']]['permission'] == 3
    #now he should has no permission to change other's permisssion
    with pytest.raises(Value_Error):
        permission(user_info1['token'], user_info2['u_id'], 2)

    # 1 to 2
    permission(user_info3['token'], user_info1['u_id'], 2)
    data = getData()
    assert data['users'][user_info1['u_id']]['permission'] == 2

    # 1 to 3 by new admin
    permission(user_info1['token'], user_info2['u_id'], 3)
    data = getData()
    assert data['users'][user_info2['u_id']]['permission'] == 3
    # now he should has no permission to change other's permisssion
    with pytest.raises(Value_Error):
        permission(user_info2['token'], user_info3['u_id'], 1)

    save(clear_data())

    # permission_id does not refer to a value permission
    user_info1 = register("minglang@gmail.com", "12345678", "minglang", "xie")
    user_info2 = register("w17a.credible4@gmail.com", "12345678", "minglang", "xie")
    with pytest.raises(Value_Error):
        permission(user_info1['token'], user_info2['u_id'], 4)
    save(clear_data())

    # u_id does not refer to a valid user
    user_info1 = register("minglang@gmail.com", "12345678", "minglang", "xie")
    user_info2 = register("w17a.credible4@gmail.com", "12345678", "minglang", "xie")
    with pytest.raises(Value_Error):
        permission(user_info1['token'], 3, 2)
    save(clear_data())

    # The authorised user is not an admin or owner
    user_info1 = register("minglang@gmail.com", "12345678", "minglang", "xie")
    user_info2 = register("w17a.credible4@gmail.com", "12345678", "minglang", "xie")
    with pytest.raises(Value_Error):
        permission(user_info2['token'], user_info2['u_id'], 2)
    save(clear_data())

""" BELOW TEST IS TESTING CHANNEL FUNCTION """
def test_create_list_listall():

    user_info1 = register("minglang@gmail.com", "12345678", "minglang", "xie")

    #check when people join or created no channel
    assert user_channel_list(user_info1['token']) == {'channels': []}
    assert listall(user_info1['token']) == {'channels':[]}

    user_info2 = register("w17a.credible4@gmail.com", "12345678", "minglang", "xie")
    create(user_info1['token'], 'lol', True)
    create(user_info2['token'], 'wtf', True)

    # check channel_id and diff ppl create a channel
    assert user_channel_list(user_info1['token']) == {'channels': [{'channel_id': 0, 'name': 'lol'}]}
    assert user_channel_list(user_info2['token']) == {'channels': [{'channel_id': 1, 'name': 'wtf'}]}
    # check channel_list_all
    assert listall(user_info1['token']) == {'channels':[{'channel_id': 0, 'name': 'lol'}, {'channel_id': 1, 'name': 'wtf'}]}
    assert listall(user_info1['token']) == listall(user_info2['token'])
    # check channel_deatil
    assert details(user_info1['token'], 0) == {
        'name': 'lol',
        'owner_members': [{'u_id': user_info1['u_id'], 'profile_img_url': '/user_image?file=default.jpg', 'name_first': "minglang", 'name_last': "xie"}],
        'all_members': [{'u_id': user_info1['u_id'], 'profile_img_url': '/user_image?file=default.jpg', 'name_first': "minglang", 'name_last': "xie"}],
    }
    save(clear_data())

    # the token doesn't exist
    user_info1 = register("minglang@gmail.com", "12345678", "minglang", "xie")
    user_info2 = register("w17a.credible4@gmail.com", "12345678", "minglang", "xie")
    data = getData()
    token = generateToken(len(data['users']))
    with pytest.raises(Value_Error):
        create(token, 'lol', True)
    save(clear_data())

    #check channel_create: the name is longer than 20 character
    user_info1 = register("minglang@gmail.com", "12345678", "minglang", "xie")
    user_info2 = register("w17a.credible4@gmail.com", "12345678", "minglang", "xie")
    with pytest.raises(Value_Error):
        create(user_info1['token'], 'lol' * 20, True)
    save(clear_data())

def test_detail():
    user_info1 = register("minglang@gmail.com", "12345678", "minglang", "xie")
    user_info2 = register("w17a.credible4@gmail.com", "12345678", "minglang", "xie")
    create(user_info1['token'], 'lol', True)
    create(user_info2['token'], 'wtf', True)
    # check channel_deatil
    assert details(user_info1['token'], 0) == {
        'name': 'lol',
        'owner_members': [{'u_id': user_info1['u_id'], 'profile_img_url': '/user_image?file=default.jpg', 'name_first': "minglang", 'name_last': "xie"}],
        'all_members': [{'u_id': user_info1['u_id'], 'profile_img_url': '/user_image?file=default.jpg', 'name_first': "minglang", 'name_last': "xie"}],
    }
    save(clear_data())

    # Channel ID is not a valid channel
    user_info1 = register("minglang@gmail.com", "12345678", "minglang", "xie")
    user_info2 = register("w17a.credible4@gmail.com", "12345678", "minglang", "xie")
    create(user_info1['token'], 'lol', True)
    with pytest.raises(Value_Error):
        details(user_info1['token'], 1)
    save(clear_data())

    # Authorised user is not a member of channel with channel_id
    user_info1 = register("minglang@gmail.com", "12345678", "minglang", "xie")
    user_info2 = register("w17a.credible4@gmail.com", "12345678", "minglang", "xie")
    create(user_info1['token'], 'lol', True)
    with pytest.raises(AccessError):
        details(user_info2['token'], 0)
    save(clear_data())

def test_channel_invite():
    user_info1 = register("minglang@gmail.com", "12345678", "minglang", "xie")
    user_info2 = register("w17a.credible4@gmail.com", "12345678", "minglang", "xie")
    user_info3 = register("Phranqueli@gmail.com", "12345678", "Frank", "Li")

    # channel_id does not refer to a valid channel that the authorised user is part of
    create(user_info1['token'], 'lol', True)
    with pytest.raises(Value_Error):
        invite(user_info1['token'], 2, user_info2['u_id'])

    # u_id does not refer to a valid user
    with pytest.raises(Value_Error):
        invite(user_info1['token'], 0, 4)

    #  AccessError whenthe authorised user is not already a member of the channel
    with pytest.raises(AccessError):
        invite(user_info2['token'], 0, user_info1['u_id'])

    #  AccessError whenthe authorised user is not already a member of the channel
    with pytest.raises(AccessError):
        invite(user_info3['token'], 0, user_info2['u_id'])

    invite(user_info1['token'], 0, user_info2['u_id'])
    data = getData()

    assert{'u_id': user_info2['u_id'], 'profile_img_url': '/user_image?file=default.jpg', 'name_first': data['users'][user_info2['u_id']]['name_first'], 'name_last': data['users'][user_info2['u_id']]['name_last']} in data['channels_list'][0]['members']

    invite(user_info1['token'], 0, user_info2['u_id'])
    data = getData()
    assert len(data['channels_list'][0]['members']) == 2
    save(clear_data())

def test_channel_leave():
    user_info1 = register("minglang@gmail.com", "12345678", "minglang", "xie")
    user_info2 = register("w17a.credible4@gmail.com", "12345678", "minglang", "xie")
    create(user_info1['token'], 'lol', True)
    invite(user_info1['token'], 0, user_info2['u_id'])

    data = getData()
    assert len(data['channels_list'][0]['members']) == 2

    # Channel ID is not a valid channel
    with pytest.raises(Value_Error):
        leave(user_info2['token'], 1)

    leave(user_info2['token'], 0)
    data = getData()
    assert len(data['channels_list'][0]['members']) == 1

    # leave again, and it should have no change
    leave(user_info2['token'], 0)
    data = getData()
    assert len(data['channels_list'][0]['members']) == 1
    save(clear_data())

def test_join():
    user_info1 = register("minglang@gmail.com", "12345678", "minglang", "xie")
    user_info2 = register("w17a.credible4@gmail.com", "12345678", "minglang", "xie")
    create(user_info1['token'], 'lol', True)
    join(user_info2['token'], 0)

    data = getData()
    assert len(data['channels_list'][0]['members']) == 2

    # nothing change if join the same ppl
    join(user_info2['token'], 0)
    data = getData()
    assert len(data['channels_list'][0]['members']) == 2

    # Channel ID is not a valid channel
    leave(user_info2['token'], 0)
    with pytest.raises(Value_Error):
        join(user_info2['token'], 1)

    # a private channel can only be joined by invitation
    create(user_info1['token'], 'lol', False)
    with pytest.raises(AccessError):
        join(user_info2['token'], 1)
    save(clear_data())

def test_addowner_and_remove():
    user_info1 = register("minglang@gmail.com", "12345678", "minglang", "xie")
    user_info2 = register("w17a.credible4@gmail.com", "12345678", "minglang", "xie")
    create(user_info1['token'], 'lol', True)
    join(user_info2['token'], 0)

    addowner(user_info1['token'], 0, user_info2['u_id'])
    data = getData()
    assert len(data['channels_list'][0]['owners']) == 2

    removeowner(user_info1['token'], 0, user_info2['u_id'])
    data = getData()
    assert len(data['channels_list'][0]['owners']) == 1

    # Channel ID is not a valid channel
    with pytest.raises(Value_Error):
        addowner(user_info1['token'], 1, user_info2['u_id'])

    # you don't have the right to access to add owner
    with pytest.raises(AccessError):
        addowner(user_info2['token'], 0, user_info2['u_id'])

    # you don't have the right to access to remove owner
    with pytest.raises(AccessError):
        removeowner(user_info2['token'], 0, user_info2['u_id'])

    # the user id is already an owner
    addowner(user_info1['token'], 0, user_info2['u_id'])
    data = getData()
    assert len(data['channels_list'][0]['owners']) == 2

    with pytest.raises(Value_Error):
        addowner(user_info1['token'], 0, user_info2['u_id'])

    # Channel ID: is not a valid channel
    with pytest.raises(Value_Error):
        removeowner(user_info1['token'], 1, user_info2['u_id'])

    save(clear_data())

""" BELOW TEST IS TESTING MESSAGE FUNCTION """
def test_message_sendlater():
    user_info1 = register("minglang@gmail.com", "12345678", "minglang", "xie")
    user_info2 = register("w17a.credible4@gmail.com", "12345678", "minglang", "xie")
    create(user_info1['token'], 'lol', True)
    sent_time_before = dt.utcnow() - timedelta(minutes=15)
    sent_time_after = dt.utcnow() + timedelta(minutes=15)
    sendlater(user_info1['token'], 0, "first message", sent_time_after)

    data = getData()
    assert (data['messages'][0]['message'] == "first message" and data['messages'][0]['time_created'] == sent_time_after)

    # Channel ID: is not a valid channel
    with pytest.raises(Value_Error):
        sendlater(user_info1['token'], 1, "second message", sent_time_after)

    # Message is more than 1000 characters
    with pytest.raises(Value_Error):
        sendlater(user_info1['token'], 0, "second message" * 500, sent_time_after)

    # the authorised user has not joined the channel they are trying to post to
    with pytest.raises(AccessError):
        sendlater(user_info2['token'], 0, "second message", sent_time_after)

    # Time sent is a time in the past
    with pytest.raises(Value_Error):
        sendlater(user_info1['token'], 0, "second message", sent_time_before)

    # if the given time type is not datetime
    sendlater(user_info1['token'], 0, "first message", sent_time_after.replace(tzinfo=timezone.utc).timestamp())

    data = getData()
    assert (data['messages'][0]['message'] == "first message" and data['messages'][0]['time_created'] == sent_time_after)
    save(clear_data())

def test_message_send():
    user_info1 = register("minglang@gmail.com", "12345678", "minglang", "xie")
    user_info2 = register("w17a.credible4@gmail.com", "12345678", "minglang", "xie")
    create(user_info1['token'], 'lol', True)
    send(user_info1['token'], 0, "first message")

    data = getData()
    assert data['messages'][0]['message'] == "first message"

    send(user_info1['token'], 0, "second message")
    data = getData()
    assert len(data['messages']) == 2

    # Message is more than 1000 characters
    with pytest.raises(Value_Error):
        send(user_info1['token'], 0, "second message" * 500)

    # the authorised user has not joined the channel they are trying to post to
    with pytest.raises(AccessError):
        send(user_info2['token'], 0, "second message")

    save(clear_data())

def test_message_remove():
    user_info1 = register("minglang@gmail.com", "12345678", "minglang", "xie")
    user_info2 = register("w17a.credible4@gmail.com", "12345678", "minglang", "xie")
    create(user_info1['token'], 'lol', True)
    send(user_info1['token'], 0, "first message")
    remove(user_info1['token'], 0)

    data = getData()
    assert len(data['messages']) == 0

    # Message (based on ID) no longer exists
    send(user_info1['token'], 0, "first message")
    remove(user_info1['token'], 0)
    with pytest.raises(Value_Error):
        remove(user_info1['token'], 0)

    # Message with message_id was not sent by the authorised user making this request and The authorised user is not an admin or owner of this channel or the slackr
    send(user_info1['token'], 0, "first message")
    with pytest.raises(Value_Error):
        remove(user_info2['token'], 0)

    save(clear_data())

def test_message_edit():
    user_info1 = register("minglang@gmail.com", "12345678", "minglang", "xie")
    user_info2 = register("Phranqueli@gmail.com", "321654", "Frank", "Li")
    user_info3 = register("liyun8185@gmail.com", "456789", "Frank", "Li")
    create(user_info1['token'], 'lol', True)
    invite(user_info1['token'], 0, user_info2['u_id'])
    send(user_info2['token'], 0, "first message")

    edit(user_info1['token'], 0, "new first message")
    data = getData()
    assert(data['messages'][0]['message'] == "new first message")

    edit(user_info2['token'], 0, "second new first message")
    data = getData()
    assert(data['messages'][0]['message'] == "second new first message")

    # a normal member who doesn't send message wants to edit it
    with pytest.raises(AccessError):
        edit(user_info3['token'], 0, "not possible")

    # a member in channel but not the owner who doesn't send message wants to edit it
    invite(user_info1['token'], 0, user_info3['u_id'])
    with pytest.raises(AccessError):
        edit(user_info3['token'], 0, "not possible")

    # now member 3 is a admin
    data = getData()
    data['users'][2]['permission'] = 2
    edit(user_info1['token'], 0, "final message")
    data = getData()
    assert(data['messages'][0]['message'] == "final message")
    save(clear_data())

def test_message_react():
    user_info1 = register("minglang@gmail.com", "12345678", "minglang", "xie")
    user_info2 = register("w17a.credible4@gmail.com", "12345678", "minglang", "xie")
    create(user_info1['token'], 'lol', True)
    send(user_info1['token'], 0, "first message")
    react(user_info1['token'], 0, 1)

    data = getData()
    assert len(data['messages'][0]['reacts'][0]['u_ids']) == 1

    # sencond user create a channel and send a msg
    create(user_info2['token'], 'lol', True)
    send(user_info2['token'], 1, "second message")

    data = getData()
    assert len(data['messages']) == 2

    # Not a valid message within a channel that the authorised user has joined
    with pytest.raises(Value_Error):
        react(user_info1['token'], 1, 1)

    # Not a valid react_id
    with pytest.raises(Value_Error):
        react(user_info2['token'], 1, 0)

    # Message already contains active react with same react_id
    react(user_info2['token'], 1, 1)
    data = getData()
    assert len(data['messages'][1]['reacts'][0]['u_ids']) == 1

    with pytest.raises(Value_Error):
        react(user_info2['token'], 1, 1)

    save(clear_data())

def test_message_unreact():
    user_info1 = register("minglang@gmail.com", "12345678", "minglang", "xie")
    user_info2 = register("w17a.credible4@gmail.com", "12345678", "minglang", "xie")
    create(user_info1['token'], 'lol', True)
    send(user_info1['token'], 0, "first message in first channel")
    react(user_info1['token'], 0, 1)

    data = getData()
    assert len(data['messages'][0]['reacts'][0]['u_ids']) == 1

    # sencond user create a channel and send a msg and react by itself
    create(user_info2['token'], 'lol', True)
    send(user_info2['token'], 1, "first message in second channel")
    react(user_info2['token'], 1, 1)

    data = getData()
    assert len(data['messages']) == 2

    # Not a valid message within a channel that the authorised user has joined
    with pytest.raises(Value_Error):
        unreact(user_info1['token'], 1, 1)

    # Not a valid react_id
    with pytest.raises(Value_Error):
        unreact(user_info2['token'], 1, 0)

    # Message with ID message_id does not contain an active React with ID react_id
    send(user_info2['token'], 1, "third message")
    data = getData()
    assert len(data['messages'][2]['reacts'][0]['u_ids']) == 0

    with pytest.raises(Value_Error):
        unreact(user_info2['token'], 2, 1)

    # pass test
    unreact(user_info2['token'], 1, 1)
    data = getData()
    assert len(data['messages'][1]['reacts'][0]['u_ids']) == 0

    save(clear_data())

def test_message_pin():
    user_info1 = register("minglang@gmail.com", "12345678", "minglang", "xie")
    user_info2 = register("w17a.credible4@gmail.com", "12345678", "minglang", "xie")
    create(user_info1['token'], 'lol', True)
    send(user_info1['token'], 0, "first message")
    pin(user_info1['token'], 0)

    data = getData()
    assert data['messages'][0]['is_pinned'] == True

    # Message_Id is not a valid message
    with pytest.raises(Value_Error):
        pin(user_info1['token'], 1)

    # Message with ID message_id already pinned
    with pytest.raises(Value_Error):
        pin(user_info1['token'], 0)

    # The user is not an admin
    with pytest.raises(Value_Error):
        pin(user_info2['token'], 0)

    save(clear_data())

    user_info1 = register("minglang@gmail.com", "12345678", "minglang", "xie")
    user_info2 = register("w17a.credible4@gmail.com", "12345678", "minglang", "xie")
    create(user_info2['token'], 'lol', True)
    send(user_info2['token'], 0, "first message")

    # The authorised user is not a member of the channel that the message is within
    with pytest.raises(AccessError):
        pin(user_info1['token'], 0)

    save(clear_data())

def test_message_unpin():
    user_info1 = register("minglang@gmail.com", "12345678", "minglang", "xie")
    user_info2 = register("w17a.credible4@gmail.com", "12345678", "minglang", "xie")
    create(user_info1['token'], 'lol', True)
    send(user_info1['token'], 0, "first message")
    pin(user_info1['token'], 0)
    unpin(user_info1['token'], 0)
    data = getData()
    assert data['messages'][0]['is_pinned'] == False

    # Message_Id is not a valid message
    with pytest.raises(Value_Error):
        unpin(user_info1['token'], 1)

    # Message with ID message_id already pinned
    with pytest.raises(Value_Error):
        unpin(user_info1['token'], 0)

   # The user is not an admin
    with pytest.raises(Value_Error):
        unpin(user_info2['token'], 0)

    save(clear_data())

    user_info1 = register("minglang@gmail.com", "12345678", "minglang", "xie")
    user_info2 = register("w17a.credible4@gmail.com", "12345678", "minglang", "xie")
    create(user_info2['token'], 'lol', True)
    send(user_info2['token'], 0, "first message")

    # The authorised user is not a member of the channel that the message is within
    with pytest.raises(AccessError):
        unpin(user_info1['token'], 0)

    save(clear_data())

def test_standup_active():
    user_info1 = register("minglang@gmail.com", "12345678", "minglang", "xie")
    user_info2 = register("w17a.credible4@gmail.com", "12345678", "minglang", "xie")
    create(user_info1['token'], 'lol', True)
    finish_time = standup_start(user_info1['token'], 0, 1)
    standup_send(user_info1['token'], 0, "hi")
    standup_send(user_info1['token'], 0, "lol")

    data = getData()
    assert standup_active(user_info1, 0) == {'is_active': True, 'time_finish': finish_time['time_finish']}

    sleep(1)
    assert standup_active(user_info1, 0) == {'is_active': False, 'time_finish': finish_time['time_finish']}

    # Channel ID: is not a valid channel
    with pytest.raises(Value_Error):
        standup_active(user_info1, 1)

    save(clear_data())

def test_standup_start_send():
    user_info1 = register("minglang@gmail.com", "12345678", "minglang", "xie")
    user_info2 = register("w17a.credible4@gmail.com", "12345678", "minglang", "xie")
    create(user_info1['token'], 'lol', True)
    finish_time = standup_start(user_info1['token'], 0, 10)
    standup_send(user_info1['token'], 0, "hi")
    standup_send(user_info1['token'], 0, "lol")

    data = getData()
    assert (len(data['messages']) == 1 and data['messages'][0]['time_created'].replace(tzinfo=timezone.utc).timestamp() == finish_time['time_finish'])
    # An active standup is currently running in this channel
    with pytest.raises(Value_Error):
        finish_time = standup_start(user_info1['token'], 0, 10)

    # Channel ID: is not a valid channel
    with pytest.raises(Value_Error):
        finish_time = standup_start(user_info1['token'], 1, 10)

    # standup_send: Channel ID: is not a valid channel
    with pytest.raises(Value_Error):
        standup_send(user_info1['token'], 1, "hi")

    # standup_send: Message is more than 1000 characters
    with pytest.raises(Value_Error):
        standup_send(user_info1['token'], 0, "hi" * 1000)

    # The authorised user is not a member of the channel that the message is within
    with pytest.raises(AccessError):
        finish_time = standup_start(user_info2['token'], 0, 10)

    # standup_send: The authorised user is not a member of the channel that the message is within
    with pytest.raises(AccessError):
        standup_send(user_info2['token'], 0, "hi")

    save(clear_data())

    # standup_send: An active standup is not currently running in this channel
    user_info1 = register("minglang@gmail.com", "12345678", "minglang", "xie")
    user_info2 = register("w17a.credible4@gmail.com", "12345678", "minglang", "xie")
    create(user_info1['token'], 'lol', True)

    # The authorised user is not a member of the channel that the message is within
    with pytest.raises(Value_Error):
        standup_send(user_info1['token'], 0, "hi")

    save(clear_data())

def test_search():
    user_info1 = register("minglang@gmail.com", "12345678", "minglang", "xie")
    user_info2 = register("w17a.credible4@gmail.com", "12345678", "minglang", "xie")
    create(user_info1['token'], 'lol', True)
    send(user_info1['token'], 0, "first message")
    send(user_info1['token'], 0, "second message")

    messages = search(user_info1['token'], 'mess')
    assert len(messages['messages']) == 2

    messages = search(user_info1['token'], 'p')
    assert len(messages['messages']) == 0

    messages = search(user_info1['token'], '')
    assert len(messages['messages']) == 0

    messages = search(user_info1['token'], 'second')
    assert len(messages['messages']) == 1

    save(clear_data())

def test_channel_messages():
    user_info1 = register("minglang@gmail.com", "12345678", "minglang", "xie")
    user_info2 = register("w17a.credible4@gmail.com", "12345678", "minglang", "xie")
    create(user_info1['token'], 'lol', True)
    send(user_info1['token'], 0, "first message")
    send(user_info1['token'], 0, "second message")

    channel_message = messages(user_info1['token'], 0, 0)
    assert (len(channel_message['messages']) == 2) and (channel_message['start'] == 0 and channel_message['end'] == -1)

    channel_message = messages(user_info1['token'], 0, 1)
    assert (len(channel_message['messages']) == 1) and (channel_message['start'] == 1 and channel_message['end'] == -1)

    edit(user_info1['token'], 0, '')
    channel_message = messages(user_info1['token'], 0, 0)
    assert (len(channel_message['messages']) == 1) and (channel_message['start'] == 0 and channel_message['end'] == -1)

    # start is greater than or equal to the total number of messages in the channel
    with pytest.raises(Value_Error):
        channel_message = messages(user_info1['token'], 0, 2)

    # Channel ID: is not a valid channel
    with pytest.raises(Value_Error):
        channel_message = messages(user_info1['token'], 1, 0)

    # Authorised user is not a member of channel with channel_id
    with pytest.raises(AccessError):
        channel_message = messages(user_info2['token'], 0, 0)

    save(clear_data())

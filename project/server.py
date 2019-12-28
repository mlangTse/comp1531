''' Flask server '''
import sys
from json import dumps
from datetime import datetime as dt
from flask import Flask, request, send_from_directory
from flask_mail import Mail, Message
from flask_cors import CORS
from server.auth_function import login, logout, register, passwordreset_request, passwordreset_reset
from server.auth_function import profile, setname, setemail, sethandle, permission, uploadphoto, all_user
from server.channel_function import invite, details, messages, leave, join
from server.channel_function import addowner, removeowner, user_channel_list, listall, create
from server.message_function import sendlater, send, remove, edit, react, unreact
from server.message_function import pin, unpin, standup_start, standup_active, standup_send, search
from server.help_server import defaultHandler, getData

APP = Flask(__name__)
APP.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME="w17a.credible4@gmail.com",
    MAIL_PASSWORD="Credible4_four"
)
APP.config['TRAP_HTTP_EXCEPTIONS'] = True
APP.register_error_handler(Exception, defaultHandler)
CORS(APP)

def sent_mail(email, message):
    """ senting reset code """
    mail = Mail(APP)
    msg = Message("The reset code from Slack",
                  sender="w17a.credible4@gmail.com",
                  recipients=[email])
    msg.body = f"The reset code from slackr: {message}"
    mail.send(msg)
    return

@APP.route('/echo/get', methods=['GET'])
def echo1():
    """ Returns the input """
    return dumps({
        'echo' : request.args.get('echo'),
    })

@APP.route('/echo/post', methods=['POST'])
def echo2():
    """ Returns the input """
    return dumps({
        'echo' : request.form.get('echo'),
    })

@APP.route('/auth/login', methods=['POST'])
def auth_login():
    """ return token and u_id """
    result = login(request.form.get('email'), request.form.get('password'))
    return dumps(result)

@APP.route('/auth/logout', methods=['POST'])
def auth_logout():
    """ return a bool type "is_success" """
    result = logout(request.form.get('token'))
    return dumps(result)

@APP.route('/auth/register', methods=['POST'])
def auth_register():
    """ return token and u_id """
    result = register(request.form.get('email'), request.form.get('password'),
                      request.form.get('name_first'), request.form.get('name_last'))
    return dumps(result)

@APP.route('/auth/passwordreset/request', methods=['POST'])
def auth_passwordreset_request():
    """ senting reset code return empty dic """
    email = request.form.get('email')
    reset_code = passwordreset_request(email)
    sent_mail(email, reset_code)
    return dumps({})

@APP.route('/auth/passwordreset/reset', methods=['POST'])
def auth_passwordreset_reset():
    """ return empty dic, change user's password """
    result = passwordreset_reset(request.form.get('reset_code'), request.form.get('new_password'))
    return dumps(result)

@APP.route('/channel/invite', methods=['POST'])
def channel_invite():
    """ return empty dic, invite user into a channel """
    result = invite(request.form.get('token'), int(request.form.get('channel_id')),
                    int(request.form.get('u_id')))
    return dumps(result)

@APP.route('/channel/details', methods=['GET'])
def channel_details():
    """ return name, owner_members, all_members """
    data = getData()
    base = str(request.base_url)
    result = details(request.args.get('token'), request.args.get('channel_id'))

    for owner in result['owner_members']:
        if owner['profile_img_url'] != data['users'][int(owner['u_id'])]['profile_img_url']:
            owner['profile_img_url'] = data['users'][int(owner['u_id'])]['profile_img_url']
        owner['profile_img_url'] = base + owner['profile_img_url']

    for member in result['all_members']:
        if member['profile_img_url'] != data['users'][int(owner['u_id'])]['profile_img_url']:
            member['profile_img_url'] = data['users'][int(owner['u_id'])]['profile_img_url']
        member['profile_img_url'] = base + member['profile_img_url']

    return dumps(result)

@APP.route('/channel/details/user_image', methods=['GET'])
def channel_send_js():
    picture = request.args.get('file')
    return send_from_directory('./server/user_image/', picture)

@APP.route('/channel/messages', methods=['GET'])
def channel_messages():
    """ return 'messages', 'start', 'end' """
    result = messages(request.args.get('token'), request.args.get('channel_id'),
                      request.args.get('start'))
    return dumps(result)

@APP.route('/channel/leave', methods=['POST'])
def channel_leave():
    """ return empty dic, user leave channel """
    result = leave(request.form.get('token'), int(request.form.get('channel_id')))
    return dumps(result)

@APP.route('/channel/join', methods=['POST'])
def channel_join():
    """ return empty dic, join user into a channel """
    result = join(request.form.get('token'), int(request.form.get('channel_id')))
    return dumps(result)

@APP.route('/channel/addowner', methods=['POST'])
def channel_addowner():
    """ return empty dic, make user to be owner """
    result = addowner(request.form.get('token'), int(request.form.get('channel_id')),
                      int(request.form.get('u_id')))
    return dumps(result)

@APP.route('/channel/removeowner', methods=['POST'])
def channel_removeowner():
    """ return empty dic, remove a owner """
    result = removeowner(request.form.get('token'), int(request.form.get('channel_id')),
                         int(request.form.get('u_id')))
    return dumps(result)

@APP.route('/channels/list', methods=['GET'])
def channel_list():
    """ return a list of channels """
    result = user_channel_list(request.args.get('token'))
    return dumps(result)

@APP.route('/channels/listall', methods=['GET'])
def channel_listall():
    """ return a list of channels """
    result = listall(request.args.get('token'))
    return dumps(result)

@APP.route('/channels/create', methods=['POST'])
def channel_create():
    """ return channel id """
    result = create(request.form.get('token'), request.form.get('name'),
                    request.form.get('is_public'))
    return dumps(result)

@APP.route('/message/sendlater', methods=['POST'])
def message_sendlater():
    """ return messag _id """
    result = sendlater(request.form.get('token'), int(request.form.get('channel_id')),
                       request.form.get('message'),
                       request.form.get('time_sent'))
    return dumps(result)

@APP.route('/message/send', methods=['POST'])
def message_send():
    """ return messag _id """
    result = send(request.form.get('token'), int(request.form.get('channel_id')),
                  request.form.get('message'))
    return dumps(result)

@APP.route('/message/remove', methods=['DELETE'])
def message_remove():
    """ return empty dic, remove a msg """
    result = remove(request.form.get('token'), request.form.get('message_id'))
    return dumps(result)

@APP.route('/message/edit', methods=['PUT'])
def message_edit():
    """ return empty dic, edit a msg """
    result = edit(request.form.get('token'), request.form.get('message_id'),
                  request.form.get('message'))
    return dumps(result)

@APP.route('/message/react', methods=['POST'])
def message_react():
    """ return empty dic, react a msg """
    result = react(request.form.get('token'), request.form.get('message_id'),
                   int(request.form.get('react_id')))
    return dumps(result)

@APP.route('/message/unreact', methods=['POST'])
def message_unreact():
    """ return empty dic, unreact a msg """
    result = unreact(request.form.get('token'), request.form.get('message_id'),
                     int(request.form.get('react_id')))
    return dumps(result)

@APP.route('/message/pin', methods=['POST'])
def message_pin():
    """ return empty dic, pin a msg """
    result = pin(request.form.get('token'), request.form.get('message_id'))
    return dumps(result)

@APP.route('/message/unpin', methods=['POST'])
def message_unpin():
    """ return empty dic, unpin a msg """
    result = unpin(request.form.get('token'), request.form.get('message_id'))
    return dumps(result)

@APP.route('/users/all', methods=['GET'])
def all_users():
    """ show all users """
    result = all_user(request.args.get('token'))
    return dumps(result)

@APP.route('/user/profile', methods=['GET'])
def user_profile():
    """ return 'email', 'name_first', 'name_last', 'handle_str', unpin a msg """
    result = profile(request.args.get('token'), request.args.get('u_id'))
    result['profile_img_url'] = str(request.base_url) + result['profile_img_url']
    return dumps(result)

@APP.route('/user/profile/user_image', methods=['GET'])
def send_js():
    picture = request.args.get('file')
    return send_from_directory('./server/user_image/', picture)

@APP.route('/user/profile/setname', methods=['PUT'])
def user_profile_setname():
    """ return empty dic, change user's name """
    result = setname(request.form.get('token'), request.form.get('name_first'),
                     request.form.get('name_last'))
    return dumps(result)

@APP.route('/user/profile/setemail', methods=['PUT'])
def user_profile_setemail():
    """ return empty dic, change user's email """
    result = setemail(request.form.get('token'), request.form.get('email'))
    return dumps(result)

@APP.route('/user/profile/sethandle', methods=['PUT'])
def user_profile_sethandle():
    """ return empty dic, change user's handle """
    result = sethandle(request.form.get('token'), request.form.get('handle_str'))
    return dumps(result)

@APP.route('/user/profiles/uploadphoto', methods=['POST'])
def user_profile_uploadphoto():
    """ return empty dic, change user's photo """
    uploadphoto(request.form.get('token'), request.form.get('img_url'),
                int(request.form.get('x_start')), int(request.form.get('y_start')),
                int(request.form.get('x_end')), int(request.form.get('y_end')))
    return dumps({})

@APP.route('/standup/start', methods=['POST'])
def start():
    """ return time_finish """
    result = standup_start(request.form.get('token'), int(request.form.get('channel_id')),
                           request.form.get('length'))
    return dumps(result)

@APP.route('/standup/active', methods=['GET'])
def active():
    """ return is_active, time_finish """
    result = standup_active(request.args.get('token'), int(request.args.get('channel_id')))
    return dumps(result)

@APP.route('/standup/send', methods=['POST'])
def standupsend():
    """ return empty dic, send msg to start """
    result = standup_send(request.form.get('token'), int(request.form.get('channel_id')),
                          request.form.get('message'))
    return dumps(result)

@APP.route('/search', methods=['GET'])
def message_search():
    """ return messages """
    result = search(request.args.get('token'), request.args.get('query_str'))
    return dumps(result)

@APP.route('/admin/userpermission/change', methods=['POST'])
def userpermission_change():
    """ return empty dic, change user's permission """
    result = permission(request.form.get('token'), int(request.form.get('u_id')),
                        int(request.form.get('permission_id')))
    return dumps(result)

if __name__ == '__main__':
    APP.run(port=(sys.argv[1] if len(sys.argv) > 1 else 5000), debug=True)

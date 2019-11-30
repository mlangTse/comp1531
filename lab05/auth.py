from json import dumps
from flask import Flask, request
import jwt

APP = Flask(__name__)

data = {
    'user': [],
}

def getData():
    global data
    return data

def encoding_password(password):
    data = getData()
    for user in data['user']:
        if user['password'] == password:
            secret = user['secret']
            encoded_jwt = jwt.encode({'token': password}, secret, algorithm='HS256')
            return str(encoded_jwt)
    

def decoding_password(token):
    data = getData()
    for user in data['user']:
        if encoding_password(user['password']) == token:
            secret = user['secret']
            return secret

@APP.route('/user/create', methods=['POST'])
def create():
    data = getData()
    password = request.form.get('password')
    secret = request.form.get('secret')
    user = {'password': password, 'secret': secret}
    data['user'].append(user)
    token = encoding_password(password)
    return dumps({
        'token': token,
    })

@APP.route('/user/connect', methods=['PUT'])
def connect():
    password = request.form.get('password')
    return dumps({
        'token': encoding_password(password)
    })

@APP.route('/user/secret', methods=['GET'])
def secret():
    token = request.args.get('token')
    return dumps({
        'secret': decoding_password(token)
    })

if __name__ == '__main__':
    APP.run()

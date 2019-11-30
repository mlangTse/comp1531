from json import dumps
from flask import Flask, request

APP = Flask(__name__)

data = {
    'name':[],
}

def getData():
    global data
    return data

@APP.route('/name/add', methods=['POST'])
def add():
    data = getData()
    name = request.form.get('name')
    data['name'].append(name)
    return dumps({})

@APP.route('/names', methods=['GET'])
def get_name():
    data = getData()
    return dumps(data)

@APP.route('/name/remove', methods=['DELETE'])
def remove():
    data = getData()
    remove_n = request.form.get('name')
    data['name'].remove(remove_n)
    return dumps({})

if __name__ == '__main__':
    APP.run()

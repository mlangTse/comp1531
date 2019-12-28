import sys
import os
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='prebundle')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        print(app.static_folder, path)
        return send_from_directory(app.static_folder, path)
    else:
        print(app.static_folder, 'index.html')
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(port=(int(sys.argv[1]) if len(sys.argv) > 1 else 15310), threaded=True)

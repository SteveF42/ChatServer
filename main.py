from flask import Flask
from flask_socketio import SocketIO, send
from application import create_app

app = create_app()
socketio = SocketIO(app)

app.secret_key='change later'

@socketio.on('message')
def handle_message(json):
    sentence = json['name'] + json['message']

    print('[MESSAGE]',sentence)
    socketio.send(sentence, brodcast=True)

if __name__ =='__main__':
    socketio.run(app,debug=True)
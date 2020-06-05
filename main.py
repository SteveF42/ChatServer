from flask import Flask, session
from flask_socketio import SocketIO, send
from application import create_app
from application.databse import database

app = create_app()
socketio = SocketIO(app)
db = database

app.secret_key='change later'

@socketio.on('message')
def handle_message(json):
    sentence = json['name'] + json['message']
    user = session.get('user')

    print('[MESSAGE]',sentence)
    socketio.send(sentence, brodcast=True)

if __name__ =='__main__':
    socketio.run(app,debug=True)
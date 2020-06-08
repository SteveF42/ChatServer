from flask import Flask, session
from flask_socketio import SocketIO, send
from application import create_app
from application.databse import database

app = create_app()
socketio = SocketIO(app)

app.secret_key='change later'

@socketio.on('message')
def handle_message(json):
    """
    message event that receives messages, saves them to the database,
    and sends out an object to the client
    type json: json object
    rtpe: none
    """
    sentence = json['name'] + json['message']
    msg = json['message']

    print('[MESSAGE]',sentence)
    
    db = database()
    db.insert_message(json['name'],json['message'])

    socketio.send(json, brodcast=True)

if __name__ =='__main__':
    socketio.run(app,debug=True)
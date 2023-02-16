from flask import Flask, request
from flask_socketio import SocketIO, emit, join_room, leave_room, send

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app)


@socketio.on("room_1")
def handle_event(message):
    request.sid
    print("服务器已经接收到消息：" + message)
    emit("room_1", "服务器已经接收到消息：" + message)


# 房间的概念，加入房间
@socketio.on('join')
def join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    send(f'{username} has entered the room', to=room)


# 房间的概念，离开房间
@socketio.on('leave')
def leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    send(f'{username} has left the room', to=room)


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)

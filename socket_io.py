from flask import Flask, request
from flask_socketio import SocketIO, emit, join_room, leave_room, send

app = Flask(__name__)
socketio = SocketIO(app)


# 自定义事件
@socketio.on("information")
def handle_event(*message):
    user_id = message[0]
    room = message[1]
    message_info = message[2]
    # 向房间号所有的用户发消息，不包括自己
    print(f'{user_id} to room:{room} send {message_info}')
    emit("information", message_info, to=room, include_self=False)


# 房间的概念，加入房间
@socketio.on('join')
def join(*data):
    user_id = data[0]
    room = data[1]
    join_room(room)
    # send为内置普通事件，客户端必须使用event='message'去接收消息
    # 向房间号所有的用户发消息，不包括自己
    print(f'{user_id} user has entered the room')
    send(f'{user_id} user has entered the room', to=room, include_self=False)


# 房间的概念，离开房间
@socketio.on('leave')
def leave(*data):
    user_id = data[0]
    room = data[1]
    leave_room(room)
    # send为内置普通事件，客户端必须使用event='message'去接收消息
    # 向房间号所有的用户发消息，不包括自己
    print(f'{user_id} user has left the room')
    send(f'{user_id} user has left the room', to=room)


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)

import time

import socketio

sio = socketio.Client(logger=True, engineio_logger=True)
sio.connect(url='http://10.68.178.3:7000')
print('my sid is', sio.sid)


@sio.on('connect')
def on_connect():
    print("I'm connected!")


@sio.on('scpi-response')
def on_resp(data):
    print(data)


def send_command(cmd):
    sio.emit('scpi-cmd', cmd)


def connect(ip):
    data = {"ip": f"{ip}"}
    #
    sio.emit('scpi-connect', {"ip": ip})


def disconnect():
    sio.emit('scpi-disconnect')


def add():
    cmd = """MACRo ABC <ml>
    PUBLish Run Ending Cycle</ml>"""
    send_command(cmd)


if __name__ == '__main__':
    connect("10.68.178.168")
    time.sleep(2)
    # add()
    time.sleep(3)
    disconnect()
    time.sleep(1)
    sio.disconnect()

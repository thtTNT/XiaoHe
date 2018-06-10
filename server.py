import json as jlib
import threading
import socket


class Server:
    sm = None

    def __init__(self, sm):
        global ss
        self.sm = sm
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ss.bind(("0.0.0.0",1261))
        ss.listen(5)

    def client_receive(self):
        while 1:
            conn, _ = ss.accept()
            threading.Thread(target=self.data_receive(conn)).start()

    def data_receive(self, conn):
        total_data = []
        while 1:
            data = conn.rev(1024)
            if not data:
                break
            total_data.append(data)
        msg = ''.join(total_data)
        json = jlib.loads(msg)
        p_type = json['type']
        if p_type == "speak":
            self.sm.listener.fire("MessageEvent", MessageEvent(json['data']['message']))


class MessageEvent:
    msg = ""

    def __init__(self, msg):
        self.msg = msg

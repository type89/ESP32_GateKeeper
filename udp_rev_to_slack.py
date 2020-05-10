import socket
import struct
from contextlib import closing
import slackweb
import time, datetime

UDP_IP="0.0.0.0"
UDP_PORT=9000

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP,UDP_PORT))

with closing(sock):
    while True:
        data,addr = sock.recvfrom(1024)
        #print("Send from ESP",data)
        print("Detected!")
        today = datetime.datetime.fromtimestamp(time.time())
        strtime = today.strftime('%Y/%m/%d %H:%M:%S')
        IPslack=slackweb.Slack(url="WebhookのURLを記入")
        IPslack.notify(text="Detected! " + strtime, username="Gatekeeper")

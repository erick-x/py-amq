#!/usr/bin/python
#coding:utf-8


import time
import sys
import os
import stomp
user = os.getenv("ACTIVEMQ_USER") or "admin"
password = os.getenv("ACTIVEMQ_PASSWORD") or "admin"
host = os.getenv("ACTIVEMQ_HOST") or "127.0.0.1"
port = os.getenv("ACTIVEMQ_PORT") or 61613
destination = "/topic/test"

class MyListener(object):

  def __init__(self, conn):
    self.conn = conn
    self.count = 0
    self.start = time.time()
    self.statu = True

  def on_error(self, headers, message):
    print('received an error %s' % message)

  def on_message(self, headers, message):
    print message
    if message == "SHUTDOWN":
      diff = time.time() - self.start

      print("Received %s in %f seconds" % (self.count, diff))

      self.statu = False
      self.conn.disconnect()

      #sys.exit(0)
    else:
      if self.count==0:
        self.start = time.time()

      self.count += 1
      if self.count % 1000 == 0:
        print("Received %s messages." % self.count)


  def on_statu(self):
    return self.statu

client = stomp.Connection(host_and_ports = [(host, port)])
listener =MyListener(client)
client.set_listener('test', listener)
client.start()
client.connect(login=user,passcode=password)
client.subscribe(destination=destination, id=1)
print("Waiting for messages...")

while 1:
  time.sleep(0.01)
  #断线重连
  # if listener.on_statu() == False:
  #   print "False"
  # else:
  #   print "True"


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
import time


address = ('192.168.1.118', 8187)

with socket.socket(family=socket.AF_INET,
                   type=socket.SOCK_STREAM) as simple_client:
  simple_client.connect(address)
  # while True:
  #   time.sleep(5)
  while True:
    text = input('{}:$ '.format(address[0]))
    if text != 'EOF':
      simple_client.sendall(text.encode('utf-8'))
      res = simple_client.recv(1024)
      print(str(res, encoding='utf-8'))
    else:
      break
  print('END!')


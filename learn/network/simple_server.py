#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
import time

address = ('192.168.1.118', 8187)


with socket.socket(family=socket.AF_INET,
                   type=socket.SOCK_STREAM) as simple_server:

  simple_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  simple_server.bind(address)
  simple_server.listen(2)

  while True:
    try:
      conn, addr = simple_server.accept()
    except KeyboardInterrupt:
      print('killed by user!')
      break
    with conn:
      print('Connection From ', addr)
      break
      # while True:
      #   data = conn.recv(1024)
      #   if data:
      #     print(str(data, encoding='utf-8'))
      #     conn.sendall(data)
      #   else:
      #     break
  print('server close!')

  # while True:
  #   time.sleep(5)



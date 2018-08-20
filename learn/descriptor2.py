#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class MaxValDes(object):
  def __init__(self, inti_val, max_val):
    self.value = inti_val
    self.max_val = max_val

  def __get__(self, instance, typ):
    return self.value

  def __set__(self, instance, value):
    self.value = min(self.max_val, value)


class Widget(object):
  a = MaxValDes(0, 10)


if __name__ == '__main__':
  w0 = Widget()
  print('inited w0', w0.a)
  w0.a = 123
  print('after set w0', w0.a)
  w1 = Widget()
  print('inited w1', w1.a)

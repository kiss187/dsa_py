#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class MaxValDes(object):
  def __init__(self, attr, max_val):
    print('init MaxValDes {}, {}'.format(attr, max_val))
    self.attr = attr
    self.max_val = max_val

  def __get__(self, instance, typ):
    print('__get__ {} of {}-attr'.format(instance, typ))
    return instance.__dict__[self.attr]

  def __set__(self, instance, value):
    print('__set__ {} of {}-attr'.format(instance, value))
    instance.__dict__[self.attr] = min(self.max_val, value)


class Widget(object):
  a = MaxValDes('a', 10)
  b = MaxValDes('b', 12)

  def __init__(self):
    print('__init__ Widget')
    self.a = 0
    self.b = 1


if __name__ == '__main__':
  w0 = Widget()
  print(id(w0.a), id(w0.b))
  print(w0.__dict__)

  # print(Widget.a)
  # raise AttributeError: 'NoneType' object has no attribute '__dict__'

  print('inited w0', w0.a, w0.b)

  w0.a = 123
  w0.b = 123
  print('after set w0', w0.a, w0.b)

  w1 = Widget()
  print('inited w1', w1.a, w1.b)


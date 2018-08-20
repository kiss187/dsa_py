#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class MaxValDes(object):
  def __init__(self, attr, max_val):
    self.attr = attr
    self.max_val = max_val

  def __get__(self, instance, typ):
    return instance.__dict__[self.attr]

  def __set__(self, instance, value):
    instance.__dict__[self.attr] = min(self.max_val, value)
    print('MaxValDes __set__', self.attr, instance.__dict__[self.attr])


class Widget(object):
  a = MaxValDes('a', 10)

  def __init__(self):
    self.a = 0

  def __setattr__(self, name, value):
      self.__dict__[name] = value
      print('Widget __setattr__', name, self.__dict__[name])


if __name__ == '__main__':
  """
  因此：对于属性赋值，obj = Clz(), 那么obj.attr = var，按照这样的顺序：

（1）如果Clz定义了__setattr__方法，那么调用该方法，否则

（2）如果“attr”是出现在Clz或其基类的__dict__中， 且attr是data descriptor， 那么调用其__set__方法, 否则

（3）等价调用obj.__dict__['attr'] = var 
  """
  w0 = Widget()
  w0.a = 123

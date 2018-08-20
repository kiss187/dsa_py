#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def user_defined_fuc():
  return 'user_defined_fuc'


class MyClass:
  x = user_defined_fuc

  def __init__(self, func):
    self.y = func

  def method(self):
    return 'instance method called', self

  @classmethod
  def c_method(cls):
    return 'class method called', cls

  @staticmethod
  def s_method():
    return 'static method called'


print('info of user_defined_func:',
      id(user_defined_fuc),
      type(user_defined_fuc),
      user_defined_fuc)


obj = MyClass(user_defined_fuc)
print(obj.x.__func__ is user_defined_fuc)
print(obj.y is user_defined_fuc)

print(obj.x)
print(obj.method)

print(obj.method.__self__)
print(obj.method.__class__)
print(obj.method.__name__)
print(obj.method.__module__)

print(obj.method.__func__)
print(obj.method.__func__.__name__)

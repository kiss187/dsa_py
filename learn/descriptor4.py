#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import inspect
import functools
import time


# object.__get__(self, instance, owner)：return value
# object.__set__(self, instance, value)：return None
# object.__delete__(self, instance)： return None

class CachedProperty(object):
  """
  A property that is only computed once per instance and then replaces
  itself with an ordinary attribute. Deleting the attribute resets the
  property.
  """

  def __init__(self, func):
    functools.update_wrapper(self, func)
    self.func = func

  def __get__(self, obj, cls):
    if obj:
      value = obj.__dict__[self.func.__name__] = self.func(obj)
      return value
    else:
      return self


class TestClz(object):
  @CachedProperty
  def complex_calc(self):
    print('very complex_calc')
    return sum(range(100))


if __name__ == '__main__':
  t = TestClz()
  print(t.__dict__)
  print('>>> first call')
  print(t.complex_calc)
  print('>>> second call')
  print(t.complex_calc)

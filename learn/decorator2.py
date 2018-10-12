#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from inspect import getmembers, getfullargspec, ismethod
from functools import wraps


def wraps_decorator(f):
  @wraps(f)
  def wraps_wrapper(*args, **kwargs):
    return f(*args, **kwargs)

  return wraps_wrapper


class SomeClass(object):
  @wraps_decorator
  def method(self, x, y, z: str = ""):
    pass


if __name__ == '__main__':
  obj = SomeClass()
  for name, func in getmembers(obj, predicate=ismethod):
    print('Member Name: {}'.format(name))
    print('Func Name: {}'.format(func.__name__))
    print('Args: {}'.format(getfullargspec(func)))

# Member Name: method
# Func Name: method
# Args: FullArgSpec(args=[], varargs='args', varkw='kwargs', defaults=None, kwonlyargs=[], kwonlydefaults=None, annotations={})

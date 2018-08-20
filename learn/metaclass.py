#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://blog.ionelmc.ro/2015/02/09/understanding-python-metaclasses/


# the metaclass will automatically get passed the same argument
# that you usually pass to `type`
def upper_attr(future_class_name, future_class_parents, future_class_attr):
  """
    Return a class object, with the list of its attribute turned
    into uppercase.
  """

  # pick up any attribute that doesn't start with '__' and uppercase it
  print('in upper_attr')
  uppercase_attr = {}
  for name, val in future_class_attr.items():
    if not name.startswith('__'):
      uppercase_attr[name.upper()] = val
    else:
      uppercase_attr[name] = val

  # let `type` do the class creation
  return type(future_class_name, future_class_parents, uppercase_attr)


# __metaclass__ = upper_attr won't work


class FooMom(metaclass=upper_attr):
  # __metaclass__ = upper_attr won't work
  bar = 'bip'


class Foo(FooMom):
  bar_2 = 'bip2'


print(hasattr(Foo, 'bar'))
# Out: False
print(hasattr(Foo, 'BAR'))
# Out: True

print(hasattr(Foo, 'bar_2'))
# Out: True
print(hasattr(Foo, 'BAR_2'))
# Out: False

f = Foo()
try:
  print(f.BAR)
  # out bip
except AttributeError:
  print("'Foo' object has no attribute 'BAR'")

try:
  print(f.bar)
except AttributeError:
  print("'Foo' object has no attribute 'bar'")

try:
  print(f.BAR_2)
except AttributeError:
  print("'Foo' object has no attribute 'BAR_2'")

try:
  print(f.bar_2)
  # out bip2
except AttributeError:
  print("'Foo' object has no attribute 'bar_2'")

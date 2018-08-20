#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = 0


class D(object):
  def f(self, x):
    return x
# >>> d = D()
# >>> D.__dict__['f']  # Stored internally as a function
# <function f at 0x00C45070>
# >>> D.f              # Get from a class becomes an unbound method
# <unbound method D.f>
# >>> d.f              # Get from an instance becomes a bound method
# <bound method D.f of <__main__.D object at 0x00B18C90>>


def print_separate(*args, **kwargs):
  global n
  n += 1
  print('###{}###'.format(n))
  print(*args, **kwargs)
  print('\n')


class Des(object):
  def __init__(self, init_value):
    self.value = init_value

  def __get__(self, instance, typ):
    print('call __get__', instance, typ)
    return self.value

  def __set__(self, instance, value):
    print('call __set__', instance, value)
    self.value = value

  def __delete__(self, instance):
    print('call __delete__', instance)


class Widget(object):
  t = Des(1)


def main():
  w = Widget()

  print_separate(w.__dict__)

  print_separate(type(w.t))

  w.t = 1
  print_separate(w.t)

  print_separate(Widget.t)

  del w.t
  print()

  print_separate(w.t)

  print_separate(Widget.t)


if __name__ == '__main__':
  """
  obj = Clz(), 那么obj.attr 顺序如下：
  （1）如果“attr”是出现在Clz或其基类的__dict__中， 且attr是data descriptor， 那么调用其__get__方法, 否则

  （2）如果“attr”出现在obj的__dict__中， 那么直接返回 obj.__dict__['attr']， 否则

  （3）如果“attr”出现在Clz或其基类的__dict__中

    （3.1）如果attr是non-data descriptor，那么调用其__get__方法， 否则

    （3.2）返回 __dict__['attr']

  （4）如果Clz有__getattr__方法，调用__getattr__方法，否则

  （5）抛出AttributeError
  """
  main()

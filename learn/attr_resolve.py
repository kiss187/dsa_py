#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Foo(object):
  x = 'a'

  def __init__(self):
    self.m = 'm'


f1 = Foo()
f2 = Foo()

print(Foo.x, f1.x, f2.x)
print(id(Foo.x), id(f1.x), id(f2.x))
print(Foo.__dict__, f1.__dict__, f2.__dict__)

Foo.x = 'b'
print('\nafter changed x value in Foo:')
print(Foo.x, f1.x, f2.x)
print(id(Foo.x), id(f1.x), id(f2.x))
print(Foo.__dict__, f1.__dict__, f2.__dict__)

f2.x = 'c'
print('\nafter changed x value in f2:')
print(Foo.x, f1.x, f2.x)
print(id(Foo.x), id(f1.x), id(f2.x))
print(Foo.__dict__, f1.__dict__, f2.__dict__)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import wraps
import cProfile, pstats
import io


def memo(fn):
  cache = {}
  miss = object()

  @wraps(fn)
  def wrapper(*args):
    result = cache.get(args, miss)
    if result is miss:
      result = fn(*args)
      cache[args] = result
    return result

  return wrapper


class MemoC:
  cache = dict()
  miss = object()

  def __init__(self, fn):
    self.fn = fn

  def __call__(self, *args, **kwargs):
    result = self.cache.get(args, self.miss)
    if result is self.miss:
      result = self.fn(*args)
      self.cache[args] = result
    return result


@memo
def fib(n):
  if n < 2:
    return n
  return fib(n - 1) + fib(n - 2)


@MemoC
def fib_c(n):
  if n < 2:
    return n
  return fib_c(n - 1) + fib_c(n - 2)


def profiler(func):
  def wrapper(*args, **kwargs):
    datafn = func.__name__ + ".profile"  # Name the data file
    prof = cProfile.Profile()
    retval = prof.runcall(func, *args, **kwargs)
    # prof.dump_stats(datafn)
    s = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(prof, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())
    return retval

  return wrapper


class MyApp:
  def __init__(self):
    self.func_map = {}

  def register(self, name):
    def func_wrapper(func):
      self.func_map[name] = func
      return func

    return func_wrapper

  def call_method(self, name=None):
    func = self.func_map.get(name, None)
    if func is None:
      raise Exception("No function registered against - " + str(name))
    return func()


def test_myapp():
  app = MyApp()

  @app.register('/')
  def main_page_func():
    return "This is the main page."

  @app.register('/next_page')
  def next_page_func():
    return "This is the next page."

  print(app.call_method('/'))
  print(app.call_method('/next_page'))

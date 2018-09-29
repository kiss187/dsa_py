#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from functools import wraps


def perf_time(f):

  @wraps(f)
  def wrapper(*args, **kwargs):
    start = time.time()
    res = f(*args, **kwargs)
    print('--{} cost {} seconds!--'.format(f.__name__, time.time() - start))
    return res

  return wrapper()

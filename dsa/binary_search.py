#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def std_binary(nums, target):
  """
  :param nums: sorted list with ascending order
  :param target:
  :return: find first element equals with target.
  """
  lo = -1
  hi = len(nums)

  while lo + 1 != hi:
    # mid has a left bias
    mid = lo + ((hi - lo) >> 1)
    if nums[mid] < target:
      lo = mid
    else:
      hi = mid
  if hi == len(nums) or nums[hi] != target:
    return -1
  return hi

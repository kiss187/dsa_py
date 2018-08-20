#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class S100:
  def s1_two_sum(self, nums, target):
    """
    Given an array of integers, return indices of the two numbers
    such that they add up to a specific target.

    You may assume that each input would have exactly one solution,
    and you may not use the same element twice.

    Example:
    Given nums = [2, 7, 11, 15], target = 9,
    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].

    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    tmp = dict()
    for idx, num in enumerate(nums):
      if num in tmp:
        return [tmp[num], idx]
      else:
        need = target - num
        tmp[need] = idx
    raise ValueError('cannot find solution!')

  def s4_find_median_sorted_arrays(self, nums1, nums2):
    """
    There are two sorted arrays nums1 and nums2 of size m and n respectively.
    Find the median of the two sorted arrays.
    The overall run time complexity should be O(log (m+n)).
    You may assume nums1 and nums2 cannot be both empty.

    :param nums1:
    :param nums2:
    :return:
    """
    # todo
    pass

  def s20_is_valid(self, s):
    """
    Given a string containing just the characters
    '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.
    An input string is valid if:
    1.Open brackets must be closed by the same type of brackets.
    2.Open brackets must be closed in the correct order.
    Note that an empty string is also considered valid.
    :type s: str
    :rtype: bool
    """
    stack = list()
    for c in s:
      if c in {'(', '{', '['}:
        stack.append(c)
        continue
      try:
        if c == ')':
          if stack.pop() != '(':
            return False
        elif c == '}':
          if stack.pop() != '{':
            return False
        elif c == ']':
          if stack.pop() != '[':
            return False
        else:
          raise RuntimeError('invalid input string.')
      except (IndexError, RuntimeError) as e:
        return False

    if stack:
      return False
    else:
      return True

  def s26_remove_duplicates(self, nums):
    if not nums:
      return 0
    pos = 0
    for idx in range(len(nums)):
      if nums[pos] != nums[idx]:
        pos = pos + 1
        nums[pos] = nums[idx]
    return pos + 1

  def s27_remove_element(self, nums, val):
    pos = 0
    for n in nums:
      if n != val:
        nums[pos] = n
        pos += 1
    return pos


if __name__ == '__main__':
  solution = S100()
  res = solution.s27_remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2)
  print(res)

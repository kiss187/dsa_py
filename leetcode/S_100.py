#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from leetcode import perf_time


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

  @perf_time
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
    m = len(nums1)
    n = len(nums2)
    s = m + n

    if m > n:
      nums1, nums2, m, n = nums2, nums1, n, m

    i_min, i_max = 0, m

    while True:
      # i's domain is [0, m], m could be zero
      # i means the num of elements,
      # which locate the left side of final median but belong to nums1
      # j as like i is
      # what ever s is even or odd,
      # s // 2 is the num of total elements locate the left side of final median
      i = (i_min + i_max) // 2
      j = s // 2 - i

      if i > 0 and nums1[i - 1] > nums2[j]:
        # if m <= n, i > 0
        # then j = (m+n)//2 - i < (m+n)//2 <= (n + n)//2 == n
        # so j < n
        i_max = i - 1
      elif i < m and nums2[j - 1] > nums1[i]:
        # if m <= n, i < m then
        # j = (m+n)//2 - i > (m+n)//2 - m >= (m + m)//2 - m >= 0
        # so j > 0
        i_min = i + 1
      else:
        # now, i is determined
        # find max left-side element and min right-side element
        if i == m:
          min_right = nums2[j]
        elif j == n:
          min_right = nums1[i]
        else:
          min_right = min(nums1[i], nums2[j])

        if s % 2 == 1:
          return min_right / 1.0

        if i == 0:
          max_left = nums2[j - 1]
        elif j == 0:
          max_left = nums1[i - 1]
        else:
          max_left = max(nums1[i - 1], nums2[j - 1])

        return (max_left + min_right) / 2.0

  @perf_time
  def s11_max_area(self, height):
    """
    greed and pruning
      1 8 6 2 5 7
    1 x ------- o
    8 x x
    6 x x x
    2 x x x x
    5 x x x x x
    7 x x x x x x

    For detailed illustration see
    'https://leetcode.com/problems/container-with-most-water/discuss/6099
    /yet-another-way-to-see-what-happens-in-the-on-algorithm'
    :param height:
    :return:
    """
    left = 0
    right = len(height) - 1
    max_area = 0
    while left < right:
      max_area = max(
        max_area,
        (right - left) * min(height[left], height[right])
      )
      if height[left] > height[right]:
        right = right - 1
      else:
        left = left + 1

    return max_area

  @perf_time
  def s15_three_sum(self, nums):
    """

    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if len(nums) < 3:
      return []
    nums.sort()
    result = set()
    for i, v in enumerate(nums[:-2]):
      if i >= 1 and v == nums[i - 1]:
        continue
      d = {}
      for x in nums[i + 1:]:
        if x not in d:
          d[-v - x] = 1
        else:
          result.add((v, -v - x, x))
    return list(map(list, result))

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
  res = solution.s15_three_sum(
    [-1, 0, 1, 2, -1, -4]
  )
  print(res)

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
  def s15_three_sum_i(self, nums):
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

  @perf_time
  def s15_three_sum_ii(self, nums):
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
      # 类杨氏矩阵线性搜索
      m = i + 1
      n = len(nums) - 1
      while m < n:
        two_sum = nums[m] + nums[n]
        if two_sum == -v:
          result.add((v, nums[m], nums[n]))
          while m + 1 < n and nums[m] == nums[m + 1]:
            m += 1
          while n - 1 > m and nums[n] == nums[n - 1]:
            n -= 1
          m += 1
          n -= 1
        elif two_sum > -v:
          n -= 1
        elif two_sum < -v:
          m += 1
    return list(map(list, result))

  @perf_time
  def s16_three_sum_closest(self, nums, target):
    tmp_three_sum = sum(nums[:3])
    if len(nums) <= 3:
      return tmp_three_sum
    nums.sort()
    for i, v in enumerate(nums[:-2]):
      if i >= 1 and v == nums[i - 1]:
        continue
      # 类杨氏矩阵线性搜索
      m = i + 1
      n = len(nums) - 1
      while m < n:
        three_sum = nums[m] + nums[n] + v
        if three_sum == target:
          return target
        elif three_sum > target:
          n -= 1
        elif three_sum < target:
          m += 1
        if abs(three_sum - target) < abs(tmp_three_sum - target):
          tmp_three_sum = three_sum
    return tmp_three_sum

  @perf_time
  def s18_four_sum(self, nums, target):
    if len(nums) < 4:
      return []
    nums.sort()
    result = set()
    for i in range(len(nums) - 3):
      if i >= 1 and nums[i] == nums[i - 1]:
        continue
      for j in range(i + 1, len(nums) - 2):
        if j >= i + 2 and nums[j] == nums[j - 1]:
          continue
        m = j + 1
        n = len(nums) - 1
        while m < n:
          four_sum = nums[i] + nums[j] + nums[m] + nums[n]
          if four_sum == target:
            result.add((nums[i], nums[j], nums[m], nums[n]))
            while m + 1 < n and nums[m] == nums[m + 1]:
              m += 1
            while n - 1 > m and nums[n] == nums[n - 1]:
              n -= 1
            m += 1
            n -= 1
          elif four_sum > target:
            n -= 1
          elif four_sum < target:
            m += 1

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

  @perf_time
  def s31_next_permutation(self, nums):
    def reverse(num_list, start, end):
      size = len(num_list)
      while (start % size) < (end % size):
        num_list[start], num_list[end] = num_list[end], num_list[start]
        start += 1
        end -= 1

    if len(nums) < 2:
      return

    # from right to left,
    # find first element is lower than its right element
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
      i = i - 1

    if i < 0:
      nums.sort()
      return

    # from right to left,
    # find first element is greater than nums[i]
    j = len(nums) - 1
    while nums[j] <= nums[i]:
      j = j - 1

    nums[i], nums[j] = nums[j], nums[i]
    # sorted will be faster
    # nums[i + 1:] = sorted(nums[i + 1:])
    reverse(nums, i + 1, -1)

  @perf_time
  def s33_search(self, nums, target):
    if not nums:
      return -1
    lo = 0
    hi = len(nums) - 1

    while lo <= hi:
      mid = (lo + hi) // 2
      if nums[mid] == target:
        return mid
      if nums[lo] <= nums[mid]:
        # lo -- mid asc
        # mid -- hi, asc, desc, asc
        if nums[lo] <= target <= nums[mid]:
          hi = mid - 1
        else:
          lo = mid + 1
      else:
        # mid -- hi, ascend
        # lo -- mid, asc, desc, asc
        if nums[mid] <= target <= nums[hi]:
          lo = mid + 1
        else:
          hi = mid - 1
    return -1

  @perf_time
  def s34_search_range(self, nums, target):
    if not nums:
      return [-1, -1]
    lo = 0
    hi = len(nums) - 1
    while lo < hi:
      left = (lo + hi) // 2
      if nums[left] < target:
        lo = left + 1
      else:
        hi = left
    if nums[lo] != target:
      return [-1, -1]
    left = lo

    hi = len(nums) - 1
    while lo < hi:
      right = (lo + hi) // 2 + 1
      if nums[right] > target:
        hi = right - 1
      else:
        lo = right
    return [left, hi]



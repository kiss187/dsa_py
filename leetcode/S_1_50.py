#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from leetcode import perf_time


class Solution:
  @perf_time
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
  def s7_reverse(self, x):
    # using str library
    # res = sign * int(str(sign * x)[::-1])
    # return res if -2147483648 <= res <= 2147483647 else 0
    sign = -1 if x < 0 else 1
    res = 0
    x_abs = abs(x)
    while x_abs != 0:
      res = res * 10 + (x_abs % 10) * sign
      x_abs = x_abs // 10

    return res if -2147483648 <= res <= 2147483647 else 0

  @perf_time
  def s9_is_palindrome(self, x):
    if x < 0:
      return False

    res = 0
    x_abs = abs(x)
    while x_abs != 0:
      res = res * 10 + (x_abs % 10)
      x_abs = x_abs // 10

    if x == res:
      return True
    else:
      return False

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
  def s13_roman_to_int(self, s):
    r_to_i = {
      'I': 1,
      'V': 5,
      'X': 10,
      'L': 50,
      'C': 100,
      'D': 500,
      'M': 1000
    }
    res = 0
    last_base = 0
    idx = len(s) - 1
    while idx >= 0:
      if r_to_i[s[idx]] >= last_base:
        res += r_to_i[s[idx]]
        last_base = r_to_i[s[idx]]
        idx -= 1
      else:
        anchor = s[idx]
        while idx >= 0 and s[idx] == anchor:
          res -= r_to_i[anchor]
          idx -= 1
        last_base = r_to_i[anchor]
    return res

  @perf_time
  def s14_longest_common_prefix(self, strs):

    if not strs:
      return ''
    # simple method
    # common_prefix = strs[0]
    # for s in strs[1:]:
    #   prefix = ''
    #   i = 0
    #   while i < len(s) and i < len(common_prefix) and s[i] == common_prefix[i]:
    #     prefix += common_prefix[i]
    #     i += 1
    #   if prefix:
    #     common_prefix = prefix
    #   else:
    #     return ''
    # return common_prefix

    # using sort
    strs.sort()
    common_prefix = list()
    i = 0
    while i < len(strs[0]) \
        and i < len(strs[-1]) \
        and strs[0][i] == strs[-1][i]:
      common_prefix.append(strs[0][i])
      i += 1
    return ''.join(common_prefix)

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

  @perf_time
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

  @perf_time
  def s21_merge_two_lists(self, l1, l2):
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    if None in (l1, l2):
      return l1 or l2

    if l1.val <= l2.val:
      head = tail = l1
      l1 = l1.next
    else:
      head = tail = l2
      l2 = l2.next

    while l1:
      if l2 and l2.val <= l1.val:
        tail.next = l2
        tail = l2
        l2 = l2.next
      else:
        tail.next = l1
        tail = l1
        l1 = l1.next

    if l2:
      tail.next = l2
    else:
      tail.next = None

    return head

  @perf_time
  def s26_remove_duplicates(self, nums):
    if not nums:
      return 0
    pos = 0
    for idx in range(len(nums)):
      if nums[pos] != nums[idx]:
        pos = pos + 1
        nums[pos] = nums[idx]
    return pos + 1

  @perf_time
  def s27_remove_element(self, nums, val):
    pos = 0
    for n in nums:
      if n != val:
        nums[pos] = n
        pos += 1
    return pos

  @perf_time
  def s28_strstr(self, haystack, needle):
    """
    :tags: KMP String Match
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    #todo kmp solution
    if not needle:
      return 0
    length = len(needle)
    if length > len(haystack):
      return -1
    for i, s in enumerate(haystack):
      if s == needle[0] and haystack[i:i + length] == needle:
        return i
    return -1

  @perf_time
  def s29_divide(self, dividend, divisor):
    if dividend == -2147483648 and divisor == -1:
      # overflow case
      return 2147483647

    is_negative = (dividend < 0) ^ (divisor < 0)
    dividend_abs = abs(dividend)
    divisor_abs = abs(divisor)
    if not dividend_abs or dividend_abs < divisor_abs:
      return 0

    res = 0
    while dividend_abs >= divisor_abs:
      curr_divisor = divisor_abs
      multiplier = 1
      while dividend_abs >= curr_divisor << 1:
        curr_divisor <<= 1
        multiplier <<= 1
      res += multiplier
      dividend_abs -= curr_divisor

    if is_negative:
      res = ~res + 1
    return res

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
    """
    :tags: Binary Search
    :param nums:
    :param target:
    :return:
    """
    lo = -1
    hi = len(nums)

    while lo + 1 != hi:
      mid = lo + (hi - lo) // 2
      if nums[mid] == target:
        return mid
      if nums[lo + 1] <= nums[mid]:
        # lo -- mid asc
        # mid -- hi, asc, desc, asc
        if nums[lo + 1] <= target <= nums[mid]:
          hi = mid
        else:
          lo = mid
      else:
        # mid -- hi, ascend
        # lo -- mid, asc, desc, asc
        if nums[mid] <= target <= nums[hi - 1]:
          lo = mid
        else:
          hi = mid
    return -1

  @perf_time
  def s34_search_range(self, nums, target):
    """
    :tags: Binary Search
    :param nums:
    :param target:
    :return:
    """
    lo = -1
    hi = len(nums)
    while lo + 1 != hi:
      mid = lo + (hi - lo) // 2
      if nums[mid] < target:
        lo = mid
      else:
        hi = mid

    if hi == len(nums) or nums[hi] != target:
      return [-1, -1]
    left = hi

    lo = hi - 1
    hi = len(nums)
    while lo + 1 != hi:
      mid = lo + (hi - lo) // 2
      if nums[mid] <= target:
        lo = mid
      else:
        hi = mid

    return [left, lo]

  @perf_time
  def s35_search_insert(self, nums, target):
    """
    :tags: Binary Search
    :param nums:
    :param target:
    :return:
    """
    lo = -1
    hi = len(nums)

    while lo + 1 != hi:
      mid = lo + (hi - lo) // 2
      if nums[mid] < target:
        lo = mid
      else:
        hi = mid
    return hi

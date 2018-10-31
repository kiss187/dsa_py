#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def kmp_pmt(s, p):
  """
  Knuth–Morris–Pratt algorithm solution
  partial matching table implementation
  :type s: str
  :type p: str
  :rtype: int
  """
  def gen_pmt(pattern):
    """
    generate the partial matching table
    pmt[j] = k could be defined as
    means pattern[0:k] is the longest prefix
    which is also proper suffix for substring pattern[0:j]
    :param pattern: cannot be None or Empty string
    :return: list
    """
    pmt = list()
    k = -1
    j = 0
    pmt.append(k)
    while j < len(pattern) - 1:
      if k == -1 or pattern[j] == pattern[k]:
        j += 1
        k += 1
        pmt.append(k)
      else:
        k = pmt[k]
    return pmt

  if not p or len(p) > len(s):
    return -1

  i = 0
  j = 0
  pmt = gen_pmt(p)
  while i < len(s) and j < len(p):
    if j == -1 or s[i] == p[j]:
      i += 1
      j += 1
    else:
      j = pmt[j]
  if j == len(p):
    return i - j
  else:
    return -1


def kmp_dfa(s, p):
  """
  Knuth–Morris–Pratt algorithm solution
  deterministic finite automata implementation
  :type s: str
  :type p: str
  :rtype: int
  """
  pass


def bm(s, p):
  """
  Boyer-Moore algorithm solution
  :type s: str
  :type p: str
  :rtype: int
  """
  pass


def sunday(s, p):
  """
  Sunday algorithm solution
  :type s: str
  :type p: str
  :rtype: int
  """
  pass


if __name__ == '__main__':
  # [-1, 0, 0, 0, 1, 2, 0]
  print(
    kmp_pmt(
      '123123123123123', 'ABCDABD'
    )
  )

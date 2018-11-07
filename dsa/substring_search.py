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
    prefix != pattern[0:j]
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
        # simple update
        # pmt.append(k)

        # refine update
        if pattern[j] != pattern[k]:
          pmt.append(k)
        else:
          pmt.append(pmt[k])
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

  def gen_dfa(pattern):
    R = 256
    dfa = [[0]*len(pattern) for _ in range(R)]
    i = 0
    # s[0], s[1], ..., s[i-1], s[i]
    # 1. if s[i] match p[i], dfa[s[i]][i] = i + 1
    # 2. if s[i] mismatch p[i],
    # next state equals the state of dfa has matched substring s[1],...,s[i]
    state_bk = 0
    while i < len(pattern):
      m = ord(pattern[i])
      for c in range(R):
        dfa[c][i] = dfa[c][state_bk]
      state_bk = dfa[m][state_bk]
      dfa[m][i] = i + 1
      i += 1

    return dfa

  if not p or len(p) > len(s):
    return -1

  dfa = gen_dfa(p)

  i = 0
  state = 0
  while i < len(s) and state < len(p):
    state = dfa[ord(s[i])][state]
    i += 1

  if state == len(p):
    return i - state
  else:
    return -1


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


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import gc
import ctypes


# We are using ctypes to access our unreachable objects by memory address.
class PyObject(ctypes.Structure):
  _fields_ = [("refcnt", ctypes.c_long)]


gc.disable()  # Disable generational gc

lst = []
lst.append(lst)

# Store address of the list
lst_address = id(lst)
print(PyObject.from_address(lst_address).refcnt)
# Destroy the lst reference
del lst

object_1 = dict()
object_2 = dict()
object_1['obj2'] = object_2
object_2['obj1'] = object_1

obj_address = id(object_1)

print(PyObject.from_address(obj_address).refcnt)
# Destroy references
del object_1, object_2

# Uncomment if you want to manually run garbage collection process
# gc.collect()

# Check the reference count
print(PyObject.from_address(obj_address).refcnt)
print(PyObject.from_address(lst_address).refcnt)

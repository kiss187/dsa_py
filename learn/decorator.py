#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def make_html_tag(tag, css_class):
  def real_decorator(fn):
    css_class_html = " class='{0}'".format(css_class if css_class else "")

    def wrapped(*args, **kwargs):
      return "<" + tag + css_class_html + ">" + \
             fn(*args, **kwargs) + "</" + tag + ">"

    return wrapped

  return real_decorator


class MakeHtmlTag:

  def __init__(self, tag, css_class):
    self.tag = tag
    self.css_class_html = " class='{0}'".format(css_class if css_class else "")

  def __call__(self, fn):
    def wrapped(*args, **kwargs):
      return "<" + self.tag + self.css_class_html + ">" + \
             fn(*args, **kwargs) + "</" + self.tag + ">"
    return wrapped


@make_html_tag(tag="b", css_class="bold_css")
@make_html_tag(tag="i", css_class="italic_css")
def hello():
  return "hello world"


@MakeHtmlTag(tag='2', css_class='2_css')
@MakeHtmlTag(tag='1', css_class='1_css')
def hello_c():
  return "hello world - class"


def fuck(fn):
  def wrapper(*args, **kwargs):
    print("fuck {}!".format(fn.__name__[::-1].upper()))
    fn(*args, **kwargs)
  return wrapper


class FuckC:

  def __init__(self, fn):
    self.fn = fn

  def __call__(self, *args, **kwargs):
    print("fuck {}!".format(self.fn.__name__[::-1].upper()))


@fuck
def wfg():
  print('in wfg')


@FuckC
def wfg_c():
  pass


wfg()
wfg_c()

print(hello())
print(hello_c())

# print: <b class='bold_css'><i class='italic_css'>hello world</i></b>

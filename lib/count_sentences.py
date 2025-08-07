#!/usr/bin/env python3

class MyString:
  def __init__(self, value=""):
    self.value = value

  @property
  def value(self):
    return self._value

  @value.setter
  def value(self, value):
    if isinstance(value, str):
      self._value = value
    else:
      print('The value must be a string.')

  def is_sentence(self):
    if self._value.endswith(('.', '?', '!')):
      return True
    else:
      return False

  def is_question(self):
    if self._value.endswith('?'):
      return True
    else:
      return False

  def is_exclamation(self):
    if self._value.endswith('!'):
      return True
    else:
      return False

  def count_sentences(self):
    count = 0
    words = self._value.split(" ") #split words
    for word in words:
      if word.endswith('.') or word.endswith('?') or word.endswith('!'):
        count += 1
      
    return count
  
  

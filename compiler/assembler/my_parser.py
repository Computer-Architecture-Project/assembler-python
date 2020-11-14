from abstract_syntax_tree import (
  Label,
  Register,
  Offset,
  Unary,
  Number,
  RType,
  IType,
  JType,
  OType,
  FillType,
  Method,
  Initial,
  ParsedTree
)

class Parser(object):
  def __init__(self, lexer):
    for _ in range(100):
      print(lexer.get_next_token())
    pass

  def parse(self):
    pass


from lis import Define, Plus, Variable, Const
from lis import tokenize, parse_tokens

def test_tokenize():
    source = ['(define a 3)']
    tokens = list(tokenize(source))
    assert tokens == ['(', 'define', 'a', '3', ')']


def test_parse_1():
    source = ['(define a 3)']
    tokens = list(tokenize(source))
    exp, index = parse_tokens(tokens, 0)
    assert exp == Define(Variable('a'), Const('3'))

def test_parse_2():
    source = ['(define a (+ 3 3))']
    tokens = list(tokenize(source))
    exp, index = parse_tokens(tokens, 0)
    assert exp == Define(Variable('a'), Plus(Const('3'), Const('3')))

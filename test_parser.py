
from lis import Define, Plus, Variable, Const, Lambda
from lis import tokenize, parse_tokens

def test_tokenize():
    source = ['(define a 3)']
    tokens = list(tokenize(source))
    assert tokens == ['(', 'define', 'a', '3', ')']


def test_parse_Define():
    source = ['(define a 3)']
    tokens = list(tokenize(source))
    exp, index = parse_tokens(tokens, 0)
    assert exp == Define(Variable('a'), Const('3'))


def test_parse_Plus():
    source = ['(define a (+ 3 3))']
    tokens = list(tokenize(source))
    exp, index = parse_tokens(tokens, 0)
    assert exp == Define(Variable('a'), Plus(Const('3'), Const('3')))


def test_parse_Lambda():
    source = ['(lambda (x y) (+ x y))']
    tokens = list(tokenize(source))
    exp, index = parse_tokens(tokens, 0)
    assert exp == Lambda(['x', 'y'], Plus(Variable('x'), Variable('y')))


def test_parse_Define_Lambda():
    source = ['(define add (lambda (x y) (+ x y))']
    tokens = list(tokenize(source))
    exp, index = parse_tokens(tokens, 0)
    assert exp == Define(Variable('a'),
                         Lambda(['x', 'y'],
                                Plus(Variable('x'), Variable('y'))))

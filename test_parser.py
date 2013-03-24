
#from lis import Define, Plus, Variable, Const, Lambda
from lis import tokenize, parse_tokens

def test_tokenize():
    source = ['(define a 3)']
    tokens = list(tokenize(source))
    assert tokens == ['(', 'define', 'a', '3', ')']


def test_tokenize2():
    source = ['(+ 10 25 0)']
    tokens = list(tokenize(source))
    assert tokens == ['(', '+', '10', '25', '0', ')']

# get_list()

def test_parse_Define():
    source = ['(define a 3)']
    tokens = list(tokenize(source))
    exp = parse_tokens(tokens)
    assert exp == ['define', 'a', 3]


def test_parse_Plus():
    source = ['(define a (+ 3 3))']
    tokens = list(tokenize(source))
    exp = parse_tokens(tokens)
    assert exp == ['define', 'a', ['+', 3, 3]]


def test_parse_Lambda():
    source = ['(lambda (x y) (+ x y))']
    tokens = list(tokenize(source))
    exp = parse_tokens(tokens)
    assert exp == ['lambda', ['x', 'y'], ['+', 'x', 'y']]


def test_parse_Define_Lambda():
    source = ['(define add (lambda (x y) (+ x y)))']
    tokens = list(tokenize(source))
    exp = parse_tokens(tokens)
    assert exp == ['define', 'add', ['lambda', ['x', 'y'], ['+', 'x', 'y']]]


from lis import tokenize, parse_tokens, eval_in_env

def test_add():
    source = ['(+ 1 3 5)']
    exp = parse_tokens(list(tokenize(source)))
    assert eval_in_env(exp, []) == 9


def test_multiply():
    source = ['(* 1 3 5)']
    exp = parse_tokens(list(tokenize(source)))
    assert eval_in_env(exp, []) == 15


def test_subtract():
    source = ['(- 10 14)']
    exp = parse_tokens(list(tokenize(source)))
    assert eval_in_env(exp, []) == -4


def test_divide():
    source = ['(/ 10 3)']
    exp = parse_tokens(list(tokenize(source)))
    assert eval_in_env(exp, []) == 3


def test_equals():
    source0, source1 = ['(= 1 2)'], ['(= 2 2)']
    exp0 = parse_tokens(list(tokenize(source0)))
    exp1 = parse_tokens(list(tokenize(source1)))
    assert eval_in_env(exp0, []) == False
    assert eval_in_env(exp1, []) == True


def test_lt():
    source0, source1 = ['(< 2 2)'], ['(< 1 2)']
    exp0 = parse_tokens(list(tokenize(source0)))
    exp1 = parse_tokens(list(tokenize(source1)))
    assert eval_in_env(exp0, []) == False
    assert eval_in_env(exp1, []) == True


def test_gt():
    source0, source1 = ['(> 2 2)'], ['(> 3 2)']
    exp0 = parse_tokens(list(tokenize(source0)))
    exp1 = parse_tokens(list(tokenize(source1)))
    assert eval_in_env(exp0, []) == False
    assert eval_in_env(exp1, []) == True

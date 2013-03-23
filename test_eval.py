
from lis import tokenize, parse_tokens, eval_in_env


def test_eval_Plus_Const():
    exp = ['+', 3, 4]
    res = eval_in_env(exp, [])
    assert res == 7


def test_eval_LT():
    exp = ['<', 2, 3]
    res = eval_in_env(exp, [])
    assert res == True


def test_eval_if():
    exp = ['if', True, 3, 4]
    assert eval_in_env(exp, []) == 3


def test_eval_let():
    exp = ['let', [['x', 3], ['y', 10]], ['+', 'x', 'y']]
    assert eval_in_env(exp, []) == 13


def test_eval_define():
    env = []
    exp = ['define', 'a', 3]
    eval_in_env(exp, env)
    assert env == [('a', 3)]


def test_eval_function():
    env = [('add3', ['closure', ['lambda', ['x'], ['+', 'x', 3]], []])]
    exp = ['add3', 10]
    assert eval_in_env(exp, env) == 13


def test_eval_function_2():
    env = [('ifthen', ['closure', ['lambda', ['x'], ['if', True, 'x', 3]], []])]
    exp = ['ifthen', 10]
    assert eval_in_env(exp, env) == 10


def test_eval_recursion():
    env = [('sumto', ['closure', ['lambda', ['n'],
                                    ['if',  ['<', 'n', 1],
                                            0,
                                            ['+', 'n', ['sumto', ['-', 'n', 1]]]]],
                                 []])]
    exp = ['sumto', 3]
    assert eval_in_env(exp, env) == 6


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

#def test_eval_Variable():
#    env = [('a', Const(10))]
#    exp = Plus(Const(3), Variable('a'))
#    res = eval_in_env(exp, env)
#    assert res == Const(13)


#def test_eval_Closure():
#    env = [('add', Closure(['x', 'y'], Plus(Variable('x'), Variable('y'))))]
#    exp = None

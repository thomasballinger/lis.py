
#from lis import Define, Plus, Variable, Const
from lis import tokenize, parse_tokens #, eval_in_env


#def test_eval_Plus_Const():
#    exp = Plus(Const(3), Const(4))
#    res = eval_in_env(exp, [])
#    assert res == Const(7)
#
#
#def test_eval_Variable():
#    env = [('a', Const(10))]
#    exp = Plus(Const(3), Variable('a'))
#    res = eval_in_env(exp, env)
#    assert res == Const(13)
#
#
#def test_eval_Closure():
#    env = [('add', Closure(['x', 'y'], Plus(Variable('x'), Variable('y'))))]
#    exp = None

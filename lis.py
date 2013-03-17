#! /usr/bin/env python

from collections import namedtuple

# LEXER ================================

def split_word(word):
    current = ''
    for c in word:
        if c == '(' or c == ')':
            if current != '':
                yield current
            yield c
            current = ''
        else:
            current = current + c
    if current != '':
        yield current

def tokenize(lines):
    for line in lines:
        for word in line.split():
            for s in split_word(word):
                yield s


# COMPONENTS ===========================

Define = namedtuple('Define', 'name exp')
Function = namedtuple('Function', 'body')
Plus = namedtuple('Plus', 'exp1 exp2')
Const = namedtuple('Const', 'val')
Variable = namedtuple('Variable', 'name')
Display = namedtuple('Display', 'exp')
Main = namedtuple('Main', 'exp')


# PARSER ===============================

def parse_tokens(tokens, index):
    tok = tokens[index]
    if tok == 'define':
        name, next_index = parse_tokens(tokens, index + 1)
        exp, next_index = parse_tokens(tokens, next_index)
        if tokens[next_index] == ')':
            return Define(name, exp), next_index + 1
        else:
            raise Exception('define has too many arguments')
    elif tok == '+':
        exp1, next_index = parse_tokens(tokens, index + 1)
        exp2, next_index = parse_tokens(tokens, next_index)
        if tokens[next_index] == ')':
            return Plus(exp1, exp2), next_index + 1
        else:
            raise Exception('"+" has too many arguments')
    elif tok == '(':
        return parse_tokens(tokens, index+1)
    elif tok.isdigit():
        return Const(tok), index+1
    elif tok.isalpha():
        return Variable(tok), index+1
    else:
        raise Exception('unrecognized token')


# EVALUATOR ============================

def lookup_in_env(var, env):
    for name, val in env:
        if var == name:
            return val
    raise Exception('unrecognized variable name')


def eval_in_env(exp, env):
    if type(exp) == Const:
        return exp
    elif type(exp) == Plus:
        return Const(eval_in_env(exp.exp1, env).val
                     + eval_in_env(exp.exp2, env).val)
    elif type(exp) == Variable:
        return eval_in_env(lookup_in_env(exp.name, env), env)


# RUN INTERPRETER ======================

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('source', nargs = 1, help='source text file')
    args = parser.parse_args()

    try:
        source = open(args.source[0], 'r')
        for x in tokenize(source):
            print(x)
    except:
        print('Invalid source file')

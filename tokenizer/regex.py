from cmp.utils import Token
from .grammar import G_for_regular_exp
from parser_library.LL1_parser import LL1
from parser_library.algorithm.evaluate import evaluate_parse
from tokenizer.automata_algorithm.nfa_to_dfa import nfa_to_dfa

import pydot

class Regex:
    def __init__(self):
        self.G = G_for_regular_exp
        self.ll1 = LL1(self.G)

    def automaton(self,regular_exp):
        tokens = self.regex_tokenizer(regular_exp)
        left_parse = self.ll1.parser(tokens)
        ast = evaluate_parse(left_parse, tokens)
        nfa = ast.evaluate()
        return nfa_to_dfa(nfa)

    def regex_tokenizer(self,text, skip_whitespaces=False):
        tokens = []
        fixed_tokens = {lex: Token(lex, self.G[lex]) for lex in '| * ( ) ε'.split() }
        for char in text:
            if skip_whitespaces and char.isspace():
                continue
            try:
                tokens.append(fixed_tokens[char])
            except KeyError:
                tokens.append(Token(char,self.G['symbol']))

        tokens.append(Token('$', self.G.EOF))
        return tokens
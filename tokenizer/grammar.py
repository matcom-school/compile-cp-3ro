from cmp.pycompiler import Grammar
from .ast import UnionNode,ClosureNode,ConcatNode,SymbolNode,EpsilonNode

G_for_regular_exp = Grammar()

E = G_for_regular_exp.NonTerminal('E', True)
T, F, A, X, Y, Z = G_for_regular_exp.NonTerminals('T F A X Y Z')
pipe, star, opar, cpar, symbol, epsilon = G_for_regular_exp.Terminals('| * ( ) symbol ε')

E %= T + X,                     lambda h,s:s[2], None, lambda h,s: s[1]

X %= pipe + T + X,              lambda h,s: s[3], None, None, lambda h,s: UnionNode(h[0], s[2])
X %= G_for_regular_exp.Epsilon, lambda h,s: h[0]

T %= F + Y,                     lambda h,s: s[2], None, lambda h,s: s[1]

Y %= F + Y,                     lambda h,s: s[2], None, lambda h,s: ConcatNode(h[0], s[1])
Y %= G_for_regular_exp.Epsilon, lambda h,s: h[0]

F %= A + Z,                     lambda h,s: s[2], None, lambda h,s: s[1]

Z %= star + Z,                  lambda h,s: s[2], None, lambda h,s: ClosureNode(h[0])
Z %= G_for_regular_exp.Epsilon, lambda h,s: h[0]

A %= opar + E + cpar ,          lambda h,s: s[2], None, None, None
A %= symbol,                    lambda h,s: SymbolNode(s[1]), None
A %= epsilon,                   lambda h,s: EpsilonNode(h[0])

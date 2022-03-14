from tokenizer.regex import Regex
from tokenizer.automata_algorithm.nfa_to_dfa import nfa_to_dfa

dfa = nfa_to_dfa( Regex().automaton("a*(a|b)*cd|ε") )
print("a")

assert dfa.recognize('')
assert dfa.recognize('cd')
assert dfa.recognize('aaaaacd')
assert dfa.recognize('bbbbbcd')
assert dfa.recognize('bbabababcd')
assert dfa.recognize('aaabbabababcd')

assert not dfa.recognize('cda')
assert not dfa.recognize('aaaaa')
assert not dfa.recognize('bbbbb')
assert not dfa.recognize('ababba')
assert not dfa.recognize('cdbaba')
assert not dfa.recognize('cababad')
assert not dfa.recognize('bababacc')

from tokenizer.lexer import Lexer

nonzero_digits = '|'.join(str(n) for n in range(1,10))
letters = '|'.join(chr(n) for n in range(ord('a'),ord('z')+1))

lexer = Lexer([
    ('num', f'({nonzero_digits})(0|{nonzero_digits})*'),
    ('for' , 'for'),
    ('foreach' , 'foreach'),
    ('space', ' *'),
    ('id', f'({letters})({letters}|0|{nonzero_digits})*')
], 'eof')

text = '5465 for 45foreach fore'
tokens = lexer(text)
assert [t.token_type for t in tokens] == ['num', 'space', 'for', 'space', 'num', 'foreach', 'space', 'id', 'eof']
assert [t.lex for t in tokens] == ['5465', ' ', 'for', ' ', '45', 'foreach', ' ', 'fore', '$']

text = '4forense forforeach for4foreach foreach 4for'
tokens = lexer(text)
assert [t.token_type for t in tokens] == ['num', 'id', 'space', 'id', 'space', 'id', 'space', 'foreach', 'space', 'num', 'for', 'eof']
assert [t.lex for t in tokens] == ['4', 'forense', ' ', 'forforeach', ' ', 'for4foreach', ' ', 'foreach', ' ', '4', 'for', '$']
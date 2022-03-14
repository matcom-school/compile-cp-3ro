from tokenizer.automata_algorithm.dfa import DFA 
from tokenizer.automata_algorithm.nfa import NFA

automaton = DFA(states=3, finals=[2], transitions={
    (0, 'a'): 0,
    (0, 'b'): 1,
    (1, 'a'): 2,
    (1, 'b'): 1,
    (2, 'a'): 0,
    (2, 'b'): 1,
})

assert automaton.recognize('ba')
assert automaton.recognize('aababbaba')

assert not automaton.recognize('')
assert not automaton.recognize('aabaa')
assert not automaton.recognize('aababb')

##########################################################################################################
from tokenizer.automata_algorithm.nfa_to_dfa import move

automaton = NFA(states=6, finals=[3, 5], transitions={
    (0, ''): [ 1, 2 ],
    (1, ''): [ 3 ],
    (1,'b'): [ 4 ],
    (2,'a'): [ 4 ],
    (3,'c'): [ 3 ],
    (4, ''): [ 5 ],
    (5,'d'): [ 5 ]
})

assert move(automaton, [1], 'a') == set()
assert move(automaton, [2], 'a') == {4}
assert move(automaton, [1, 5], 'd') == {5}

############################################################################################################
from tokenizer.automata_algorithm.nfa_to_dfa import epsilon_closure

automaton = NFA(states=6, finals=[3, 5], transitions={
    (0, ''): [ 1, 2 ],
    (1, ''): [ 3 ],
    (1,'b'): [ 4 ],
    (2,'a'): [ 4 ],
    (3,'c'): [ 3 ],
    (4, ''): [ 5 ],
    (5,'d'): [ 5 ]
})

assert epsilon_closure(automaton, [0]) == {0,1,2,3}
assert epsilon_closure(automaton, [0, 4]) == {0,1,2,3,4,5}
assert epsilon_closure(automaton, [1, 2, 4]) == {1,2,3,4,5}


#############################################################################################################
from tokenizer.automata_algorithm.nfa_to_dfa import nfa_to_dfa
from tokenizer.automata_algorithm.nfa import NFA

automaton = NFA(states=6, finals=[3, 5], transitions={
    (0, ''): [ 1, 2 ],
    (1, ''): [ 3 ],
    (1,'b'): [ 4 ],
    (2,'a'): [ 4 ],
    (3,'c'): [ 3 ],
    (4, ''): [ 5 ],
    (5,'d'): [ 5 ]
})

dfa = nfa_to_dfa(automaton)

assert dfa.states == 4
assert len(dfa.finals) == 4

assert dfa.recognize('')
assert dfa.recognize('a')
assert dfa.recognize('b')
assert dfa.recognize('cccccc')
assert dfa.recognize('adddd')
assert dfa.recognize('bdddd')

assert not dfa.recognize('dddddd')
assert not dfa.recognize('cdddd')
assert not dfa.recognize('aa')
assert not dfa.recognize('ab')
assert not dfa.recognize('ddddc')

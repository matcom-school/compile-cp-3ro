
from tokenizer.automata_algorithm.dfa import DFA
from tokenizer.automata_algorithm.nfa_to_dfa import nfa_to_dfa

automaton = DFA(states=2, finals=[1], transitions={
    (0,'a'):  0,
    (0,'b'):  1,
    (1,'a'):  0,
    (1,'b'):  1,
})

#############################################################################################
from tokenizer.automata_algorithm.union import automata_union
union = automata_union(automaton, automaton)
recognize = nfa_to_dfa(union).recognize

assert union.states == 2 * automaton.states + 2

assert recognize('b')
assert recognize('abbb')
assert recognize('abaaababab')

assert not recognize('')
assert not recognize('a')
assert not recognize('abbbbaa')

##############################################################################################
from tokenizer.automata_algorithm.concatenation import automata_concatenation

concat = automata_concatenation(automaton, automaton)
recognize = nfa_to_dfa(concat).recognize

assert concat.states == 2 * automaton.states + 1

assert recognize('bb')
assert recognize('abbb')
assert recognize('abaaababab')

assert not recognize('')
assert not recognize('a')
assert not recognize('b')
assert not recognize('ab')
assert not recognize('aaaab')
assert not recognize('abbbbaa')

#####################################################################################################
from tokenizer.automata_algorithm.closure import automata_closure

closure = automata_closure(automaton)
recognize = nfa_to_dfa(closure).recognize

assert closure.states == automaton.states + 2

assert recognize('')
assert recognize('b')
assert recognize('ab')
assert recognize('bb')
assert recognize('abbb')
assert recognize('abaaababab')

assert not recognize('a')
assert not recognize('abbbbaa')

################################################################################################
automaton = DFA(states=5, finals=[4], transitions={
    (0,'a'): 1,
    (0,'b'): 2,
    (1,'a'): 1,
    (1,'b'): 3,
    (2,'a'): 1,
    (2,'b'): 2,
    (3,'a'): 1,
    (3,'b'): 4,
    (4,'a'): 1,
    (4,'b'): 2,
})

###################################################################################################
from tokenizer.automata_algorithm.minimization import state_minimization
states = state_minimization(automaton)

for members in states.groups:
    all_in_finals = all(m.value in automaton.finals for m in members)
    none_in_finals = all(m.value not in automaton.finals for m in members)
    assert all_in_finals or none_in_finals
    
assert len(states) == 4
assert states[0].representative == states[2].representative
assert states[1].representative == states[1]
assert states[3].representative == states[3]
assert states[4].representative == states[4]

#####################################################################################################
from tokenizer.automata_algorithm.minimization import automata_minimization
mini = automata_minimization(automaton)

assert mini.states == 4

assert mini.recognize('abb')
assert mini.recognize('ababbaabb')

assert not mini.recognize('')
assert not mini.recognize('ab')
assert not mini.recognize('aaaaa')
assert not mini.recognize('bbbbb')
assert not mini.recognize('abbabababa')
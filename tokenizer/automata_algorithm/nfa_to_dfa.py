from cmp.utils import ContainerSet 
from .dfa import DFA

def move(automaton, states, symbol):
    moves = set()
    for state in states:
        try:
            for item in automaton.transitions[state][symbol]:
                moves.add(item)
        except KeyError:
            pass
    return moves

def epsilon_closure(automaton, states):
    pending = [ s for s in states ] # equivalente a list(states) pero me gusta así :p
    closure = { s for s in states } # equivalente a  set(states) pero me gusta así :p
    
    while pending:
        state = pending.pop()
        try:
            for item in automaton.transitions[state]['']:
                pending.append(item)
                closure.add(item)
        except KeyError:
            pass
                
    return ContainerSet(*closure)

def nfa_to_dfa(automaton):
    transitions = {}
    
    start = epsilon_closure(automaton, [automaton.start])
    start.id = 0
    start.is_final = any(s in automaton.finals for s in start)
    states = [ start ]
    
    pending = [ start ]
    while pending:
        state = pending.pop()
     
        for symbol in automaton.vocabulary:

            e_closure = ContainerSet(*move(automaton,state,symbol))
            e_closure.update(epsilon_closure(automaton,e_closure.set))
                
            if(len(e_closure) == 0):
                continue
                
            try:
                transitions[state.id,symbol] = states[states.index(e_closure)].id
            except ValueError:
                e_closure.id = len(states)
                e_closure.is_final = any(s in automaton.finals for s in e_closure)
                states.append(e_closure)
                pending.append(e_closure)
                transitions[state.id,symbol] = e_closure.id
    
    finals = [ state.id for state in states if state.is_final ]
    dfa = DFA(len(states), finals, transitions)
    return dfa
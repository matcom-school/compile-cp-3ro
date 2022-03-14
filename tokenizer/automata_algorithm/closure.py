from .nfa import NFA

def automata_closure(a1):
    transitions = {}
    
    start = 0
    d1 = 1
    final = a1.states + d1
    
    for (origin, symbol), destinations in a1.map.items():
        transitions[origin + d1 , symbol] = [ nd + d1 for nd in destinations]
        
    transitions[start , ''] = [ d1 , final]
    
    for state in a1.finals:
        transitions[state + d1, ''] = [a1.start + d1 ,final]
    
    states = a1.states +  2
    finals = { final }
    
    return NFA(states, finals, transitions, start)
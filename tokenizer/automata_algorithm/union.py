from .nfa import NFA

def automata_union(a1, a2):
    transitions = {}
    
    start = 0
    d1 = 1
    d2 = a1.states + d1
    final = a2.states + d2
    
    for (origin, symbol), destinations in a1.map.items():
        transitions[origin + d1 , symbol] = [nd + d1 for nd in destinations]

    for (origin, symbol), destinations in a2.map.items():
        transitions[origin + d2 , symbol] = [nd + d2 for nd in destinations]
    
    transitions[start,''] = [d1,d2]
    
    for state in a1.finals:
        transitions[state + d1,''] = [final]
    for state in a2.finals:
        transitions[state + d2,''] = [final]
        
    states = a1.states + a2.states + 2
    finals = { final }
    
    return NFA(states, finals, transitions, start)
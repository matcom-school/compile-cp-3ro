from cmp.utils import DisjointSet
from .dfa import DFA

def distinguish_states(group, automaton, partition):
    split = {}
    vocabulary = tuple(automaton.vocabulary)

    for member in group:
        new_group = []
        for symbol in vocabulary:
            try:
                ikey = partition[automaton.transitions[member.value][symbol][0]].representative
                new_group.append(ikey)
            except KeyError:
                new_group.append(None)
        try:
            split[tuple(new_group)].append(member.value)
        except KeyError:
            split[tuple(new_group)] = [member.value]
            
    return [ group for group in split.values()]

            
def state_minimization(automaton):
    partition = DisjointSet(*range(automaton.states))
    
    not_final = {s for s in range(automaton.states)}
    final = {s for s in automaton.finals}
    not_final.difference_update(final)
    
    partition.merge(not_final)
    partition.merge(final)
    
    while True:
        new_partition = DisjointSet(*range(automaton.states))
            
        for group in partition.groups:
            new_groups = distinguish_states(group,automaton,partition)
            for g in new_groups:
                new_partition.merge(g)

        if len(new_partition) == len(partition):
            break

        partition = new_partition
        
    return partition

def automata_minimization(automaton):
    partition = state_minimization(automaton)
    
    states = [s for s in partition.representatives]
    mapper = { state : int(i) for i,state in enumerate(states) }
    
    transitions = {}
    for i, state in enumerate(states):
        #transitions[i] = {}
        for symbol, destinations in automaton.transitions[state.value].items():
            transitions[i,symbol] = [ mapper[partition[n].representative] for n in destinations ][0]
    
    finals = [ mapper[partition[n].representative] for n in automaton.finals ]
    start  = mapper[partition[automaton.start].representative]
    
    return DFA(len(states), finals, transitions, start)
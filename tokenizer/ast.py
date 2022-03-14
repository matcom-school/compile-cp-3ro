from cmp.ast_abstract_node import AtomicNode,UnaryNode,BinaryNode
from .automata_algorithm.closure import automata_closure
from .automata_algorithm.concatenation import automata_concatenation
from .automata_algorithm.union import automata_union
from .automata_algorithm.nfa import NFA

class EpsilonNode(AtomicNode):
    def evaluate(self):
        return NFA(1,[0],{})

class SymbolNode(AtomicNode):
    def evaluate(self):
        s = self.lex
        return NFA(2,[1],{(0,s):[1]})

class ClosureNode(UnaryNode):
    @staticmethod
    def operate(value):
        return automata_closure(value)

class UnionNode(BinaryNode):
    @staticmethod
    def operate(lvalue, rvalue):
        return automata_union(lvalue,rvalue)
    
class ConcatNode(BinaryNode):
    @staticmethod
    def operate(lvalue, rvalue):
        return automata_concatenation(lvalue,rvalue)
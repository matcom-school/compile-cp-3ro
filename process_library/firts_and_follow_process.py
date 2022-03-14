from process_library.process import Process
from parser_library.algorithm.firts_set import compute_firsts
from parser_library.algorithm.follow_set import compute_follows 

class FAF_Process(Process):
    def __init__(self,G,works):
        Process.__init__(self)
        self.add_get("firsts set", self.firsts)
        self.add_get("follows set", self.follow)
        self.grammar = G

    def firsts(self):
        return compute_firsts(self.grammar)
    def follow(self):
        return compute_follows(self.grammar,self.get("firsts set"))
    
    @staticmethod
    def new_istance(G,works):
        return FAF_Process(G,works)
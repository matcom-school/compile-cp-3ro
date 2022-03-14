from process_library.process import Process
from parser_library.LL1_parser import LL1

class LL1_Process(Process):
    def __init__(self,G,works):
        Process.__init__(self)
        self.parser = LL1(G,works)
        self.add_get("the grammar is ll1", self.parser.grammar_is_ll1)
        self.add_get("parsing table", self.parser.build_parsing_table)
        self.add_get("derivations tree" , self.parser.n_parser)

    @staticmethod
    def new_istance(G,works):
        return LL1_Process(G,works)
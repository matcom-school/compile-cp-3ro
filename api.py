from unit_testing import run
from process_factory import ProcessFactory
from tokenizer.lexer import Lexer
from grammar_compile import InnerGrammar,InnerRegexTable
from parser_library.LL1_parser import LL1
from parser_library.algorithm.evaluate import evaluate_parse

class Api:

    def __init__(self):
        self.process_class = {}
        self.ProcessFactory = ProcessFactory()
        #self.inner_grammar = InnerGrammar()
        #self.ll1 = LL1(self.inner_grammar)
        #self.lexer = Lexer(InnerRegexTable(),self.inner_grammar.EOF)
        self.grammar = None
        self.works = None


    def set_grammar(self,G_str):
      #  assert type(G_str) == type(str()), "api.set_grammar need a string"
      #  tokens = self.lexer(G_str)
      #  tokens = [ token for token in tokens if token.token_type != "space" ]            
      #  left_parser = self.ll1.parser(tokens)
      #  ast = evaluate_parse(left_parser,tokens)
      #  self.grammar = ast.evaluate()
        self.process_class = {}


    def set_works_testing(self,works):
        self.works = works
        self.process_class = {}

    def process(self,process):
        try:
            return self.process_class[process]
        except KeyError:
            self.process_class[process] = self.ProcessFactory(process)(self.grammar,self.works)
            return self.process_class[process]

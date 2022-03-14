from cmp.utils import Token
from cmp.automata import State
from .regex import Regex

class Lexer:
    def __init__(self, table, eof):
        self.eof = eof
        self.regex = Regex()
        self.regexs = self._build_regexs(table)
        self.automaton = self._build_automaton()
        
    
    def _build_regexs(self, table):
        regexs = []
        for n, (token_type, regex) in enumerate(table):
            automaton = State.from_nfa(self.regex.automaton(regex)).to_deterministic()
            for i in automaton:
                if i.final:
                    i.tag = (n, token_type)
            
            regexs.append(automaton)
        return regexs
    
    def _build_automaton(self):
        start = State('start')
        for automaton in self.regexs:
            start.add_epsilon_transition(automaton)
        return start.to_deterministic()
    
        
    def _walk(self, string):
        state = self.automaton
        final = state 
        final_lex = lex = ''
        
        for symbol in string:
            try:
                state = state[symbol][0]
                lex += symbol
                if state.final:
                    final = state
                    final_lex = lex
            except:
                break
        return final_lex, final
    
    def _tokenize(self, text):
        text = text + "$"
        final = None
        
        while len(text) > 0:
            final_lex, final= self._walk(text)
            minPrior = 9999999999999999999999999999999999999999999
            finalfinal = None
            
            for st in final.state:
                if st.final:
                    n, _type = st.tag
                    if  n < minPrior:
                        minPrior = n
                        finalfinal = st
            yield final_lex, finalfinal.tag[1]
            text = text[len(final_lex):]
                    
        yield '$', self.eof
    
    def __call__(self, text):
        return [ Token(lex, ttype) for lex, ttype in self._tokenize(text) ]
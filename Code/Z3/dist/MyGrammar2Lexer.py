# Generated from MyGrammar2.g4 by ANTLR 4.11.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,20,153,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,
        2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,
        10,1,10,1,11,1,11,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,1,16,1,16,5,16,122,8,16,10,16,12,16,125,9,
        16,1,16,1,16,1,16,1,16,1,17,4,17,132,8,17,11,17,12,17,133,1,17,5,
        17,137,8,17,10,17,12,17,140,9,17,1,18,4,18,143,8,18,11,18,12,18,
        144,1,19,4,19,148,8,19,11,19,12,19,149,1,19,1,19,1,123,0,20,1,1,
        3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,
        29,15,31,16,33,17,35,18,37,19,39,20,1,0,4,2,0,65,90,97,122,3,0,48,
        57,65,90,97,122,1,0,48,57,3,0,9,10,13,13,32,32,157,0,1,1,0,0,0,0,
        3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,
        1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,
        1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,
        1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,1,41,1,0,0,0,3,43,
        1,0,0,0,5,55,1,0,0,0,7,58,1,0,0,0,9,62,1,0,0,0,11,64,1,0,0,0,13,
        71,1,0,0,0,15,80,1,0,0,0,17,83,1,0,0,0,19,86,1,0,0,0,21,88,1,0,0,
        0,23,90,1,0,0,0,25,92,1,0,0,0,27,96,1,0,0,0,29,99,1,0,0,0,31,109,
        1,0,0,0,33,119,1,0,0,0,35,131,1,0,0,0,37,142,1,0,0,0,39,147,1,0,
        0,0,41,42,5,40,0,0,42,2,1,0,0,0,43,44,5,100,0,0,44,45,5,101,0,0,
        45,46,5,99,0,0,46,47,5,108,0,0,47,48,5,97,0,0,48,49,5,114,0,0,49,
        50,5,101,0,0,50,51,5,45,0,0,51,52,5,102,0,0,52,53,5,117,0,0,53,54,
        5,110,0,0,54,4,1,0,0,0,55,56,5,40,0,0,56,57,5,41,0,0,57,6,1,0,0,
        0,58,59,5,73,0,0,59,60,5,110,0,0,60,61,5,116,0,0,61,8,1,0,0,0,62,
        63,5,41,0,0,63,10,1,0,0,0,64,65,5,97,0,0,65,66,5,115,0,0,66,67,5,
        115,0,0,67,68,5,101,0,0,68,69,5,114,0,0,69,70,5,116,0,0,70,12,1,
        0,0,0,71,72,5,100,0,0,72,73,5,105,0,0,73,74,5,115,0,0,74,75,5,116,
        0,0,75,76,5,105,0,0,76,77,5,110,0,0,77,78,5,99,0,0,78,79,5,116,0,
        0,79,14,1,0,0,0,80,81,5,62,0,0,81,82,5,61,0,0,82,16,1,0,0,0,83,84,
        5,60,0,0,84,85,5,61,0,0,85,18,1,0,0,0,86,87,5,60,0,0,87,20,1,0,0,
        0,88,89,5,62,0,0,89,22,1,0,0,0,90,91,5,61,0,0,91,24,1,0,0,0,92,93,
        5,97,0,0,93,94,5,110,0,0,94,95,5,100,0,0,95,26,1,0,0,0,96,97,5,111,
        0,0,97,98,5,114,0,0,98,28,1,0,0,0,99,100,5,99,0,0,100,101,5,104,
        0,0,101,102,5,101,0,0,102,103,5,99,0,0,103,104,5,107,0,0,104,105,
        5,45,0,0,105,106,5,115,0,0,106,107,5,97,0,0,107,108,5,116,0,0,108,
        30,1,0,0,0,109,110,5,103,0,0,110,111,5,101,0,0,111,112,5,116,0,0,
        112,113,5,45,0,0,113,114,5,109,0,0,114,115,5,111,0,0,115,116,5,100,
        0,0,116,117,5,101,0,0,117,118,5,108,0,0,118,32,1,0,0,0,119,123,5,
        59,0,0,120,122,9,0,0,0,121,120,1,0,0,0,122,125,1,0,0,0,123,124,1,
        0,0,0,123,121,1,0,0,0,124,126,1,0,0,0,125,123,1,0,0,0,126,127,5,
        10,0,0,127,128,1,0,0,0,128,129,6,16,0,0,129,34,1,0,0,0,130,132,7,
        0,0,0,131,130,1,0,0,0,132,133,1,0,0,0,133,131,1,0,0,0,133,134,1,
        0,0,0,134,138,1,0,0,0,135,137,7,1,0,0,136,135,1,0,0,0,137,140,1,
        0,0,0,138,136,1,0,0,0,138,139,1,0,0,0,139,36,1,0,0,0,140,138,1,0,
        0,0,141,143,7,2,0,0,142,141,1,0,0,0,143,144,1,0,0,0,144,142,1,0,
        0,0,144,145,1,0,0,0,145,38,1,0,0,0,146,148,7,3,0,0,147,146,1,0,0,
        0,148,149,1,0,0,0,149,147,1,0,0,0,149,150,1,0,0,0,150,151,1,0,0,
        0,151,152,6,19,0,0,152,40,1,0,0,0,6,0,123,133,138,144,149,1,6,0,
        0
    ]

class MyGrammar2Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    COMMENT = 17
    ID = 18
    NUMBER = 19
    WS = 20

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "'declare-fun'", "'()'", "'Int'", "')'", "'assert'", 
            "'distinct'", "'>='", "'<='", "'<'", "'>'", "'='", "'and'", 
            "'or'", "'check-sat'", "'get-model'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "ID", "NUMBER", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "COMMENT", "ID", "NUMBER", "WS" ]

    grammarFileName = "MyGrammar2.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



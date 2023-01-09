# Generated from MyGrammar.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,32,146,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,5,0,26,8,0,10,
        0,12,0,29,9,0,1,0,5,0,32,8,0,10,0,12,0,35,9,0,3,0,37,8,0,1,1,1,1,
        1,1,1,1,1,1,1,1,5,1,45,8,1,10,1,12,1,48,9,1,3,1,50,8,1,1,1,1,1,1,
        1,1,2,1,2,1,2,1,3,1,3,5,3,60,8,3,10,3,12,3,63,9,3,1,3,1,3,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,81,8,4,1,5,
        1,5,1,5,1,5,1,5,5,5,88,8,5,10,5,12,5,91,9,5,3,5,93,8,5,1,5,1,5,1,
        6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,3,9,117,8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,136,8,11,1,11,
        1,11,1,11,5,11,141,8,11,10,11,12,11,144,9,11,1,11,0,1,22,12,0,2,
        4,6,8,10,12,14,16,18,20,22,0,1,1,0,19,31,154,0,36,1,0,0,0,2,38,1,
        0,0,0,4,54,1,0,0,0,6,57,1,0,0,0,8,80,1,0,0,0,10,82,1,0,0,0,12,96,
        1,0,0,0,14,101,1,0,0,0,16,104,1,0,0,0,18,109,1,0,0,0,20,118,1,0,
        0,0,22,135,1,0,0,0,24,26,3,2,1,0,25,24,1,0,0,0,26,29,1,0,0,0,27,
        25,1,0,0,0,27,28,1,0,0,0,28,37,1,0,0,0,29,27,1,0,0,0,30,32,3,8,4,
        0,31,30,1,0,0,0,32,35,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,37,
        1,0,0,0,35,33,1,0,0,0,36,27,1,0,0,0,36,33,1,0,0,0,37,1,1,0,0,0,38,
        39,5,13,0,0,39,40,5,14,0,0,40,49,5,1,0,0,41,46,3,4,2,0,42,43,5,2,
        0,0,43,45,3,4,2,0,44,42,1,0,0,0,45,48,1,0,0,0,46,44,1,0,0,0,46,47,
        1,0,0,0,47,50,1,0,0,0,48,46,1,0,0,0,49,41,1,0,0,0,49,50,1,0,0,0,
        50,51,1,0,0,0,51,52,5,3,0,0,52,53,3,6,3,0,53,3,1,0,0,0,54,55,5,13,
        0,0,55,56,5,14,0,0,56,5,1,0,0,0,57,61,5,4,0,0,58,60,3,8,4,0,59,58,
        1,0,0,0,60,63,1,0,0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,64,1,0,0,0,
        63,61,1,0,0,0,64,65,5,5,0,0,65,7,1,0,0,0,66,67,3,10,5,0,67,68,5,
        6,0,0,68,81,1,0,0,0,69,70,3,12,6,0,70,71,5,6,0,0,71,81,1,0,0,0,72,
        73,3,14,7,0,73,74,5,6,0,0,74,81,1,0,0,0,75,76,3,16,8,0,76,77,5,6,
        0,0,77,81,1,0,0,0,78,81,3,18,9,0,79,81,3,20,10,0,80,66,1,0,0,0,80,
        69,1,0,0,0,80,72,1,0,0,0,80,75,1,0,0,0,80,78,1,0,0,0,80,79,1,0,0,
        0,81,9,1,0,0,0,82,83,5,14,0,0,83,92,5,1,0,0,84,89,3,22,11,0,85,86,
        5,2,0,0,86,88,3,22,11,0,87,85,1,0,0,0,88,91,1,0,0,0,89,87,1,0,0,
        0,89,90,1,0,0,0,90,93,1,0,0,0,91,89,1,0,0,0,92,84,1,0,0,0,92,93,
        1,0,0,0,93,94,1,0,0,0,94,95,5,3,0,0,95,11,1,0,0,0,96,97,5,7,0,0,
        97,98,5,1,0,0,98,99,3,22,11,0,99,100,5,3,0,0,100,13,1,0,0,0,101,
        102,5,8,0,0,102,103,3,22,11,0,103,15,1,0,0,0,104,105,5,13,0,0,105,
        106,5,14,0,0,106,107,5,9,0,0,107,108,3,22,11,0,108,17,1,0,0,0,109,
        110,5,10,0,0,110,111,5,1,0,0,111,112,3,22,11,0,112,113,5,3,0,0,113,
        116,3,8,4,0,114,115,5,11,0,0,115,117,3,8,4,0,116,114,1,0,0,0,116,
        117,1,0,0,0,117,19,1,0,0,0,118,119,5,12,0,0,119,120,5,1,0,0,120,
        121,3,22,11,0,121,122,5,3,0,0,122,123,3,8,4,0,123,21,1,0,0,0,124,
        125,6,11,-1,0,125,136,5,14,0,0,126,136,5,15,0,0,127,136,5,16,0,0,
        128,136,5,17,0,0,129,136,5,18,0,0,130,136,3,10,5,0,131,132,5,1,0,
        0,132,133,3,22,11,0,133,134,5,3,0,0,134,136,1,0,0,0,135,124,1,0,
        0,0,135,126,1,0,0,0,135,127,1,0,0,0,135,128,1,0,0,0,135,129,1,0,
        0,0,135,130,1,0,0,0,135,131,1,0,0,0,136,142,1,0,0,0,137,138,10,1,
        0,0,138,139,7,0,0,0,139,141,3,22,11,2,140,137,1,0,0,0,141,144,1,
        0,0,0,142,140,1,0,0,0,142,143,1,0,0,0,143,23,1,0,0,0,144,142,1,0,
        0,0,12,27,33,36,46,49,61,80,89,92,116,135,142
    ]

class MyGrammarParser ( Parser ):

    grammarFileName = "MyGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "','", "')'", "'{'", "'}'", "';'", 
                     "'print'", "'return'", "'='", "'if'", "'else'", "'while'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'=='", "'!='", "'>'", "'<'", "'>='", "'<='", 
                     "'&&'", "'||'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "TYPE", "ID", "INT", "FLOAT", "BOOL", 
                      "STRING", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "MODULO", 
                      "EQUALS", "NOT_EQUALS", "GREATER_THAN", "LESS_THAN", 
                      "GREATER_THAN_EQUALS", "LESS_THAN_EQUALS", "AND", 
                      "OR", "WS" ]

    RULE_prog = 0
    RULE_function_declaration = 1
    RULE_parameter_declaration = 2
    RULE_block = 3
    RULE_statement = 4
    RULE_function_call = 5
    RULE_print_statement = 6
    RULE_return_statement = 7
    RULE_assignment = 8
    RULE_if_statement = 9
    RULE_while_statement = 10
    RULE_expression = 11

    ruleNames =  [ "prog", "function_declaration", "parameter_declaration", 
                   "block", "statement", "function_call", "print_statement", 
                   "return_statement", "assignment", "if_statement", "while_statement", 
                   "expression" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    TYPE=13
    ID=14
    INT=15
    FLOAT=16
    BOOL=17
    STRING=18
    PLUS=19
    MINUS=20
    MULTIPLY=21
    DIVIDE=22
    MODULO=23
    EQUALS=24
    NOT_EQUALS=25
    GREATER_THAN=26
    LESS_THAN=27
    GREATER_THAN_EQUALS=28
    LESS_THAN_EQUALS=29
    AND=30
    OR=31
    WS=32

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.Function_declarationContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.Function_declarationContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = MyGrammarParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.state = 36
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==13:
                    self.state = 24
                    self.function_declaration()
                    self.state = 29
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while ((_la) & ~0x3f) == 0 and ((1 << _la) & 30080) != 0:
                    self.state = 30
                    self.statement()
                    self.state = 35
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MyGrammarParser.TYPE, 0)

        def ID(self):
            return self.getToken(MyGrammarParser.ID, 0)

        def block(self):
            return self.getTypedRuleContext(MyGrammarParser.BlockContext,0)


        def parameter_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.Parameter_declarationContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.Parameter_declarationContext,i)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_function_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_declaration" ):
                listener.enterFunction_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_declaration" ):
                listener.exitFunction_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_declaration" ):
                return visitor.visitFunction_declaration(self)
            else:
                return visitor.visitChildren(self)




    def function_declaration(self):

        localctx = MyGrammarParser.Function_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_function_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(MyGrammarParser.TYPE)
            self.state = 39
            self.match(MyGrammarParser.ID)
            self.state = 40
            self.match(MyGrammarParser.T__0)
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 41
                self.parameter_declaration()
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 42
                    self.match(MyGrammarParser.T__1)
                    self.state = 43
                    self.parameter_declaration()
                    self.state = 48
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 51
            self.match(MyGrammarParser.T__2)
            self.state = 52
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MyGrammarParser.TYPE, 0)

        def ID(self):
            return self.getToken(MyGrammarParser.ID, 0)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_parameter_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter_declaration" ):
                listener.enterParameter_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter_declaration" ):
                listener.exitParameter_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_declaration" ):
                return visitor.visitParameter_declaration(self)
            else:
                return visitor.visitChildren(self)




    def parameter_declaration(self):

        localctx = MyGrammarParser.Parameter_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_parameter_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(MyGrammarParser.TYPE)
            self.state = 55
            self.match(MyGrammarParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MyGrammarParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(MyGrammarParser.T__3)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 30080) != 0:
                self.state = 58
                self.statement()
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 64
            self.match(MyGrammarParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_call(self):
            return self.getTypedRuleContext(MyGrammarParser.Function_callContext,0)


        def print_statement(self):
            return self.getTypedRuleContext(MyGrammarParser.Print_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(MyGrammarParser.Return_statementContext,0)


        def assignment(self):
            return self.getTypedRuleContext(MyGrammarParser.AssignmentContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(MyGrammarParser.If_statementContext,0)


        def while_statement(self):
            return self.getTypedRuleContext(MyGrammarParser.While_statementContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MyGrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statement)
        try:
            self.state = 80
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.function_call()
                self.state = 67
                self.match(MyGrammarParser.T__5)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.print_statement()
                self.state = 70
                self.match(MyGrammarParser.T__5)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 72
                self.return_statement()
                self.state = 73
                self.match(MyGrammarParser.T__5)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 75
                self.assignment()
                self.state = 76
                self.match(MyGrammarParser.T__5)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 5)
                self.state = 78
                self.if_statement()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 6)
                self.state = 79
                self.while_statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MyGrammarParser.ID, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.ExpressionContext,i)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_function_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call" ):
                listener.enterFunction_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call" ):
                listener.exitFunction_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = MyGrammarParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(MyGrammarParser.ID)
            self.state = 83
            self.match(MyGrammarParser.T__0)
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 507906) != 0:
                self.state = 84
                self.expression(0)
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 85
                    self.match(MyGrammarParser.T__1)
                    self.state = 86
                    self.expression(0)
                    self.state = 91
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 94
            self.match(MyGrammarParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MyGrammarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_print_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_statement" ):
                listener.enterPrint_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_statement" ):
                listener.exitPrint_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint_statement" ):
                return visitor.visitPrint_statement(self)
            else:
                return visitor.visitChildren(self)




    def print_statement(self):

        localctx = MyGrammarParser.Print_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_print_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(MyGrammarParser.T__6)
            self.state = 97
            self.match(MyGrammarParser.T__0)
            self.state = 98
            self.expression(0)
            self.state = 99
            self.match(MyGrammarParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MyGrammarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_return_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_statement" ):
                listener.enterReturn_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_statement" ):
                listener.exitReturn_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = MyGrammarParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(MyGrammarParser.T__7)
            self.state = 102
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MyGrammarParser.TYPE, 0)

        def ID(self):
            return self.getToken(MyGrammarParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(MyGrammarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = MyGrammarParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(MyGrammarParser.TYPE)
            self.state = 105
            self.match(MyGrammarParser.ID)
            self.state = 106
            self.match(MyGrammarParser.T__8)
            self.state = 107
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MyGrammarParser.ExpressionContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_if_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_statement" ):
                listener.enterIf_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_statement" ):
                listener.exitIf_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = MyGrammarParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(MyGrammarParser.T__9)
            self.state = 110
            self.match(MyGrammarParser.T__0)
            self.state = 111
            self.expression(0)
            self.state = 112
            self.match(MyGrammarParser.T__2)
            self.state = 113
            self.statement()
            self.state = 116
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 114
                self.match(MyGrammarParser.T__10)
                self.state = 115
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MyGrammarParser.ExpressionContext,0)


        def statement(self):
            return self.getTypedRuleContext(MyGrammarParser.StatementContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_while_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_statement" ):
                listener.enterWhile_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_statement" ):
                listener.exitWhile_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_statement" ):
                return visitor.visitWhile_statement(self)
            else:
                return visitor.visitChildren(self)




    def while_statement(self):

        localctx = MyGrammarParser.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(MyGrammarParser.T__11)
            self.state = 119
            self.match(MyGrammarParser.T__0)
            self.state = 120
            self.expression(0)
            self.state = 121
            self.match(MyGrammarParser.T__2)
            self.state = 122
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MyGrammarParser.ID, 0)

        def INT(self):
            return self.getToken(MyGrammarParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MyGrammarParser.FLOAT, 0)

        def BOOL(self):
            return self.getToken(MyGrammarParser.BOOL, 0)

        def STRING(self):
            return self.getToken(MyGrammarParser.STRING, 0)

        def function_call(self):
            return self.getTypedRuleContext(MyGrammarParser.Function_callContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.ExpressionContext,i)


        def PLUS(self):
            return self.getToken(MyGrammarParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(MyGrammarParser.MINUS, 0)

        def MULTIPLY(self):
            return self.getToken(MyGrammarParser.MULTIPLY, 0)

        def DIVIDE(self):
            return self.getToken(MyGrammarParser.DIVIDE, 0)

        def MODULO(self):
            return self.getToken(MyGrammarParser.MODULO, 0)

        def EQUALS(self):
            return self.getToken(MyGrammarParser.EQUALS, 0)

        def NOT_EQUALS(self):
            return self.getToken(MyGrammarParser.NOT_EQUALS, 0)

        def GREATER_THAN(self):
            return self.getToken(MyGrammarParser.GREATER_THAN, 0)

        def LESS_THAN(self):
            return self.getToken(MyGrammarParser.LESS_THAN, 0)

        def GREATER_THAN_EQUALS(self):
            return self.getToken(MyGrammarParser.GREATER_THAN_EQUALS, 0)

        def LESS_THAN_EQUALS(self):
            return self.getToken(MyGrammarParser.LESS_THAN_EQUALS, 0)

        def AND(self):
            return self.getToken(MyGrammarParser.AND, 0)

        def OR(self):
            return self.getToken(MyGrammarParser.OR, 0)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyGrammarParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 125
                self.match(MyGrammarParser.ID)
                pass

            elif la_ == 2:
                self.state = 126
                self.match(MyGrammarParser.INT)
                pass

            elif la_ == 3:
                self.state = 127
                self.match(MyGrammarParser.FLOAT)
                pass

            elif la_ == 4:
                self.state = 128
                self.match(MyGrammarParser.BOOL)
                pass

            elif la_ == 5:
                self.state = 129
                self.match(MyGrammarParser.STRING)
                pass

            elif la_ == 6:
                self.state = 130
                self.function_call()
                pass

            elif la_ == 7:
                self.state = 131
                self.match(MyGrammarParser.T__0)
                self.state = 132
                self.expression(0)
                self.state = 133
                self.match(MyGrammarParser.T__2)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 142
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MyGrammarParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 137
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 138
                    _la = self._input.LA(1)
                    if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 4294443008) != 0):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 139
                    self.expression(2) 
                self.state = 144
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[11] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         





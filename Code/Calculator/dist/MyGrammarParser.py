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
        4,1,37,167,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,5,0,30,8,0,10,0,12,0,33,9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,3,1,47,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,56,8,
        2,10,2,12,2,59,9,2,3,2,61,8,2,1,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,5,
        4,71,8,4,10,4,12,4,74,9,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,92,8,5,1,6,1,6,1,6,1,6,1,6,5,6,99,
        8,6,10,6,12,6,102,9,6,3,6,104,8,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,
        8,1,8,1,8,1,9,1,9,1,9,1,9,3,9,120,8,9,1,10,1,10,1,10,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,134,8,10,1,11,1,11,1,11,1,
        11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,
        12,1,12,1,12,3,12,155,8,12,1,12,1,12,1,12,5,12,160,8,12,10,12,12,
        12,163,9,12,1,13,1,13,1,13,0,1,24,14,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,0,2,1,0,24,36,1,0,14,18,177,0,31,1,0,0,0,2,46,1,0,0,0,4,
        48,1,0,0,0,6,65,1,0,0,0,8,68,1,0,0,0,10,91,1,0,0,0,12,93,1,0,0,0,
        14,107,1,0,0,0,16,112,1,0,0,0,18,115,1,0,0,0,20,121,1,0,0,0,22,135,
        1,0,0,0,24,154,1,0,0,0,26,164,1,0,0,0,28,30,3,2,1,0,29,28,1,0,0,
        0,30,33,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,1,1,0,0,0,33,31,1,
        0,0,0,34,47,3,4,2,0,35,36,3,12,6,0,36,37,5,1,0,0,37,47,1,0,0,0,38,
        39,3,14,7,0,39,40,5,1,0,0,40,47,1,0,0,0,41,42,3,18,9,0,42,43,5,1,
        0,0,43,47,1,0,0,0,44,47,3,20,10,0,45,47,3,22,11,0,46,34,1,0,0,0,
        46,35,1,0,0,0,46,38,1,0,0,0,46,41,1,0,0,0,46,44,1,0,0,0,46,45,1,
        0,0,0,47,3,1,0,0,0,48,49,5,2,0,0,49,50,3,26,13,0,50,51,5,19,0,0,
        51,60,5,3,0,0,52,57,3,6,3,0,53,54,5,4,0,0,54,56,3,6,3,0,55,53,1,
        0,0,0,56,59,1,0,0,0,57,55,1,0,0,0,57,58,1,0,0,0,58,61,1,0,0,0,59,
        57,1,0,0,0,60,52,1,0,0,0,60,61,1,0,0,0,61,62,1,0,0,0,62,63,5,5,0,
        0,63,64,3,8,4,0,64,5,1,0,0,0,65,66,3,26,13,0,66,67,5,19,0,0,67,7,
        1,0,0,0,68,72,5,6,0,0,69,71,3,10,5,0,70,69,1,0,0,0,71,74,1,0,0,0,
        72,70,1,0,0,0,72,73,1,0,0,0,73,75,1,0,0,0,74,72,1,0,0,0,75,76,5,
        7,0,0,76,9,1,0,0,0,77,78,3,12,6,0,78,79,5,1,0,0,79,92,1,0,0,0,80,
        81,3,14,7,0,81,82,5,1,0,0,82,92,1,0,0,0,83,84,3,16,8,0,84,85,5,1,
        0,0,85,92,1,0,0,0,86,87,3,18,9,0,87,88,5,1,0,0,88,92,1,0,0,0,89,
        92,3,20,10,0,90,92,3,22,11,0,91,77,1,0,0,0,91,80,1,0,0,0,91,83,1,
        0,0,0,91,86,1,0,0,0,91,89,1,0,0,0,91,90,1,0,0,0,92,11,1,0,0,0,93,
        94,5,19,0,0,94,103,5,3,0,0,95,100,3,24,12,0,96,97,5,4,0,0,97,99,
        3,24,12,0,98,96,1,0,0,0,99,102,1,0,0,0,100,98,1,0,0,0,100,101,1,
        0,0,0,101,104,1,0,0,0,102,100,1,0,0,0,103,95,1,0,0,0,103,104,1,0,
        0,0,104,105,1,0,0,0,105,106,5,5,0,0,106,13,1,0,0,0,107,108,5,8,0,
        0,108,109,5,3,0,0,109,110,3,24,12,0,110,111,5,5,0,0,111,15,1,0,0,
        0,112,113,5,9,0,0,113,114,3,24,12,0,114,17,1,0,0,0,115,116,3,26,
        13,0,116,119,5,19,0,0,117,118,5,10,0,0,118,120,3,24,12,0,119,117,
        1,0,0,0,119,120,1,0,0,0,120,19,1,0,0,0,121,122,5,11,0,0,122,123,
        5,3,0,0,123,124,3,24,12,0,124,125,5,5,0,0,125,126,5,6,0,0,126,127,
        3,10,5,0,127,133,5,7,0,0,128,129,5,12,0,0,129,130,5,6,0,0,130,131,
        3,10,5,0,131,132,5,7,0,0,132,134,1,0,0,0,133,128,1,0,0,0,133,134,
        1,0,0,0,134,21,1,0,0,0,135,136,5,13,0,0,136,137,5,3,0,0,137,138,
        3,24,12,0,138,139,5,5,0,0,139,140,5,6,0,0,140,141,3,10,5,0,141,142,
        5,7,0,0,142,23,1,0,0,0,143,144,6,12,-1,0,144,155,5,19,0,0,145,155,
        5,20,0,0,146,155,5,21,0,0,147,155,5,22,0,0,148,155,5,23,0,0,149,
        155,3,12,6,0,150,151,5,3,0,0,151,152,3,24,12,0,152,153,5,5,0,0,153,
        155,1,0,0,0,154,143,1,0,0,0,154,145,1,0,0,0,154,146,1,0,0,0,154,
        147,1,0,0,0,154,148,1,0,0,0,154,149,1,0,0,0,154,150,1,0,0,0,155,
        161,1,0,0,0,156,157,10,1,0,0,157,158,7,0,0,0,158,160,3,24,12,2,159,
        156,1,0,0,0,160,163,1,0,0,0,161,159,1,0,0,0,161,162,1,0,0,0,162,
        25,1,0,0,0,163,161,1,0,0,0,164,165,7,1,0,0,165,27,1,0,0,0,12,31,
        46,57,60,72,91,100,103,119,133,154,161
    ]

class MyGrammarParser ( Parser ):

    grammarFileName = "MyGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'function'", "'('", "','", "')'", 
                     "'{'", "'}'", "'print'", "'return'", "'='", "'if'", 
                     "'else'", "'while'", "'int'", "'float'", "'bool'", 
                     "'string'", "'void'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'=='", "'!='", "'>'", "'<'", "'>='", "'<='", 
                     "'&&'", "'||'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "INT", 
                      "FLOAT", "BOOL", "STRING", "PLUS", "MINUS", "MULTIPLY", 
                      "DIVIDE", "MODULO", "EQUALS", "NOT_EQUALS", "GREATER_THAN", 
                      "LESS_THAN", "GREATER_THAN_EQUALS", "LESS_THAN_EQUALS", 
                      "AND", "OR", "WS" ]

    RULE_prog = 0
    RULE_single_statement = 1
    RULE_function_declaration = 2
    RULE_parameter_declaration = 3
    RULE_block = 4
    RULE_statement = 5
    RULE_function_call = 6
    RULE_print_statement = 7
    RULE_return_statement = 8
    RULE_assignment = 9
    RULE_if_statement = 10
    RULE_while_statement = 11
    RULE_expression = 12
    RULE_type = 13

    ruleNames =  [ "prog", "single_statement", "function_declaration", "parameter_declaration", 
                   "block", "statement", "function_call", "print_statement", 
                   "return_statement", "assignment", "if_statement", "while_statement", 
                   "expression", "type" ]

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
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    ID=19
    INT=20
    FLOAT=21
    BOOL=22
    STRING=23
    PLUS=24
    MINUS=25
    MULTIPLY=26
    DIVIDE=27
    MODULO=28
    EQUALS=29
    NOT_EQUALS=30
    GREATER_THAN=31
    LESS_THAN=32
    GREATER_THAN_EQUALS=33
    LESS_THAN_EQUALS=34
    AND=35
    OR=36
    WS=37

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

        def single_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.Single_statementContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.Single_statementContext,i)


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
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 1042692) != 0:
                self.state = 28
                self.single_statement()
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Single_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_declaration(self):
            return self.getTypedRuleContext(MyGrammarParser.Function_declarationContext,0)


        def function_call(self):
            return self.getTypedRuleContext(MyGrammarParser.Function_callContext,0)


        def print_statement(self):
            return self.getTypedRuleContext(MyGrammarParser.Print_statementContext,0)


        def assignment(self):
            return self.getTypedRuleContext(MyGrammarParser.AssignmentContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(MyGrammarParser.If_statementContext,0)


        def while_statement(self):
            return self.getTypedRuleContext(MyGrammarParser.While_statementContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_single_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingle_statement" ):
                listener.enterSingle_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingle_statement" ):
                listener.exitSingle_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingle_statement" ):
                return visitor.visitSingle_statement(self)
            else:
                return visitor.visitChildren(self)




    def single_statement(self):

        localctx = MyGrammarParser.Single_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_single_statement)
        try:
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.function_declaration()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.function_call()
                self.state = 36
                self.match(MyGrammarParser.T__0)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 38
                self.print_statement()
                self.state = 39
                self.match(MyGrammarParser.T__0)
                pass
            elif token in [14, 15, 16, 17, 18]:
                self.enterOuterAlt(localctx, 4)
                self.state = 41
                self.assignment()
                self.state = 42
                self.match(MyGrammarParser.T__0)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 5)
                self.state = 44
                self.if_statement()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 6)
                self.state = 45
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


    class Function_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(MyGrammarParser.TypeContext,0)


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
        self.enterRule(localctx, 4, self.RULE_function_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(MyGrammarParser.T__1)
            self.state = 49
            self.type_()
            self.state = 50
            self.match(MyGrammarParser.ID)
            self.state = 51
            self.match(MyGrammarParser.T__2)
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 507904) != 0:
                self.state = 52
                self.parameter_declaration()
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==4:
                    self.state = 53
                    self.match(MyGrammarParser.T__3)
                    self.state = 54
                    self.parameter_declaration()
                    self.state = 59
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 62
            self.match(MyGrammarParser.T__4)
            self.state = 63
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

        def type_(self):
            return self.getTypedRuleContext(MyGrammarParser.TypeContext,0)


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
        self.enterRule(localctx, 6, self.RULE_parameter_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.type_()
            self.state = 66
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
        self.enterRule(localctx, 8, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(MyGrammarParser.T__5)
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 1043200) != 0:
                self.state = 69
                self.statement()
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 75
            self.match(MyGrammarParser.T__6)
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
        self.enterRule(localctx, 10, self.RULE_statement)
        try:
            self.state = 91
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.function_call()
                self.state = 78
                self.match(MyGrammarParser.T__0)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.print_statement()
                self.state = 81
                self.match(MyGrammarParser.T__0)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 83
                self.return_statement()
                self.state = 84
                self.match(MyGrammarParser.T__0)
                pass
            elif token in [14, 15, 16, 17, 18]:
                self.enterOuterAlt(localctx, 4)
                self.state = 86
                self.assignment()
                self.state = 87
                self.match(MyGrammarParser.T__0)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 5)
                self.state = 89
                self.if_statement()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 6)
                self.state = 90
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
        self.enterRule(localctx, 12, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(MyGrammarParser.ID)
            self.state = 94
            self.match(MyGrammarParser.T__2)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 16252936) != 0:
                self.state = 95
                self.expression(0)
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==4:
                    self.state = 96
                    self.match(MyGrammarParser.T__3)
                    self.state = 97
                    self.expression(0)
                    self.state = 102
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 105
            self.match(MyGrammarParser.T__4)
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
        self.enterRule(localctx, 14, self.RULE_print_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(MyGrammarParser.T__7)
            self.state = 108
            self.match(MyGrammarParser.T__2)
            self.state = 109
            self.expression(0)
            self.state = 110
            self.match(MyGrammarParser.T__4)
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
        self.enterRule(localctx, 16, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(MyGrammarParser.T__8)
            self.state = 113
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

        def type_(self):
            return self.getTypedRuleContext(MyGrammarParser.TypeContext,0)


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
        self.enterRule(localctx, 18, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.type_()
            self.state = 116
            self.match(MyGrammarParser.ID)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 117
                self.match(MyGrammarParser.T__9)
                self.state = 118
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
        self.enterRule(localctx, 20, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(MyGrammarParser.T__10)
            self.state = 122
            self.match(MyGrammarParser.T__2)
            self.state = 123
            self.expression(0)
            self.state = 124
            self.match(MyGrammarParser.T__4)
            self.state = 125
            self.match(MyGrammarParser.T__5)
            self.state = 126
            self.statement()
            self.state = 127
            self.match(MyGrammarParser.T__6)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 128
                self.match(MyGrammarParser.T__11)
                self.state = 129
                self.match(MyGrammarParser.T__5)
                self.state = 130
                self.statement()
                self.state = 131
                self.match(MyGrammarParser.T__6)


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
        self.enterRule(localctx, 22, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(MyGrammarParser.T__12)
            self.state = 136
            self.match(MyGrammarParser.T__2)
            self.state = 137
            self.expression(0)
            self.state = 138
            self.match(MyGrammarParser.T__4)
            self.state = 139
            self.match(MyGrammarParser.T__5)
            self.state = 140
            self.statement()
            self.state = 141
            self.match(MyGrammarParser.T__6)
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
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 144
                self.match(MyGrammarParser.ID)
                pass

            elif la_ == 2:
                self.state = 145
                self.match(MyGrammarParser.INT)
                pass

            elif la_ == 3:
                self.state = 146
                self.match(MyGrammarParser.FLOAT)
                pass

            elif la_ == 4:
                self.state = 147
                self.match(MyGrammarParser.BOOL)
                pass

            elif la_ == 5:
                self.state = 148
                self.match(MyGrammarParser.STRING)
                pass

            elif la_ == 6:
                self.state = 149
                self.function_call()
                pass

            elif la_ == 7:
                self.state = 150
                self.match(MyGrammarParser.T__2)
                self.state = 151
                self.expression(0)
                self.state = 152
                self.match(MyGrammarParser.T__4)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 161
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MyGrammarParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 156
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 157
                    _la = self._input.LA(1)
                    if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 137422176256) != 0):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 158
                    self.expression(2) 
                self.state = 163
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyGrammarParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = MyGrammarParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 507904) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[12] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         





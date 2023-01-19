# Generated from MyGrammar2.g4 by ANTLR 4.11.1
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
        4,1,24,143,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,4,0,34,8,0,11,0,12,0,35,1,1,1,1,1,1,1,1,
        1,1,3,1,43,8,1,1,2,1,2,1,2,1,2,1,2,5,2,50,8,2,10,2,12,2,53,9,2,1,
        2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,
        5,1,5,1,5,1,5,1,5,5,5,76,8,5,10,5,12,5,79,9,5,1,5,1,5,1,6,1,6,1,
        6,1,6,1,6,5,6,88,8,6,10,6,12,6,91,9,6,1,6,1,6,1,7,1,7,1,7,1,7,1,
        7,5,7,100,8,7,10,7,12,7,103,9,7,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,125,8,9,1,10,
        1,10,1,11,1,11,1,12,1,12,1,13,1,13,1,14,1,14,1,14,1,14,1,15,1,15,
        1,15,1,15,1,15,0,0,16,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,
        0,4,1,0,21,22,1,0,7,10,1,0,12,15,1,0,16,17,140,0,33,1,0,0,0,2,42,
        1,0,0,0,4,44,1,0,0,0,6,58,1,0,0,0,8,65,1,0,0,0,10,70,1,0,0,0,12,
        82,1,0,0,0,14,94,1,0,0,0,16,106,1,0,0,0,18,124,1,0,0,0,20,126,1,
        0,0,0,22,128,1,0,0,0,24,130,1,0,0,0,26,132,1,0,0,0,28,134,1,0,0,
        0,30,138,1,0,0,0,32,34,3,2,1,0,33,32,1,0,0,0,34,35,1,0,0,0,35,33,
        1,0,0,0,35,36,1,0,0,0,36,1,1,0,0,0,37,43,3,4,2,0,38,43,3,8,4,0,39,
        43,3,28,14,0,40,43,3,30,15,0,41,43,3,6,3,0,42,37,1,0,0,0,42,38,1,
        0,0,0,42,39,1,0,0,0,42,40,1,0,0,0,42,41,1,0,0,0,43,3,1,0,0,0,44,
        45,5,1,0,0,45,46,5,2,0,0,46,47,5,21,0,0,47,51,5,1,0,0,48,50,5,24,
        0,0,49,48,1,0,0,0,50,53,1,0,0,0,51,49,1,0,0,0,51,52,1,0,0,0,52,54,
        1,0,0,0,53,51,1,0,0,0,54,55,5,3,0,0,55,56,5,24,0,0,56,57,5,3,0,0,
        57,5,1,0,0,0,58,59,5,1,0,0,59,60,5,4,0,0,60,61,5,21,0,0,61,62,5,
        24,0,0,62,63,5,22,0,0,63,64,5,3,0,0,64,7,1,0,0,0,65,66,5,1,0,0,66,
        67,5,5,0,0,67,68,3,18,9,0,68,69,5,3,0,0,69,9,1,0,0,0,70,71,5,1,0,
        0,71,72,5,6,0,0,72,73,3,16,8,0,73,77,3,16,8,0,74,76,3,16,8,0,75,
        74,1,0,0,0,76,79,1,0,0,0,77,75,1,0,0,0,77,78,1,0,0,0,78,80,1,0,0,
        0,79,77,1,0,0,0,80,81,5,3,0,0,81,11,1,0,0,0,82,83,5,1,0,0,83,84,
        3,26,13,0,84,85,3,18,9,0,85,89,3,18,9,0,86,88,3,18,9,0,87,86,1,0,
        0,0,88,91,1,0,0,0,89,87,1,0,0,0,89,90,1,0,0,0,90,92,1,0,0,0,91,89,
        1,0,0,0,92,93,5,3,0,0,93,13,1,0,0,0,94,95,5,1,0,0,95,96,3,24,12,
        0,96,97,5,22,0,0,97,101,5,22,0,0,98,100,5,22,0,0,99,98,1,0,0,0,100,
        103,1,0,0,0,101,99,1,0,0,0,101,102,1,0,0,0,102,104,1,0,0,0,103,101,
        1,0,0,0,104,105,5,3,0,0,105,15,1,0,0,0,106,107,7,0,0,0,107,17,1,
        0,0,0,108,125,3,10,5,0,109,125,3,12,6,0,110,111,5,1,0,0,111,112,
        3,20,10,0,112,113,3,16,8,0,113,114,3,16,8,0,114,115,5,3,0,0,115,
        125,1,0,0,0,116,125,3,14,7,0,117,118,5,1,0,0,118,119,3,22,11,0,119,
        120,5,21,0,0,120,121,3,18,9,0,121,122,5,3,0,0,122,125,1,0,0,0,123,
        125,3,16,8,0,124,108,1,0,0,0,124,109,1,0,0,0,124,110,1,0,0,0,124,
        116,1,0,0,0,124,117,1,0,0,0,124,123,1,0,0,0,125,19,1,0,0,0,126,127,
        7,1,0,0,127,21,1,0,0,0,128,129,5,11,0,0,129,23,1,0,0,0,130,131,7,
        2,0,0,131,25,1,0,0,0,132,133,7,3,0,0,133,27,1,0,0,0,134,135,5,1,
        0,0,135,136,5,18,0,0,136,137,5,3,0,0,137,29,1,0,0,0,138,139,5,1,
        0,0,139,140,5,19,0,0,140,141,5,3,0,0,141,31,1,0,0,0,7,35,42,51,77,
        89,101,124
    ]

class MyGrammar2Parser ( Parser ):

    grammarFileName = "MyGrammar2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "'declare-fun'", "')'", "'define-const'", 
                     "'assert'", "'distinct'", "'>='", "'<='", "'<'", "'>'", 
                     "'='", "'+'", "'-'", "'/'", "'*'", "'and'", "'or'", 
                     "'check-sat'", "'get-model'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'Int'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "COMMENT", "ID", "NUMBER", "WS", "INT_W" ]

    RULE_program = 0
    RULE_command = 1
    RULE_declare_fun = 2
    RULE_declare_const = 3
    RULE_assert_cmd = 4
    RULE_distinct_formula = 5
    RULE_comp_formula = 6
    RULE_operation_dormula = 7
    RULE_values = 8
    RULE_formula = 9
    RULE_comparator = 10
    RULE_equal = 11
    RULE_operation = 12
    RULE_comp = 13
    RULE_check_sat = 14
    RULE_get_model = 15

    ruleNames =  [ "program", "command", "declare_fun", "declare_const", 
                   "assert_cmd", "distinct_formula", "comp_formula", "operation_dormula", 
                   "values", "formula", "comparator", "equal", "operation", 
                   "comp", "check_sat", "get_model" ]

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
    T__18=19
    COMMENT=20
    ID=21
    NUMBER=22
    WS=23
    INT_W=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammar2Parser.CommandContext)
            else:
                return self.getTypedRuleContext(MyGrammar2Parser.CommandContext,i)


        def getRuleIndex(self):
            return MyGrammar2Parser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = MyGrammar2Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 32
                self.command()
                self.state = 35 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declare_fun(self):
            return self.getTypedRuleContext(MyGrammar2Parser.Declare_funContext,0)


        def assert_cmd(self):
            return self.getTypedRuleContext(MyGrammar2Parser.Assert_cmdContext,0)


        def check_sat(self):
            return self.getTypedRuleContext(MyGrammar2Parser.Check_satContext,0)


        def get_model(self):
            return self.getTypedRuleContext(MyGrammar2Parser.Get_modelContext,0)


        def declare_const(self):
            return self.getTypedRuleContext(MyGrammar2Parser.Declare_constContext,0)


        def getRuleIndex(self):
            return MyGrammar2Parser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)




    def command(self):

        localctx = MyGrammar2Parser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_command)
        try:
            self.state = 42
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.declare_fun()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.assert_cmd()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 39
                self.check_sat()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 40
                self.get_model()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 41
                self.declare_const()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declare_funContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MyGrammar2Parser.ID, 0)

        def INT_W(self, i:int=None):
            if i is None:
                return self.getTokens(MyGrammar2Parser.INT_W)
            else:
                return self.getToken(MyGrammar2Parser.INT_W, i)

        def getRuleIndex(self):
            return MyGrammar2Parser.RULE_declare_fun

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclare_fun" ):
                listener.enterDeclare_fun(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclare_fun" ):
                listener.exitDeclare_fun(self)




    def declare_fun(self):

        localctx = MyGrammar2Parser.Declare_funContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declare_fun)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(MyGrammar2Parser.T__0)
            self.state = 45
            self.match(MyGrammar2Parser.T__1)
            self.state = 46
            self.match(MyGrammar2Parser.ID)
            self.state = 47
            self.match(MyGrammar2Parser.T__0)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24:
                self.state = 48
                self.match(MyGrammar2Parser.INT_W)
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 54
            self.match(MyGrammar2Parser.T__2)
            self.state = 55
            self.match(MyGrammar2Parser.INT_W)
            self.state = 56
            self.match(MyGrammar2Parser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declare_constContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MyGrammar2Parser.ID, 0)

        def INT_W(self):
            return self.getToken(MyGrammar2Parser.INT_W, 0)

        def NUMBER(self):
            return self.getToken(MyGrammar2Parser.NUMBER, 0)

        def getRuleIndex(self):
            return MyGrammar2Parser.RULE_declare_const

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclare_const" ):
                listener.enterDeclare_const(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclare_const" ):
                listener.exitDeclare_const(self)




    def declare_const(self):

        localctx = MyGrammar2Parser.Declare_constContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declare_const)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(MyGrammar2Parser.T__0)
            self.state = 59
            self.match(MyGrammar2Parser.T__3)
            self.state = 60
            self.match(MyGrammar2Parser.ID)
            self.state = 61
            self.match(MyGrammar2Parser.INT_W)
            self.state = 62
            self.match(MyGrammar2Parser.NUMBER)
            self.state = 63
            self.match(MyGrammar2Parser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assert_cmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def formula(self):
            return self.getTypedRuleContext(MyGrammar2Parser.FormulaContext,0)


        def getRuleIndex(self):
            return MyGrammar2Parser.RULE_assert_cmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssert_cmd" ):
                listener.enterAssert_cmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssert_cmd" ):
                listener.exitAssert_cmd(self)




    def assert_cmd(self):

        localctx = MyGrammar2Parser.Assert_cmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assert_cmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(MyGrammar2Parser.T__0)
            self.state = 66
            self.match(MyGrammar2Parser.T__4)
            self.state = 67
            self.formula()
            self.state = 68
            self.match(MyGrammar2Parser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Distinct_formulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def values(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammar2Parser.ValuesContext)
            else:
                return self.getTypedRuleContext(MyGrammar2Parser.ValuesContext,i)


        def getRuleIndex(self):
            return MyGrammar2Parser.RULE_distinct_formula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDistinct_formula" ):
                listener.enterDistinct_formula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDistinct_formula" ):
                listener.exitDistinct_formula(self)




    def distinct_formula(self):

        localctx = MyGrammar2Parser.Distinct_formulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_distinct_formula)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(MyGrammar2Parser.T__0)
            self.state = 71
            self.match(MyGrammar2Parser.T__5)
            self.state = 72
            self.values()
            self.state = 73
            self.values()
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21 or _la==22:
                self.state = 74
                self.values()
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 80
            self.match(MyGrammar2Parser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comp_formulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comp(self):
            return self.getTypedRuleContext(MyGrammar2Parser.CompContext,0)


        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammar2Parser.FormulaContext)
            else:
                return self.getTypedRuleContext(MyGrammar2Parser.FormulaContext,i)


        def getRuleIndex(self):
            return MyGrammar2Parser.RULE_comp_formula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComp_formula" ):
                listener.enterComp_formula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComp_formula" ):
                listener.exitComp_formula(self)




    def comp_formula(self):

        localctx = MyGrammar2Parser.Comp_formulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_comp_formula)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(MyGrammar2Parser.T__0)
            self.state = 83
            self.comp()
            self.state = 84
            self.formula()
            self.state = 85
            self.formula()
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 6291458) != 0:
                self.state = 86
                self.formula()
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 92
            self.match(MyGrammar2Parser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Operation_dormulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operation(self):
            return self.getTypedRuleContext(MyGrammar2Parser.OperationContext,0)


        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(MyGrammar2Parser.NUMBER)
            else:
                return self.getToken(MyGrammar2Parser.NUMBER, i)

        def getRuleIndex(self):
            return MyGrammar2Parser.RULE_operation_dormula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperation_dormula" ):
                listener.enterOperation_dormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperation_dormula" ):
                listener.exitOperation_dormula(self)




    def operation_dormula(self):

        localctx = MyGrammar2Parser.Operation_dormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_operation_dormula)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(MyGrammar2Parser.T__0)
            self.state = 95
            self.operation()
            self.state = 96
            self.match(MyGrammar2Parser.NUMBER)
            self.state = 97
            self.match(MyGrammar2Parser.NUMBER)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 98
                self.match(MyGrammar2Parser.NUMBER)
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 104
            self.match(MyGrammar2Parser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValuesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MyGrammar2Parser.ID, 0)

        def NUMBER(self):
            return self.getToken(MyGrammar2Parser.NUMBER, 0)

        def getRuleIndex(self):
            return MyGrammar2Parser.RULE_values

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValues" ):
                listener.enterValues(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValues" ):
                listener.exitValues(self)




    def values(self):

        localctx = MyGrammar2Parser.ValuesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_values)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            _la = self._input.LA(1)
            if not(_la==21 or _la==22):
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


    class FormulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def distinct_formula(self):
            return self.getTypedRuleContext(MyGrammar2Parser.Distinct_formulaContext,0)


        def comp_formula(self):
            return self.getTypedRuleContext(MyGrammar2Parser.Comp_formulaContext,0)


        def comparator(self):
            return self.getTypedRuleContext(MyGrammar2Parser.ComparatorContext,0)


        def values(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammar2Parser.ValuesContext)
            else:
                return self.getTypedRuleContext(MyGrammar2Parser.ValuesContext,i)


        def operation_dormula(self):
            return self.getTypedRuleContext(MyGrammar2Parser.Operation_dormulaContext,0)


        def equal(self):
            return self.getTypedRuleContext(MyGrammar2Parser.EqualContext,0)


        def ID(self):
            return self.getToken(MyGrammar2Parser.ID, 0)

        def formula(self):
            return self.getTypedRuleContext(MyGrammar2Parser.FormulaContext,0)


        def getRuleIndex(self):
            return MyGrammar2Parser.RULE_formula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormula" ):
                listener.enterFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormula" ):
                listener.exitFormula(self)




    def formula(self):

        localctx = MyGrammar2Parser.FormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_formula)
        try:
            self.state = 124
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                self.distinct_formula()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 109
                self.comp_formula()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 110
                self.match(MyGrammar2Parser.T__0)
                self.state = 111
                self.comparator()
                self.state = 112
                self.values()
                self.state = 113
                self.values()
                self.state = 114
                self.match(MyGrammar2Parser.T__2)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 116
                self.operation_dormula()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 117
                self.match(MyGrammar2Parser.T__0)
                self.state = 118
                self.equal()
                self.state = 119
                self.match(MyGrammar2Parser.ID)
                self.state = 120
                self.formula()
                self.state = 121
                self.match(MyGrammar2Parser.T__2)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 123
                self.values()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyGrammar2Parser.RULE_comparator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparator" ):
                listener.enterComparator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparator" ):
                listener.exitComparator(self)




    def comparator(self):

        localctx = MyGrammar2Parser.ComparatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_comparator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 1920) != 0):
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


    class EqualContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyGrammar2Parser.RULE_equal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqual" ):
                listener.enterEqual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqual" ):
                listener.exitEqual(self)




    def equal(self):

        localctx = MyGrammar2Parser.EqualContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_equal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(MyGrammar2Parser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyGrammar2Parser.RULE_operation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperation" ):
                listener.enterOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperation" ):
                listener.exitOperation(self)




    def operation(self):

        localctx = MyGrammar2Parser.OperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_operation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 61440) != 0):
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


    class CompContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyGrammar2Parser.RULE_comp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComp" ):
                listener.enterComp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComp" ):
                listener.exitComp(self)




    def comp(self):

        localctx = MyGrammar2Parser.CompContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_comp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            _la = self._input.LA(1)
            if not(_la==16 or _la==17):
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


    class Check_satContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyGrammar2Parser.RULE_check_sat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCheck_sat" ):
                listener.enterCheck_sat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCheck_sat" ):
                listener.exitCheck_sat(self)




    def check_sat(self):

        localctx = MyGrammar2Parser.Check_satContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_check_sat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(MyGrammar2Parser.T__0)
            self.state = 135
            self.match(MyGrammar2Parser.T__17)
            self.state = 136
            self.match(MyGrammar2Parser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Get_modelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyGrammar2Parser.RULE_get_model

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGet_model" ):
                listener.enterGet_model(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGet_model" ):
                listener.exitGet_model(self)




    def get_model(self):

        localctx = MyGrammar2Parser.Get_modelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_get_model)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(MyGrammar2Parser.T__0)
            self.state = 139
            self.match(MyGrammar2Parser.T__18)
            self.state = 140
            self.match(MyGrammar2Parser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






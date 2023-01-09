# Generated from MyGrammar.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyGrammarParser import MyGrammarParser
else:
    from MyGrammarParser import MyGrammarParser

# This class defines a complete listener for a parse tree produced by MyGrammarParser.
class MyGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by MyGrammarParser#prog.
    def enterProg(self, ctx:MyGrammarParser.ProgContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#prog.
    def exitProg(self, ctx:MyGrammarParser.ProgContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#function_declaration.
    def enterFunction_declaration(self, ctx:MyGrammarParser.Function_declarationContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#function_declaration.
    def exitFunction_declaration(self, ctx:MyGrammarParser.Function_declarationContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#parameter_declaration.
    def enterParameter_declaration(self, ctx:MyGrammarParser.Parameter_declarationContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#parameter_declaration.
    def exitParameter_declaration(self, ctx:MyGrammarParser.Parameter_declarationContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#block.
    def enterBlock(self, ctx:MyGrammarParser.BlockContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#block.
    def exitBlock(self, ctx:MyGrammarParser.BlockContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#statement.
    def enterStatement(self, ctx:MyGrammarParser.StatementContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#statement.
    def exitStatement(self, ctx:MyGrammarParser.StatementContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#function_call.
    def enterFunction_call(self, ctx:MyGrammarParser.Function_callContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#function_call.
    def exitFunction_call(self, ctx:MyGrammarParser.Function_callContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#print_statement.
    def enterPrint_statement(self, ctx:MyGrammarParser.Print_statementContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#print_statement.
    def exitPrint_statement(self, ctx:MyGrammarParser.Print_statementContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#return_statement.
    def enterReturn_statement(self, ctx:MyGrammarParser.Return_statementContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#return_statement.
    def exitReturn_statement(self, ctx:MyGrammarParser.Return_statementContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#assignment.
    def enterAssignment(self, ctx:MyGrammarParser.AssignmentContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#assignment.
    def exitAssignment(self, ctx:MyGrammarParser.AssignmentContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#if_statement.
    def enterIf_statement(self, ctx:MyGrammarParser.If_statementContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#if_statement.
    def exitIf_statement(self, ctx:MyGrammarParser.If_statementContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#while_statement.
    def enterWhile_statement(self, ctx:MyGrammarParser.While_statementContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#while_statement.
    def exitWhile_statement(self, ctx:MyGrammarParser.While_statementContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#expression.
    def enterExpression(self, ctx:MyGrammarParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#expression.
    def exitExpression(self, ctx:MyGrammarParser.ExpressionContext):
        pass



del MyGrammarParser
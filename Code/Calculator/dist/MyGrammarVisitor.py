# Generated from MyGrammar.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyGrammarParser import MyGrammarParser
else:
    from MyGrammarParser import MyGrammarParser

# This class defines a complete generic visitor for a parse tree produced by MyGrammarParser.

class MyGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MyGrammarParser#prog.
    def visitProg(self, ctx:MyGrammarParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#single_statement.
    def visitSingle_statement(self, ctx:MyGrammarParser.Single_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#function_declaration.
    def visitFunction_declaration(self, ctx:MyGrammarParser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#parameter_declaration.
    def visitParameter_declaration(self, ctx:MyGrammarParser.Parameter_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#block.
    def visitBlock(self, ctx:MyGrammarParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#statement.
    def visitStatement(self, ctx:MyGrammarParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#function_call.
    def visitFunction_call(self, ctx:MyGrammarParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#print_statement.
    def visitPrint_statement(self, ctx:MyGrammarParser.Print_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#return_statement.
    def visitReturn_statement(self, ctx:MyGrammarParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#assignment.
    def visitAssignment(self, ctx:MyGrammarParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#if_statement.
    def visitIf_statement(self, ctx:MyGrammarParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#while_statement.
    def visitWhile_statement(self, ctx:MyGrammarParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#calculation.
    def visitCalculation(self, ctx:MyGrammarParser.CalculationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#parens.
    def visitParens(self, ctx:MyGrammarParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#bool.
    def visitBool(self, ctx:MyGrammarParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#string.
    def visitString(self, ctx:MyGrammarParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#id.
    def visitId(self, ctx:MyGrammarParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#float.
    def visitFloat(self, ctx:MyGrammarParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#func_call.
    def visitFunc_call(self, ctx:MyGrammarParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#int.
    def visitInt(self, ctx:MyGrammarParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#type.
    def visitType(self, ctx:MyGrammarParser.TypeContext):
        return self.visitChildren(ctx)



del MyGrammarParser
from antlr4 import *
from dist.MyGrammarLexer import MyGrammarLexer
from dist.MyGrammarParser import MyGrammarParser
from dist.MyGrammarVisitor import MyGrammarVisitor



functions = {}
variables = {} 

class Function:
    def __init__(self, name, block):
        self.name = name
        self.parameters = []
        self.block = block
        
    def add_parameter(self, param_name):
        self.parameters.append(param_name)

    def get_parameters(self):
        return self.parameters

class Evaluate(MyGrammarVisitor):
    def visitFunction_declaration(self, ctx:MyGrammarParser.Function_declarationContext):
        name = ctx.ID().getText()
        block = ctx.block()

        func = Function(name, block)

        if ctx.parameter_declaration():
            for param in ctx.parameter_declaration():
                param_name = self.visit(param)
                func.add_parameter(param_name)
                
        functions[name] = func

    def visitParameter_declaration(self, ctx:MyGrammarParser.Parameter_declarationContext):
        return ctx.ID().getText()

    def visitBlock(self, ctx:MyGrammarParser.BlockContext):
        for stmt in ctx.statement():
            self.visit(stmt)

    def visitSingle_statement(self, ctx:MyGrammarParser.Single_statementContext):
        if ctx.function_declaration():
            self.visit(ctx.function_declaration())

        elif ctx.function_call():
            self.visit(ctx.function_call())

        elif ctx.assignment():
            self.visit(ctx.assignment())

        elif ctx.if_statement():
            self.visit(ctx.if_statement())

        elif ctx.while_statement():
            self.visit(ctx.while_statement())

        elif ctx.print_statement():
            self.visit(ctx.print_statement())

    def visitStatement(self, ctx:MyGrammarParser.StatementContext):
        if ctx.function_call():
            self.visit(ctx.function_call())

        elif ctx.return_statement():
            self.visit(ctx.return_statement())

        elif ctx.assignment():
            self.visit(ctx.assignment())

        elif ctx.if_statement():
            self.visit(ctx.if_statement())

        elif ctx.while_statement():
            self.visit(ctx.while_statement())

        elif ctx.print_statement():
            self.visit(ctx.print_statement())
    
    def visitFunction_call(self, ctx:MyGrammarParser.Function_callContext):
        name = ctx.ID().getText()
        func = {}
        parameters = []
        i = 0

        if name in functions:
            func = functions[name]

        for param in func.get_parameters():
            parameters.append(param)

        if ctx.expression():
            for expr in ctx.expression():
                variables[parameters[i]] = int(self.visit(expr))
                i += 1

        return self.visit(func.block)

    def visitPrint_statement(self, ctx:MyGrammarParser.Print_statementContext):
        value = self.visit(ctx.expression())
        print(value)

    def visitReturn_statement(self, ctx:MyGrammarParser.Return_statementContext):
        expr = self.visit(ctx.expression())
        print(expr)
        return expr
    
    def visitAssignment(self, ctx:MyGrammarParser.AssignmentContext):
        name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        variables[name] = value

    def visitIf_statement(self, ctx:MyGrammarParser.If_statementContext):
        condition = self.visit(ctx.expression())
        if condition == True:
            self.visit(ctx.statement(0))
        else:
            self.visit(ctx.statement(1))


    def visitWhile_statement(self, ctx:MyGrammarParser.While_statementContext):
        condition = self.visit(ctx.expression())
        while condition == True:
            self.visit(ctx.statement())

    def visitExpression(self, ctx:MyGrammarParser.ExpressionContext):
        if ctx.ID():
            return ctx.ID().getText()
        elif ctx.INT():
            return ctx.INT().getText()
        elif ctx.FLOAT():
            return ctx.FLOAT().getText()
        elif ctx.BOOL():
            return ctx.BOOL().getText()
        elif ctx.STRING():
            return ctx.STRING().getText()
        elif ctx.function_call():
            return self.visit(ctx.function_call())
        elif ctx.expression():
            values = []
            for expr in ctx.expression():
                if type(self.visit(expr)) == str:
                    values.append(variables[self.visit(expr)])
                else:    
                    values.append(int(self.visit(expr)))
            if ctx.PLUS():
                return values[0]+values[1]
            elif ctx.MINUS():
                return values[0] - sum(values[1:])
            elif ctx.MULTIPLY():
                result = 1
                for val in values:
                    result *= val
                return result
            elif ctx.DIVIDE():
                result = values[0]
                for val in values[1:]:
                    result /= val
                return result
            elif ctx.MODULO():
                result = values[0]
                for val in values[1:]:
                    result %= val
                return result
            elif ctx.EQUALS():
                return values[0] == values[1]
            elif ctx.NOT_EQUALS():
                return values[0] != values[1]
            elif ctx.GREATER_THAN():
                return values[0] > values[1]
            elif ctx.LESS_THAN():
                return values[0] < values[1]
            elif ctx.GREATER_THAN_EQUALS():
                return values[0] >= values[1]
            elif ctx.LESS_THAN_EQUALS():
                return values[0] <= values[1]
            elif ctx.AND():
                result = True
                for val in values:
                    result = result and val
                return result
            elif ctx.OR():
                result = False
                for val in values:
                    result = result or val
                return result
            else:
                return None

    def visitType(self, ctx:MyGrammarParser.TypeContext):
        return ctx.getText()

def main():
    # lex the input string
    lexer = MyGrammarLexer(FileStream("input.txt"))
    tokens = CommonTokenStream(lexer)

    # parse the tokens
    parser = MyGrammarParser(tokens)
    tree = parser.prog()

    # create a visitor and visit the parse tree
    visitor = Evaluate()
    symbol_table = visitor.visit(tree)

    # print the symbol table
    print(symbol_table)

if __name__ == '__main__':
    main()

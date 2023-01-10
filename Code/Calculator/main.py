# antlr -Dlanguage=Python3 MyGrammar.g4 -visitor -o dist 
from antlr4 import *
from dist.MyGrammarLexer import MyGrammarLexer
from dist.MyGrammarParser import MyGrammarParser
from dist.MyGrammarVisitor import MyGrammarVisitor



functions = {}
variables = {} 

class Function:
    def __init__(self, name, return_type, block):
        self.name = name
        self.return_type = return_type
        self.parameters = []
        self.block = block
        
    def add_parameter(self, param):
        self.parameters.append(param)

class Variable:
    def __init__(self, return_type, name, value):
        self.name = name
        self.return_type = return_type
        self.value = value

class Evaluate(MyGrammarVisitor):
    def visitFunction_declaration(self, ctx:MyGrammarParser.Function_declarationContext):
        name = ctx.ID().getText()
        return_type = ctx.type_().getText()
        block = ctx.block()

        func = Function(name, return_type, block)

        if ctx.parameter_declaration():
            for param in ctx.parameter_declaration():
                param_type = self.visit(param)[0]
                param_name = self.visit(param)[1]
                func.add_parameter((param_type, param_name))
                
        functions[name] = func

    def visitParameter_declaration(self, ctx:MyGrammarParser.Parameter_declarationContext):
        parameter = (ctx.type_().getText(), ctx.ID().getText())
        return parameter

    def visitBlock(self, ctx:MyGrammarParser.BlockContext):
        for stmt in ctx.statement():
            return self.visit(stmt)

    def visitSingle_statement(self, ctx:MyGrammarParser.Single_statementContext):
        if ctx.function_declaration():
            return self.visit(ctx.function_declaration())

        elif ctx.function_call():
            return self.visit(ctx.function_call())

        elif ctx.assignment():
            return self.visit(ctx.assignment())

        elif ctx.if_statement():
            return self.visit(ctx.if_statement())

        elif ctx.while_statement():
            return self.visit(ctx.while_statement())

        elif ctx.print_statement():
            return self.visit(ctx.print_statement())

    def visitStatement(self, ctx:MyGrammarParser.StatementContext):
        if ctx.function_call():
            return self.visit(ctx.function_call())

        elif ctx.return_statement():
            return self.visit(ctx.return_statement())

        elif ctx.assignment():
            return self.visit(ctx.assignment())

        elif ctx.if_statement():
            return self.visit(ctx.if_statement())

        elif ctx.while_statement():
            return self.visit(ctx.while_statement())

        elif ctx.print_statement():
            return self.visit(ctx.print_statement())
    
    def visitFunction_call(self, ctx:MyGrammarParser.Function_callContext):
        name = ctx.ID().getText()
        func = {}
        parameters = []
        i = 0

        if name in functions:
            func = functions[name]

        parameters = func.parameters

        if ctx.expression():
            for expr in ctx.expression():
                value = self.visit(expr)
                if value.isnumeric():
                    if parameters[i][0] == 'int':
                        number = Variable(parameters[i][0], parameters[i][1], int(value))
                    else:
                        number = Variable(parameters[i][0], parameters[i][1], float(value))
                    variables[parameters[i][1]] = number
                else:
                    if value in variables:
                        if parameters[i][0] == 'int':
                            number = Variable(parameters[i][0], parameters[i][1], int(variables[value].value))
                        else:
                            number = Variable(parameters[i][0], parameters[i][1], float(variables[value].value))
                        variables[parameters[i][1]] = number
                    else:
                        print("Variable " + str(value) + " dont have any number")
                        return

                i += 1

        if func.return_type == 'int':
            return int(self.visit(func.block))
        elif func.return_type == 'float':
            return float(self.visit(func.block))
        else:
            return None

    def visitPrint_statement(self, ctx:MyGrammarParser.Print_statementContext):
        value = self.visit(ctx.expression())
        print(value)

    def visitReturn_statement(self, ctx:MyGrammarParser.Return_statementContext):
        expr = self.visit(ctx.expression())
        return expr
    
    def visitAssignment(self, ctx:MyGrammarParser.AssignmentContext):
        var_name = ctx.ID().getText()
        var_type = ctx.type_().getText()
        number = None
        if ctx.expression():
            value = self.visit(ctx.expression())
            if var_type == 'int':
                number = Variable(var_type, var_name, int(value))
            else:
                number = Variable(var_type, var_name, float(value))
        else:
            number = None
        variables[var_name] = number

    def visitIf_statement(self, ctx:MyGrammarParser.If_statementContext):
        condition = self.visit(ctx.expression())
        if condition == True:
            return self.visit(ctx.statement(0))
        else:
            return self.visit(ctx.statement(1))


    def visitWhile_statement(self, ctx:MyGrammarParser.While_statementContext):
        condition = self.visit(ctx.expression())
        while condition == True:
            self.visit(ctx.statement())

    def visitExpression(self, ctx:MyGrammarParser.ExpressionContext):
        if ctx.ID():
            value = ctx.ID().getText()
            if value in variables:
                if variables[value] == None:
                    return None
                else:    
                    return variables[value].name
            else:
                return value 
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
                value = self.visit(expr)
                if not str(value).isnumeric() and type(value) != float:
                    if value in variables:
                        var = variables[value]
                        if var.return_type == 'int':
                            values.append(int(var.value))
                        else:
                            values.append(float(var.value))
                    else:
                        print("No variable found with " + str(value) + " id")
                        return
                elif value == None:
                    print(str(value) + " variable is not assigned with numbers")
                    return
                else:    
                    values.append(value)
            if ctx.PLUS():
                return values[0] + values[1]
            elif ctx.MINUS():
                return values[0] - values[1]
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
    visitor.visit(tree)

if __name__ == '__main__':
    main()

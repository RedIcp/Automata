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
        count = 0
        for stmt in ctx.statement():
            count += 1
            if count == len(ctx.statement()):
                return self.visit(stmt)
            else:
                self.visit(stmt)

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
                if str(value).replace('.', '', 1).isdigit():
                    if parameters[i][0] == 'int':
                        number = Variable(parameters[i][0], parameters[i][1], int(float(value)))
                    else:
                        number = Variable(parameters[i][0], parameters[i][1], float(value))
                    variables[parameters[i][1]] = number
                else:
                    if value in variables:
                        if parameters[i][0] == 'int':
                            number = Variable(parameters[i][0], parameters[i][1], int(float(variables[value].value)))
                        else:
                            number = Variable(parameters[i][0], parameters[i][1], float(variables[value].value))
                        variables[parameters[i][1]] = number
                    else:
                        print("Variable " + str(value) + " dont have any number")
                        return

                i += 1

        if func.return_type == 'int':
            v = int(float(self.visit(func.block)))
        elif func.return_type == 'float':
            v = float(self.visit(func.block))
        else:
            v = None

        for i, param in enumerate(func.parameters):
            del variables[parameters[i][1]]
        
        return v

    def visitPrint_statement(self, ctx:MyGrammarParser.Print_statementContext):
        value = self.visit(ctx.expression())
        print(value)

    def visitReturn_statement(self, ctx:MyGrammarParser.Return_statementContext):
        expr = self.visit(ctx.expression())
        return expr
    
    def visitAssignment(self, ctx:MyGrammarParser.AssignmentContext):
        var_name = ctx.ID().getText()
        var_type = ""
        number = None
        if not ctx.type_():
            if var_name not in variables:
                print("no variable stored in that name")
                return
        else:
            var_type = ctx.type_().getText()
        if ctx.expression():
            value = self.visit(ctx.expression())

            if var_type == "":
                number = variables[var_name]
                if number.return_type == 'int':
                    number.value = int(float(value))
                else:
                    number.value = float(value)
            elif var_type == 'int':
                number = Variable(var_type, var_name, int(float(value)))
            else:
                number = Variable(var_type, var_name, float(value))
        else:
            number = None
        variables[var_name] = number

    def visitIf_statement(self, ctx:MyGrammarParser.If_statementContext):
        condition = self.visit(ctx.expression())
        if condition == True:
            return self.visit(ctx.block(0))
        else:
            return self.visit(ctx.block(1))


    def visitWhile_statement(self, ctx:MyGrammarParser.While_statementContext):
        condition = self.visit(ctx.expression())
        while condition == True:
            self.visit(ctx.block())
            condition = self.visit(ctx.expression())

    def visitCalculation(self, ctx:MyGrammarParser.CalculationContext):
        l = self.visit(ctx.expression(0))
        r = self.visit(ctx.expression(1))
        if not str(l).replace('.', '', 1).isdigit():
            if l in variables:
                l = variables[l]
                if l.return_type == 'int':
                    l = int(float(l.value))
                else:
                    l = float(l.value)
            else:
                print("No variable found with " + str(l) + " id")
                return
        elif l == None:
            print(str(l) + " variable is not assigned with numbers")
            return
        else:
            l = float(l)

        if not str(r).replace('.', '', 1).isdigit():
            if r in variables:
                r = variables[r]
                if r.return_type == 'int':
                    r = int(float(r.value))
                else:
                    r = float(r.value)
            else:
                print("No variable found with " + str(r) + " id")
                return
        elif r == None:
            print(str(r) + " variable is not assigned with numbers")
            return
        else:
            r = float(r)
            
        if ctx.PLUS():
            return l + r
        elif ctx.MINUS():
            return l - r
        elif ctx.MULTIPLY():
            return l * r
        elif ctx.DIVIDE():
            return l / r
        elif ctx.MODULO():
            return l % r
        elif ctx.EQUALS():
            return l == r
        elif ctx.NOT_EQUALS():
            return l != r
        elif ctx.GREATER_THAN():
            return l > r
        elif ctx.LESS_THAN():
            return l < r
        elif ctx.GREATER_THAN_EQUALS():
            return l >= r
        elif ctx.LESS_THAN_EQUALS():
            return l <= r
        elif ctx.AND():
            return l and r
        elif ctx.OR():
            return l or r
        else:
            return None    
        

    def visitParens(self, ctx:MyGrammarParser.ParensContext):
        return self.visit(ctx.expression())

    def visitBool(self, ctx:MyGrammarParser.BoolContext):
        return ctx.BOOL().getText()

    def visitString(self, ctx:MyGrammarParser.StringContext):
        return ctx.STRING().getText()

    def visitId(self, ctx:MyGrammarParser.IdContext):
        value = ctx.ID().getText()
        if value in variables:
            if variables[value] == None:
                return None
            else:    
                return variables[value].value
        else:
            return value 

    def visitFloat(self, ctx:MyGrammarParser.FloatContext):
        return ctx.FLOAT().getText()

    def visitFunc_call(self, ctx:MyGrammarParser.Func_callContext):
        return self.visit(ctx.function_call())

    def visitInt(self, ctx:MyGrammarParser.IntContext):
        return ctx.INT().getText()

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

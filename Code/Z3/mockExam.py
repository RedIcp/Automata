# antlr -Dlanguage=Python3 MyGrammar2.g4 -o dist 
from antlr4 import *
from dist.MyGrammar2Lexer import MyGrammar2Lexer
from dist.MyGrammar2Parser import MyGrammar2Parser
from dist.MyGrammar2Listener import MyGrammar2Listener

class Evaluate(MyGrammar2Listener):
    def __init__(self):
        self.variables = {}
        
    def enterDeclare_const(self, ctx:MyGrammar2Parser.Declare_constContext):
        var_name = ctx.ID().getText()
        value = int(ctx.NUMBER().getText())
        if var_name in self.variables:
            print('*** ERROR in define-const: variable ' + str(var_name) + ' redefined ***')
        else:
            print('INTEGER: ' + var_name +' = ' + str(value))
            self.variables[var_name] = value

    def enterDeclare_fun(self, ctx:MyGrammar2Parser.Declare_funContext):
        var_name = ctx.ID().getText()
        if var_name in self.variables:
            print('*** ERROR in define-fun: variable ' + str(var_name) + ' redefined ***')
        elif ctx.INT_W():
            print('FUNCTION: ' + var_name + ' #par= ' + str(len(ctx.INT_W())-1))

    def enterAssert_cmd(self, ctx:MyGrammar2Parser.Assert_cmdContext):
        formula = self.evaluate_formula(ctx.formula())
        print("ASSERT: " + str(formula))
    
    def evaluate_formula(self, ctx:MyGrammar2Parser.FormulaContext):
        if ctx.distinct_formula():
            # Handle distinct formula
            values = [self.evaluate_values(v) for v in ctx.distinct_formula().values()]
            return "DISTINCT: " + str(values)
        elif ctx.comp_formula():
            # Handle compound formula
            values = [self.evaluate_formula(f) for f in ctx.comp_formula().formula()]
            if ctx.comp_formula().comp().getText() == 'and':
                string = "("
                for i, value in enumerate(values):
                    if i == 0:
                        string += '(' + str(value) + ")"
                    else:
                        string += ' && (' + str(value) + ")"

                return string
            else:
                string = "("
                for i, value in enumerate(values):
                    if i == 0:
                        string += '(' + str(value) + ")"
                    else:
                        string += ' || (' + str(value) + ")"

                return string
        elif ctx.comparator():
            # Handle comparator formula
            left = self.evaluate_values(ctx.values(0))
            right = self.evaluate_values(ctx.values(1))
            comparator = ctx.comparator().getText()
            if comparator == '>=':
                return str(left) + ' >= ' + str(right)
            elif comparator == '<=':
                return str(left) + ' <= ' + str(right)
            elif comparator == '<':
                return str(left) + ' < ' + str(right)
            elif comparator == '>':
                return str(left) + ' > ' + str(right)
        elif ctx.operation_dormula():
            symbol = ctx.operation_dormula().operation().getText()
            #values = [self.evaluate_values(v) for v in ctx.operation_dormula().NUMBER()]
            values = []
            string = '('
            for i, num in enumerate(ctx.operation_dormula().NUMBER()):
                value = num.getText()
                values.append(value)
                if i+1 < len(ctx.operation_dormula().NUMBER()):
                    string += value + " " + symbol + " "
                else:
                    string += value + ")"

            return string
            # x = (12 symbol 12456 symbol 67)
        elif ctx.equal():
            var_name = ctx.ID().getText()
            values = self.evaluate_formula(ctx.formula())
            print(values)
            string = '( ' + var_name + ' == ( ' + str(values)

            #  (aa == (x)
            return '( ' + var_name + ' == ( ' + values + '))'
        else:
            # Handle values
            return self.evaluate_values(ctx.values())

    def evaluate_values(self, ctx:MyGrammar2Parser.ValuesContext):
        if ctx.ID():
            # Handle identifier
            id_text = ctx.ID().getText()
            if id_text in self.variables:
                # Return a function call if the identifier is a declared function
                return self.variables[id_text]
            else:
                print("*** ERROR in assert: variable " + str(id_text) + " undefined ***")
        elif ctx.NUMBER():
            # Handle number
            return ctx.NUMBER().getText()

def main():
    input_stream = FileStream("test.txt")
    lexer = MyGrammar2Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MyGrammar2Parser(stream)
    tree = parser.program()
    listener = Evaluate()
    walker = ParseTreeWalker().walk(listener, tree)
    return walker

main()
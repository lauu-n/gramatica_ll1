import math
import os
import sys

directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_generados = os.path.join(directorio_actual, "archivos_generados")
if ruta_generados not in sys.path:
    sys.path.insert(0, ruta_generados)

from gramaticaParser import gramaticaParser
from gramaticaVisitor import gramaticaVisitor

class EvalVisitor(gramaticaVisitor):

    def __init__(self, silent=False):
        # Tabla de símbolos para almacenar las variables en memoria
        self.variables = {}
        self.outputs = []
        self.silent = silent

    def emit(self, texto):
        self.outputs.append(texto)
        if not self.silent:
            print(texto)

    # Visita la regla principal 'program'
    def visitPrograma(self, ctx: gramaticaParser.ProgramaContext):
        return self.visitChildren(ctx)

    # Visita una asignación: ID '=' expr ';'
    def visitAsignacion(self, ctx: gramaticaParser.AsignacionContext):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        if value is not None:
            self.variables[var_name] = value
            self.emit(f"{var_name} = {value}")
        return value

    # Visita una expresión suelta con punto y coma: expr ';'
    def visitSentenciaExpr(self, ctx: gramaticaParser.SentenciaExprContext):
        value = self.visit(ctx.expr())
        if value is not None:
            self.emit(f"Resultado: {value}")
        return value

    # Visita la regla expr: term expr_prima
    def visitReglaExpr(self, ctx: gramaticaParser.ReglaExprContext):
        val = self.visit(ctx.term())
        return self.eval_expr_prima(val, ctx.expr_prima())

    # Evaluación de suma y resta (asociatividad por la izquierda)
    def eval_expr_prima(self, acc, ctx: gramaticaParser.Expr_primaContext):
        if ctx is None or isinstance(ctx, gramaticaParser.VacioExprContext) or ctx.getChildCount() == 0:
            return acc
        op = ctx.op.text
        term_val = self.visit(ctx.term())
        nuevo_acc = (acc + term_val) if op == "+" else (acc - term_val)
        return self.eval_expr_prima(nuevo_acc, ctx.expr_prima())

    # Visita la regla term: factor term_prima
    def visitReglaTerm(self, ctx: gramaticaParser.ReglaTermContext):
        val = self.visit(ctx.factor())
        return self.eval_term_prima(val, ctx.term_prima())

    # Evaluación de multiplicación, división y módulo (asociatividad por la izquierda)
    def eval_term_prima(self, acc, ctx: gramaticaParser.Term_primaContext):
        if ctx is None or isinstance(ctx, gramaticaParser.VacioTermContext) or ctx.getChildCount() == 0:
            return acc
        op = ctx.op.text
        factor_val = self.visit(ctx.factor())

        if op == "*":
            nuevo_acc = acc * factor_val
        elif op == "/":
            if factor_val == 0:
                raise ZeroDivisionError(f"Error Semántico [Línea {ctx.start.line}]: No se puede dividir entre cero.")
            nuevo_acc = acc / factor_val
        elif op == "%":
            if factor_val == 0:
                raise ZeroDivisionError(f"Error Semántico [Línea {ctx.start.line}]: Operación módulo (%) entre cero no permitida.")
            nuevo_acc = acc % factor_val
        else:
            nuevo_acc = acc

        return self.eval_term_prima(nuevo_acc, ctx.term_prima())

    # Visita funciones trigonométricas y matemáticas con validación de valores indefinidos
    def visitFuncionTrig(self, ctx: gramaticaParser.FuncionTrigContext):
        func_name = ctx.FUNC().getText().lower()
        val = self.visit(ctx.expr())

        if val is None:
            return None

        if func_name in ("sin", "sen"):
            return math.sin(val)
        elif func_name == "cos":
            return math.cos(val)
        elif func_name == "tan":
            # Si el coseno está muy cercano a 0 (ej. pi/2), la tangente no existe
            if abs(math.cos(val)) < 1e-12:
                raise ValueError(f"Error Semántico [Línea {ctx.start.line}]: tan({val}) está indefinida (asíntota/indeterminación).")
            return math.tan(val)
        elif func_name == "abs":
            return abs(val)
        else:
            raise ValueError(f"Error Semántico [Línea {ctx.start.line}]: Función no soportada: {func_name}")

    # Visita uso de una variable con control de variables no declaradas
    def visitVariable(self, ctx: gramaticaParser.VariableContext):
        var_name = ctx.ID().getText()
        if var_name in self.variables:
            return self.variables[var_name]
        else:
            raise NameError(f"Error Semántico [Línea {ctx.start.line}]: La variable '{var_name}' no está definida.")

    # Visita un número: NUM
    def visitNumero(self, ctx: gramaticaParser.NumeroContext):
        text = ctx.NUM().getText()
        return float(text) if "." in text else int(text)

    # Visita expresión con paréntesis: '(' expr ')'
    def visitParentesis(self, ctx: gramaticaParser.ParentesisContext):
        return self.visit(ctx.expr())

    # Visita unario (+ o -)
    def visitUnario(self, ctx: gramaticaParser.UnarioContext):
        val = self.visit(ctx.factor())
        return val if ctx.op.text == "+" else -val
# Generated from gramatica.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .gramaticaParser import gramaticaParser
else:
    from gramaticaParser import gramaticaParser

# This class defines a complete generic visitor for a parse tree produced by gramaticaParser.

class gramaticaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by gramaticaParser#Programa.
    def visitPrograma(self, ctx:gramaticaParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Asignacion.
    def visitAsignacion(self, ctx:gramaticaParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#SentenciaExpr.
    def visitSentenciaExpr(self, ctx:gramaticaParser.SentenciaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#ReglaExpr.
    def visitReglaExpr(self, ctx:gramaticaParser.ReglaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#OpSumaResta.
    def visitOpSumaResta(self, ctx:gramaticaParser.OpSumaRestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#VacioExpr.
    def visitVacioExpr(self, ctx:gramaticaParser.VacioExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#ReglaTerm.
    def visitReglaTerm(self, ctx:gramaticaParser.ReglaTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#OpMulDivMod.
    def visitOpMulDivMod(self, ctx:gramaticaParser.OpMulDivModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#VacioTerm.
    def visitVacioTerm(self, ctx:gramaticaParser.VacioTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#FuncionTrig.
    def visitFuncionTrig(self, ctx:gramaticaParser.FuncionTrigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Variable.
    def visitVariable(self, ctx:gramaticaParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Numero.
    def visitNumero(self, ctx:gramaticaParser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Parentesis.
    def visitParentesis(self, ctx:gramaticaParser.ParentesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Unario.
    def visitUnario(self, ctx:gramaticaParser.UnarioContext):
        return self.visitChildren(ctx)



del gramaticaParser
# Generated from gramatica.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .gramaticaParser import gramaticaParser
else:
    from gramaticaParser import gramaticaParser

# This class defines a complete listener for a parse tree produced by gramaticaParser.
class gramaticaListener(ParseTreeListener):

    # Enter a parse tree produced by gramaticaParser#Programa.
    def enterPrograma(self, ctx:gramaticaParser.ProgramaContext):
        pass

    # Exit a parse tree produced by gramaticaParser#Programa.
    def exitPrograma(self, ctx:gramaticaParser.ProgramaContext):
        pass


    # Enter a parse tree produced by gramaticaParser#Asignacion.
    def enterAsignacion(self, ctx:gramaticaParser.AsignacionContext):
        pass

    # Exit a parse tree produced by gramaticaParser#Asignacion.
    def exitAsignacion(self, ctx:gramaticaParser.AsignacionContext):
        pass


    # Enter a parse tree produced by gramaticaParser#SentenciaExpr.
    def enterSentenciaExpr(self, ctx:gramaticaParser.SentenciaExprContext):
        pass

    # Exit a parse tree produced by gramaticaParser#SentenciaExpr.
    def exitSentenciaExpr(self, ctx:gramaticaParser.SentenciaExprContext):
        pass


    # Enter a parse tree produced by gramaticaParser#ReglaExpr.
    def enterReglaExpr(self, ctx:gramaticaParser.ReglaExprContext):
        pass

    # Exit a parse tree produced by gramaticaParser#ReglaExpr.
    def exitReglaExpr(self, ctx:gramaticaParser.ReglaExprContext):
        pass


    # Enter a parse tree produced by gramaticaParser#OpSumaResta.
    def enterOpSumaResta(self, ctx:gramaticaParser.OpSumaRestaContext):
        pass

    # Exit a parse tree produced by gramaticaParser#OpSumaResta.
    def exitOpSumaResta(self, ctx:gramaticaParser.OpSumaRestaContext):
        pass


    # Enter a parse tree produced by gramaticaParser#VacioExpr.
    def enterVacioExpr(self, ctx:gramaticaParser.VacioExprContext):
        pass

    # Exit a parse tree produced by gramaticaParser#VacioExpr.
    def exitVacioExpr(self, ctx:gramaticaParser.VacioExprContext):
        pass


    # Enter a parse tree produced by gramaticaParser#ReglaTerm.
    def enterReglaTerm(self, ctx:gramaticaParser.ReglaTermContext):
        pass

    # Exit a parse tree produced by gramaticaParser#ReglaTerm.
    def exitReglaTerm(self, ctx:gramaticaParser.ReglaTermContext):
        pass


    # Enter a parse tree produced by gramaticaParser#OpMulDivMod.
    def enterOpMulDivMod(self, ctx:gramaticaParser.OpMulDivModContext):
        pass

    # Exit a parse tree produced by gramaticaParser#OpMulDivMod.
    def exitOpMulDivMod(self, ctx:gramaticaParser.OpMulDivModContext):
        pass


    # Enter a parse tree produced by gramaticaParser#VacioTerm.
    def enterVacioTerm(self, ctx:gramaticaParser.VacioTermContext):
        pass

    # Exit a parse tree produced by gramaticaParser#VacioTerm.
    def exitVacioTerm(self, ctx:gramaticaParser.VacioTermContext):
        pass


    # Enter a parse tree produced by gramaticaParser#FuncionTrig.
    def enterFuncionTrig(self, ctx:gramaticaParser.FuncionTrigContext):
        pass

    # Exit a parse tree produced by gramaticaParser#FuncionTrig.
    def exitFuncionTrig(self, ctx:gramaticaParser.FuncionTrigContext):
        pass


    # Enter a parse tree produced by gramaticaParser#Variable.
    def enterVariable(self, ctx:gramaticaParser.VariableContext):
        pass

    # Exit a parse tree produced by gramaticaParser#Variable.
    def exitVariable(self, ctx:gramaticaParser.VariableContext):
        pass


    # Enter a parse tree produced by gramaticaParser#Numero.
    def enterNumero(self, ctx:gramaticaParser.NumeroContext):
        pass

    # Exit a parse tree produced by gramaticaParser#Numero.
    def exitNumero(self, ctx:gramaticaParser.NumeroContext):
        pass


    # Enter a parse tree produced by gramaticaParser#Parentesis.
    def enterParentesis(self, ctx:gramaticaParser.ParentesisContext):
        pass

    # Exit a parse tree produced by gramaticaParser#Parentesis.
    def exitParentesis(self, ctx:gramaticaParser.ParentesisContext):
        pass


    # Enter a parse tree produced by gramaticaParser#Unario.
    def enterUnario(self, ctx:gramaticaParser.UnarioContext):
        pass

    # Exit a parse tree produced by gramaticaParser#Unario.
    def exitUnario(self, ctx:gramaticaParser.UnarioContext):
        pass



del gramaticaParser
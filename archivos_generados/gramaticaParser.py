# Generated from gramatica.g4 by ANTLR 4.13.2
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
        4,1,15,67,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,4,0,16,8,0,11,0,12,0,17,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,3,1,30,8,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,3,3,40,8,3,1,4,
        1,4,1,4,1,5,1,5,1,5,1,5,1,5,3,5,50,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,65,8,6,1,6,0,0,7,0,2,4,6,8,10,12,0,
        2,1,0,3,4,1,0,5,7,67,0,15,1,0,0,0,2,29,1,0,0,0,4,31,1,0,0,0,6,39,
        1,0,0,0,8,41,1,0,0,0,10,49,1,0,0,0,12,64,1,0,0,0,14,16,3,2,1,0,15,
        14,1,0,0,0,16,17,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,19,1,0,0,
        0,19,20,5,0,0,1,20,1,1,0,0,0,21,22,5,11,0,0,22,23,5,1,0,0,23,24,
        3,4,2,0,24,25,5,2,0,0,25,30,1,0,0,0,26,27,3,4,2,0,27,28,5,2,0,0,
        28,30,1,0,0,0,29,21,1,0,0,0,29,26,1,0,0,0,30,3,1,0,0,0,31,32,3,8,
        4,0,32,33,3,6,3,0,33,5,1,0,0,0,34,35,7,0,0,0,35,36,3,8,4,0,36,37,
        3,6,3,0,37,40,1,0,0,0,38,40,1,0,0,0,39,34,1,0,0,0,39,38,1,0,0,0,
        40,7,1,0,0,0,41,42,3,12,6,0,42,43,3,10,5,0,43,9,1,0,0,0,44,45,7,
        1,0,0,45,46,3,12,6,0,46,47,3,10,5,0,47,50,1,0,0,0,48,50,1,0,0,0,
        49,44,1,0,0,0,49,48,1,0,0,0,50,11,1,0,0,0,51,52,5,10,0,0,52,53,5,
        8,0,0,53,54,3,4,2,0,54,55,5,9,0,0,55,65,1,0,0,0,56,65,5,11,0,0,57,
        65,5,12,0,0,58,59,5,8,0,0,59,60,3,4,2,0,60,61,5,9,0,0,61,65,1,0,
        0,0,62,63,7,0,0,0,63,65,3,12,6,0,64,51,1,0,0,0,64,56,1,0,0,0,64,
        57,1,0,0,0,64,58,1,0,0,0,64,62,1,0,0,0,65,13,1,0,0,0,5,17,29,39,
        49,64
    ]

class gramaticaParser ( Parser ):

    grammarFileName = "gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "';'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "FUNC", "ID", "NUM", "WS", 
                      "LINE_COMMENT", "BLOCK_COMMENT" ]

    RULE_program = 0
    RULE_stat = 1
    RULE_expr = 2
    RULE_expr_prima = 3
    RULE_term = 4
    RULE_term_prima = 5
    RULE_factor = 6

    ruleNames =  [ "program", "stat", "expr", "expr_prima", "term", "term_prima", 
                   "factor" ]

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
    FUNC=10
    ID=11
    NUM=12
    WS=13
    LINE_COMMENT=14
    BLOCK_COMMENT=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_program

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ProgramaContext(ProgramContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.ProgramContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def EOF(self):
            return self.getToken(gramaticaParser.EOF, 0)
        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.StatContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.StatContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)



    def program(self):

        localctx = gramaticaParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            localctx = gramaticaParser.ProgramaContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.stat()
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 7448) != 0)):
                    break

            self.state = 19
            self.match(gramaticaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AsignacionContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(gramaticaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)


    class SentenciaExprContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(gramaticaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentenciaExpr" ):
                listener.enterSentenciaExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentenciaExpr" ):
                listener.exitSentenciaExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentenciaExpr" ):
                return visitor.visitSentenciaExpr(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = gramaticaParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 29
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = gramaticaParser.AsignacionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.match(gramaticaParser.ID)
                self.state = 22
                self.match(gramaticaParser.T__0)
                self.state = 23
                self.expr()
                self.state = 24
                self.match(gramaticaParser.T__1)
                pass

            elif la_ == 2:
                localctx = gramaticaParser.SentenciaExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.expr()
                self.state = 27
                self.match(gramaticaParser.T__1)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ReglaExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(gramaticaParser.TermContext,0)

        def expr_prima(self):
            return self.getTypedRuleContext(gramaticaParser.Expr_primaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReglaExpr" ):
                listener.enterReglaExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReglaExpr" ):
                listener.exitReglaExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReglaExpr" ):
                return visitor.visitReglaExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = gramaticaParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expr)
        try:
            localctx = gramaticaParser.ReglaExprContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.term()
            self.state = 32
            self.expr_prima()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_primaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_expr_prima

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class VacioExprContext(Expr_primaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.Expr_primaContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVacioExpr" ):
                listener.enterVacioExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVacioExpr" ):
                listener.exitVacioExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVacioExpr" ):
                return visitor.visitVacioExpr(self)
            else:
                return visitor.visitChildren(self)


    class OpSumaRestaContext(Expr_primaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.Expr_primaContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(gramaticaParser.TermContext,0)

        def expr_prima(self):
            return self.getTypedRuleContext(gramaticaParser.Expr_primaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpSumaResta" ):
                listener.enterOpSumaResta(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpSumaResta" ):
                listener.exitOpSumaResta(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpSumaResta" ):
                return visitor.visitOpSumaResta(self)
            else:
                return visitor.visitChildren(self)



    def expr_prima(self):

        localctx = gramaticaParser.Expr_primaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expr_prima)
        self._la = 0 # Token type
        try:
            self.state = 39
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4]:
                localctx = gramaticaParser.OpSumaRestaContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==3 or _la==4):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 35
                self.term()
                self.state = 36
                self.expr_prima()
                pass
            elif token in [2, 9]:
                localctx = gramaticaParser.VacioExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ReglaTermContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(gramaticaParser.FactorContext,0)

        def term_prima(self):
            return self.getTypedRuleContext(gramaticaParser.Term_primaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReglaTerm" ):
                listener.enterReglaTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReglaTerm" ):
                listener.exitReglaTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReglaTerm" ):
                return visitor.visitReglaTerm(self)
            else:
                return visitor.visitChildren(self)



    def term(self):

        localctx = gramaticaParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_term)
        try:
            localctx = gramaticaParser.ReglaTermContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.factor()
            self.state = 42
            self.term_prima()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Term_primaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_term_prima

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class VacioTermContext(Term_primaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.Term_primaContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVacioTerm" ):
                listener.enterVacioTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVacioTerm" ):
                listener.exitVacioTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVacioTerm" ):
                return visitor.visitVacioTerm(self)
            else:
                return visitor.visitChildren(self)


    class OpMulDivModContext(Term_primaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.Term_primaContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(gramaticaParser.FactorContext,0)

        def term_prima(self):
            return self.getTypedRuleContext(gramaticaParser.Term_primaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpMulDivMod" ):
                listener.enterOpMulDivMod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpMulDivMod" ):
                listener.exitOpMulDivMod(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpMulDivMod" ):
                return visitor.visitOpMulDivMod(self)
            else:
                return visitor.visitChildren(self)



    def term_prima(self):

        localctx = gramaticaParser.Term_primaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_term_prima)
        self._la = 0 # Token type
        try:
            self.state = 49
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 6, 7]:
                localctx = gramaticaParser.OpMulDivModContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 224) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 45
                self.factor()
                self.state = 46
                self.term_prima()
                pass
            elif token in [2, 3, 4, 9]:
                localctx = gramaticaParser.VacioTermContext(self, localctx)
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_factor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NumeroContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(gramaticaParser.NUM, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumero" ):
                listener.enterNumero(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumero" ):
                listener.exitNumero(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumero" ):
                return visitor.visitNumero(self)
            else:
                return visitor.visitChildren(self)


    class FuncionTrigContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FUNC(self):
            return self.getToken(gramaticaParser.FUNC, 0)
        def expr(self):
            return self.getTypedRuleContext(gramaticaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncionTrig" ):
                listener.enterFuncionTrig(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncionTrig" ):
                listener.exitFuncionTrig(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncionTrig" ):
                return visitor.visitFuncionTrig(self)
            else:
                return visitor.visitChildren(self)


    class VariableContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)


    class ParentesisContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(gramaticaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParentesis" ):
                listener.enterParentesis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParentesis" ):
                listener.exitParentesis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentesis" ):
                return visitor.visitParentesis(self)
            else:
                return visitor.visitChildren(self)


    class UnarioContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.FactorContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(gramaticaParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnario" ):
                listener.enterUnario(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnario" ):
                listener.exitUnario(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnario" ):
                return visitor.visitUnario(self)
            else:
                return visitor.visitChildren(self)



    def factor(self):

        localctx = gramaticaParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 64
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                localctx = gramaticaParser.FuncionTrigContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.match(gramaticaParser.FUNC)
                self.state = 52
                self.match(gramaticaParser.T__7)
                self.state = 53
                self.expr()
                self.state = 54
                self.match(gramaticaParser.T__8)
                pass
            elif token in [11]:
                localctx = gramaticaParser.VariableContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.match(gramaticaParser.ID)
                pass
            elif token in [12]:
                localctx = gramaticaParser.NumeroContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 57
                self.match(gramaticaParser.NUM)
                pass
            elif token in [8]:
                localctx = gramaticaParser.ParentesisContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 58
                self.match(gramaticaParser.T__7)
                self.state = 59
                self.expr()
                self.state = 60
                self.match(gramaticaParser.T__8)
                pass
            elif token in [3, 4]:
                localctx = gramaticaParser.UnarioContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 62
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==3 or _la==4):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 63
                self.factor()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






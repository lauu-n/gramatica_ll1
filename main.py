import os
import sys

directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_generados = os.path.join(directorio_actual, "archivos_generados")
if ruta_generados not in sys.path:
    sys.path.insert(0, ruta_generados)

from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from eval_visitor import EvalVisitor
from gramaticaLexer import gramaticaLexer
from gramaticaParser import gramaticaParser
from analizador_ll1 import guardar_conjuntos

class ErrorCollector(ErrorListener):
    def __init__(self, etapa="Sintáctico"):
        super().__init__()
        self.etapa = etapa
        self.errores = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        simbolo = f" cerca de '{offendingSymbol.text}'" if offendingSymbol is not None and offendingSymbol.text else ""
        self.errores.append(f"Error {self.etapa} [Línea {line}, Columna {column}]: {msg}{simbolo}")

    def tiene_errores(self):
        return len(self.errores) > 0

def ejecutar_archivo(archivo_path):
    if not os.path.exists(archivo_path):
        print(f"Error: El archivo '{archivo_path}' no existe.")
        sys.exit(1)

    # Guarda los conjuntos en la carpeta conjuntos
    guardar_conjuntos(archivo_path)

    with open(archivo_path, "r", encoding="utf-8") as f:
        contenido = f.read()

    # Muestra exactamente lo que hay dentro del archivo txt
    print(contenido.strip())

    # Dos saltos de línea para separar el contenido de los resultados
    print("\n")

    input_stream = InputStream(contenido)
    
    # Análisis Léxico
    lexer = gramaticaLexer(input_stream)
    lexer_listener = ErrorCollector("Léxico")
    lexer.removeErrorListeners()
    lexer.addErrorListener(lexer_listener)

    stream = CommonTokenStream(lexer)
    stream.fill()

    if lexer_listener.tiene_errores():
        for err in lexer_listener.errores:
            print(err)
        return False

    # Análisis Sintáctico
    parser = gramaticaParser(stream)
    parser_listener = ErrorCollector("Sintáctico")
    parser.removeErrorListeners()
    parser.addErrorListener(parser_listener)

    tree = parser.program()

    if parser_listener.tiene_errores():
        for err in parser_listener.errores:
            print(err)
        return False

    # Análisis Semántico y Evaluación
    visitor = EvalVisitor()
    try:
        visitor.visit(tree)
        return True
    except Exception as e:
        print(e)
        return False

def main():
    if len(sys.argv) < 2:
        print("Uso: python3 main.py <ruta_del_archivo>")
        sys.exit(1)

    archivo = sys.argv[1]
    ejecutar_archivo(archivo)

if __name__ == "__main__":
    main()
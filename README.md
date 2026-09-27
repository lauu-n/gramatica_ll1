# Gramática LL(1) - Analizador Sintáctico

## 🎯 ¿Qué es?

**Gramática LL(1)** es un analizador sintáctico y semántico implementado en Python que utiliza la metodología **LL(1)** (Left-to-right, Leftmost derivation, 1 lookahead token) para procesar un lenguaje de expresiones matemáticas.

El proyecto implementa un compilador completo con tres etapas de análisis:
- **Análisis Léxico**: Tokenización del código fuente
- **Análisis Sintáctico**: Validación de la estructura gramatical
- **Análisis Semántico**: Evaluación y ejecución de expresiones

---

## 🚀 ¿Qué hace?

El analizador permite:

1. **Procesar código fuente** con asignaciones de variables y expresiones matemáticas
2. **Calcular operaciones** con suma, resta, multiplicación, división y módulo
3. **Evaluar funciones trigonométricas** (sin, cos, tan) y matemáticas (abs)
4. **Validar errores** en las tres fases del análisis
5. **Generar conjuntos analíticos**: FIRST, FOLLOW y PREDICT/SELECT

### Ejemplo de código soportado:

```
x = 5 + 3;
y = x * 2;
sin(3.14159);
(10 + 20) / 5;
```

---

## 📁 Estructura del Directorio

```
gramatica_ll1/
│
├── main.py                      # Punto de entrada principal
├── analizador_ll1.py            # Cálculo de conjuntos FIRST, FOLLOW y PREDICT
├── eval_visitor.py              # Evaluador semántico del árbol de análisis
│
├── archivos_generados/          # Archivos generados automáticamente por ANTLR
│   ├── gramaticaLexer.py
│   ├── gramaticaParser.py
│   ├── gramaticaVisitor.py
│   └── (otros archivos ANTLR)
│
├── conjuntos/                   # Conjuntos analíticos generados
│   ├── conjuntos.txt            # Conjuntos generales
│   └── conjuntos_*.txt          # Conjuntos específicos por archivo
│
├── gramatica/                   # Definición de la gramática ANTLR
│   └── gramatica.g4             # Reglas de la gramática LL(1)
│
├── pruebas/                     # Archivos de prueba
│   └── (archivos de ejemplo)
│
└── README.md                    # Este archivo
```

---

## 🔧 Cómo Ejecutarlo

### Requisitos

- Python 3.8 o superior
- ANTLR4 (para Python)

### Instalación

1. **Clonar el repositorio:**
```bash
git clone https://github.com/lauu-n/gramatica_ll1.git
cd gramatica_ll1
```

2. **Crear un entorno virtual (opcional pero recomendado):**
```bash
python3 -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
```

3. **Instalar dependencias:**
```bash
pip install antlr4-python3-runtime
```

### Uso

**Ejecutar el analizador sobre un archivo:**

```bash
python3 main.py <ruta_del_archivo.txt>
```

**Ejemplo:**

```bash
python3 main.py pruebas/ejemplo.txt
```

El programa mostrará:
1. El contenido del archivo
2. Errores léxicos, sintácticos o semánticos (si los hay)
3. Resultados de las evaluaciones
4. Archivos generados en `conjuntos/`

---

## 📄 Explicación de Cada Archivo

### **main.py**
Punto de entrada del programa. Realiza:
- Carga del archivo de entrada
- Coordinación de las tres etapas de análisis
- Recolección y presentación de errores
- Llamada a la función `guardar_conjuntos()` para generar archivos analíticos

**Flujo:**
```
1. Lee el archivo → 2. Análisis Léxico → 3. Análisis Sintáctico → 
4. Análisis Semántico → 5. Genera conjuntos
```

### **analizador_ll1.py**
Módulo de análisis LL(1) que calcula:

- **FIRST (Primeros)**: Conjunto de terminales que pueden aparecer al inicio de cada no-terminal
- **FOLLOW (Siguientes)**: Conjunto de terminales que pueden seguir a cada no-terminal
- **PREDICT/SELECT (Predicción)**: Utilizado para la tabla de análisis sintáctico

Define la gramática LL(1) con:
- 8 no-terminales: `Program, StatList, Stat, Expr, ExprPrima, Term, TermPrima, Factor`
- 13 terminales: `ID, NUM, FUNC, +, -, *, /, %, (, ), ;, $`
- 18 producciones gramaticales

**Funciones principales:**
- `calcular_primeros()`: Calcula conjuntos FIRST
- `calcular_siguientes()`: Calcula conjuntos FOLLOW
- `calcular_prediccion()`: Calcula conjuntos PREDICT
- `guardar_conjuntos()`: Almacena los conjuntos en archivos de texto

### **eval_visitor.py**
Evaluador semántico del árbol de análisis (AST). Implementa el patrón **Visitor** para:

- Procesar asignaciones de variables
- Evaluar expresiones matemáticas con precedencia correcta
- Ejecutar funciones matemáticas
- Manejo de errores semánticos

**Métodos principales:**
- `visitAsignacion()`: Procesa `ID = expr;`
- `visitReglaExpr()`: Procesa suma y resta con asociatividad izquierda
- `visitReglaTerm()`: Procesa multiplicación, división y módulo
- `visitFuncionTrig()`: Ejecuta funciones (sin, cos, tan, abs)
- `visitVariable()`: Resuelve referencias a variables
- `visitNumero()`: Convierte tokens numéricos

---

## 📊 Gramática LL(1)

La gramática define un lenguaje de expresiones matemáticas:

```
Program     → StatList
StatList    → Stat StatList | ε
Stat        → ID '=' Expr ';' | Expr ';'
Expr        → Term ExprPrima
ExprPrima   → '+' Term ExprPrima | '-' Term ExprPrima | ε
Term        → Factor TermPrima
TermPrima   → '*' Factor TermPrima | '/' Factor TermPrima | '%' Factor TermPrima | ε
Factor      → FUNC '(' Expr ')' | ID | NUM | '(' Expr ')'
```

---

## ⚙️ Errores Detectados

El analizador detecta y reporta tres tipos de errores:

### 1. **Errores Léxicos**
Tokens no reconocidos:
```
Error Léxico [Línea X, Columna Y]: Unexpected character
```

### 2. **Errores Sintácticos**
Estructura incorrecta:
```
Error Sintáctico [Línea X, Columna Y]: mismatched input...
```

### 3. **Errores Semánticos**
- División por cero
- Módulo por cero
- Función tangente indefinida (asíntotas)
- Variables no declaradas
- Funciones no soportadas

```
Error Semántico [Línea X]: La variable 'x' no está definida.
```

---

## 📝 Ejemplo de Uso Completo

**Archivo de entrada** (`pruebas/ejemplo.txt`):
```
x = 10;
y = 5;
x + y;
sin(0);
x / y;
```

**Ejecución:**
```bash
python3 main.py pruebas/ejemplo.txt
```

**Salida esperada:**
```
x = 10;
y = 5;
x + y;
sin(0);
x / y;

x = 10
y = 5
Resultado: 15
Resultado: 0.0
Resultado: 2.0
```

**Archivos generados** en `conjuntos/`:
- `conjuntos.txt`: Conjuntos FIRST, FOLLOW y PREDICT
- `conjuntos_ejemplo.txt`: Conjuntos específicos para el archivo procesado

---

## 🔍 Tecnologías Utilizadas

- **Python 3.x**: Lenguaje de programación principal
- **ANTLR4**: Framework para generación de analizadores léxicos y sintácticos
- **Patrón Visitor**: Para traversal y evaluación del AST

---

## 📚 Conceptos LL(1)

**LL(1)** significa:
- **L**: Left-to-right (lectura de izquierda a derecha)
- **L**: Leftmost derivation (derivación por la izquierda)
- **1**: 1 token de lookahead (se examina solo el siguiente token)

Esta metodología garantiza parsing determinístico sin backtracking.

---

## 📄 Licencia

Sin licencia especificada (repositorio público)

---

## 👤 Autor

**lauu-n**

---

## 📞 Soporte

Para reportar errores o sugerencias, abre un issue en el repositorio.

---

**Última actualización**: Septiembre 2026

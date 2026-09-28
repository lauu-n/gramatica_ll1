# Gramática LL(1) - Analizador Sintáctico

---

## ¿Qué es?

Analizador sintáctico y semántico en Python que utiliza la metodología **LL(1)** (Left-to-right, Leftmost derivation, 1 lookahead token) para procesar un lenguaje de expresiones.

Se implementa un compilador completo con tres etapas de análisis:
- **Análisis Léxico**: Tokenización del código fuente
- **Análisis Sintáctico**: Validación de la estructura gramatical
- **Análisis Semántico**: Evaluación y ejecución de expresiones

---

## ¿Qué hace?

El analizador:

1. **Procesa código** con asignaciones de variables y expresiones matemáticas
2. **Calcula operaciones** con suma, resta, multiplicación, división y módulo
3. **Evalúa funciones** como *sin, cos, tan, abs*
4. **Valida errores** en las tres fases
5. **Genera conjuntos **: PRIMERO, SIGUIENTE y PREDICT

### Ejemplo de código soportado:

```
x = 5 + 3;
y = x * 2;
sin(3.14159);
(10 + 20) / 5;
```

---

## Directorio

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

## Ejecución

### Requisitos

- Python 3.8 o superior
- ANTLR4 (para Python)

### Instalación

1. **Clonar el repositorio:**
```bash
git clone https://github.com/lauu-n/gramatica_ll1.git
cd gramatica_ll1
```

2. **Crear un entorno virtual:**
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
python3 main.py pruebas/prueba.txt
```

Se mostrará:
1. Contenido del archivo
2. Errores léxicos, sintácticos o semánticos
3. Resultados
4. Archivos generados en `conjuntos/`

<img width="1130" height="720" alt="image" src="https://github.com/user-attachments/assets/73e0df0c-7305-4192-a512-a8f45fbbb06b" />

```
(venv) laun@Nino-Rosas:~/LENGUAJES_P_T/gramatica_ll1$ python3 main.py pruebas/prueba.txt
// 1. Asignacion de variables
x = 10.5;
y = 2.5;

// 2. Operaciones aritmeticas (+, -, *, /, %)
suma = x + y;
resta = x - y;
mult = x * y;
div = x / y;
mod = 17 % 5;

// 3. Sentencias de expresion (imprimir variables)
suma;
resta;
mult;
div;
mod;

// 4. Operador de valor absoluto (abs) y signo unario negativo (-)
val_negativo = -42.8;
val_absoluto = abs(val_negativo);
val_absoluto;

// 5. Funciones trigonometricas: sin, cos, tan
pi = 3.141592653589793;
angulo = pi / 2;
resultado_seno = sin(angulo);
resultado_cos = cos(0);
resultado_tan = tan(0);

resultado_seno;
resultado_cos;
resultado_tan;

// 6. Expresion combinada (precedencia, parentesis, modulo y abs)
z = abs(-5) * 4 + sin(pi / 6) - (10 % 4) / 2;
z;


x = 10.5
y = 2.5
suma = 13.0
resta = 8.0
mult = 26.25
div = 4.2
mod = 2
Resultado: 13.0
Resultado: 8.0
Resultado: 26.25
Resultado: 4.2
Resultado: 2
val_negativo = -42.8
val_absoluto = 42.8
Resultado: 42.8
pi = 3.141592653589793
angulo = 1.5707963267948966
resultado_seno = 1.0
resultado_cos = 1.0
resultado_tan = 0.0
Resultado: 1.0
Resultado: 1.0
Resultado: 0.0
z = 19.5
Resultado: 19.5
```

---

## Cada archivo

### **main.py**
Punto de entrada del programa. Realiza:
- Carga del archivo de entrada
- Coordina las tres etapas de análisis
- Recolección de errores
- Llamada a la función `guardar_conjuntos()` para generar archivos analíticos

**Flujo:**
```
1. Lee el archivo
→
2. Análisis Léxico
→
3. Análisis Sintáctico
→ 
4. Análisis Semántico
→
5. Genera conjuntos
```

### **analizador_ll1.py**
Módulo LL(1) que calcula:

- **PRIMEROS**: Conjunto de terminales que pueden aparecer al inicio de cada no-terminal
- **SIGUIENTES**: Conjunto de terminales que pueden seguir a cada no-terminal
- **PREDICT**: Utilizado para la tabla de análisis sintáctico

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

## Gramática LL(1)

Define un lenguaje de expresiones matemáticas:

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

## Errores

Detecta y reporta tres tipos de errores:

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

## Ejemplo de uso completo

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

## Conceptos LL(1)

**LL(1)** significa:
- **L**: Left-to-right (lectura de izquierda a derecha)
- **L**: Leftmost derivation (derivación por la izquierda)
- **1**: 1 token de lookahead (se examina solo el siguiente token)

---

## Integrantes
- David Avendaño
- Brayan Paredes
- Laura Niño

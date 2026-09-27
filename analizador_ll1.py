"""
Módulo analizador_ll1.py
Calcula y almacena los conjuntos de:
- Primeros (FIRST)
- Siguientes (FOLLOW)
- Predicción (PREDICT / SELECT)
"""

import os

NON_TERMINALS = [
    'Program',
    'StatList',
    'Stat',
    'Expr',
    'ExprPrima',
    'Term',
    'TermPrima',
    'Factor'
]

TERMINALS = [
    'ID', 'NUM', 'FUNC', '=', '+', '-', '*', '/', '%', '(', ')', ';', '$'
]

PRODUCTIONS = [
    ('Program',   ['StatList']),
    ('StatList',  ['Stat', 'StatList']),
    ('StatList',  ['ε']),
    ('Stat',      ['ID', '=', 'Expr', ';']),
    ('Stat',      ['Expr', ';']),
    ('Expr',      ['Term', 'ExprPrima']),
    ('ExprPrima', ['+', 'Term', 'ExprPrima']),
    ('ExprPrima', ['-', 'Term', 'ExprPrima']),
    ('ExprPrima', ['ε']),
    ('Term',      ['Factor', 'TermPrima']),
    ('TermPrima', ['*', 'Factor', 'TermPrima']),
    ('TermPrima', ['/', 'Factor', 'TermPrima']),
    ('TermPrima', ['%', 'Factor', 'TermPrima']),
    ('TermPrima', ['ε']),
    ('Factor',    ['FUNC', '(', 'Expr', ')']),
    ('Factor',    ['ID']),
    ('Factor',    ['NUM']),
    ('Factor',    ['(', 'Expr', ')']),
]

def first_of_sequence(seq, first_dict):
    res = set()
    for s in seq:
        f = first_dict.get(s, {s})
        res.update(f - {'ε'})
        if 'ε' not in f:
            break
    else:
        res.add('ε')
    return res

def calcular_primeros():
    first = {x: {x} for x in TERMINALS}
    first['ε'] = {'ε'}
    for nt in NON_TERMINALS:
        first[nt] = set()

    changed = True
    while changed:
        changed = False
        for nt, alpha in PRODUCTIONS:
            f_seq = first_of_sequence(alpha, first)
            before = len(first[nt])
            first[nt].update(f_seq)
            if len(first[nt]) > before:
                changed = True
    return first

def calcular_siguientes(first_dict):
    follow = {nt: set() for nt in NON_TERMINALS}
    follow['Program'].add('$')

    changed = True
    while changed:
        changed = False
        for nt, alpha in PRODUCTIONS:
            for i, s in enumerate(alpha):
                if s in NON_TERMINALS:
                    trailer = alpha[i+1:]
                    f_trailer = first_of_sequence(trailer, first_dict)
                    before = len(follow[s])
                    follow[s].update(f_trailer - {'ε'})
                    if 'ε' in f_trailer or len(trailer) == 0:
                        follow[s].update(follow[nt])
                    if len(follow[s]) > before:
                        changed = True
    return follow

def calcular_prediccion(first_dict, follow_dict):
    prediccion = []
    for idx, (nt, alpha) in enumerate(PRODUCTIONS, 1):
        f_alpha = first_of_sequence(alpha, first_dict)
        pred = set(f_alpha - {'ε'})
        if 'ε' in f_alpha:
            pred.update(follow_dict[nt])
        prediccion.append({
            'num': idx,
            'nt': nt,
            'alpha': alpha,
            'pred': pred
        })
    return prediccion

def guardar_conjuntos(archivo_path=None):
    first = calcular_primeros()
    follow = calcular_siguientes(first)
    preds = calcular_prediccion(first, follow)

    carpeta = os.path.join(os.path.dirname(os.path.abspath(__file__)), "conjuntos")
    os.makedirs(carpeta, exist_ok=True)

    dict_primeros = {nt: first[nt] for nt in NON_TERMINALS}
    dict_siguientes = {nt: follow[nt] for nt in NON_TERMINALS}
    dict_prediccion = {p['num']: p['pred'] for p in preds}

    contenido = (
        "primeros:\n"
        f"{dict_primeros}\n\n"
        "siguientes:\n"
        f"{dict_siguientes}\n\n"
        "prediccion:\n"
        f"{dict_prediccion}\n"
    )

    ruta_archivo = os.path.join(carpeta, "conjuntos.txt")
    with open(ruta_archivo, "w", encoding="utf-8") as f:
        f.write(contenido)

    if archivo_path:
        nombre_base = os.path.splitext(os.path.basename(archivo_path))[0]
        ruta_especifica = os.path.join(carpeta, f"conjuntos_{nombre_base}.txt")
        with open(ruta_especifica, "w", encoding="utf-8") as f:
            f.write(contenido)
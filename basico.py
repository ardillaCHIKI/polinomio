

def agregar_termino(polinomio, valor, termino):
    """Agrega un término al polinomio."""
    nuevo_dato = DatoPolinomio(valor, termino)
    nuevo_nodo = Nodo(dato=nuevo_dato)
    
    if polinomio.termino_mayor is None or termino > polinomio.grado:
        nuevo_nodo.siguiente = polinomio.termino_mayor
        polinomio.termino_mayor = nuevo_nodo
        polinomio.grado = termino
    else:
        actual = polinomio.termino_mayor
        anterior = None
        while actual is not None and actual.dato.termino > termino:
            anterior = actual
            actual = actual.siguiente
        if actual is not None and actual.dato.termino == termino:
            actual.dato.valor += valor  # Sumar coeficientes si el término ya existe
        else:
            nuevo_nodo.siguiente = actual
            if anterior is None:
                polinomio.termino_mayor = nuevo_nodo
            else:
                anterior.siguiente = nuevo_nodo

def obtener_valor(polinomio, termino):
    """Obtiene el coeficiente de un término específico del polinomio."""
    actual = polinomio.termino_mayor
    while actual is not None:
        if actual.dato.termino == termino:
            return actual.dato.valor
        actual = actual.siguiente
    return 0  # Si el término no existe, el coeficiente es 0

def modificar_termino(polinomio, valor, termino):
    """Modifica el coeficiente de un término específico del polinomio."""
    actual = polinomio.termino_mayor
    while actual is not None:
        if actual.dato.termino == termino:
            actual.dato.valor = valor
            return
        actual = actual.siguiente
    # Si el término no existe, se agrega como un nuevo término
    agregar_termino(polinomio, valor, termino)

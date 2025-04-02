from typing import Optional
from dataclasses import dataclass
from nodo import Nodo
from DatoPolinomio import DatoPolinomio
class Polinomio:
    def __init__(self):
        self.grado = 0  # Grado del polinomio
        self.termino_mayor = None  # Puntero al término de mayor grado
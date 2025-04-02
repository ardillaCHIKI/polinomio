from polinomio import Polinomio

def sumar(self, otro):
    # Suma dos polinomios
    max_grado = max(len(self.coeficientes), len(otro.coeficientes))
    nuevos_coeficientes = [0] * max_grado
    for i in range(max_grado):
        coef1 = self.coeficientes[i] if i < len(self.coeficientes) else 0
        coef2 = otro.coeficientes[i] if i < len(otro.coeficientes) else 0
        nuevos_coeficientes[i] = coef1 + coef2
    return Polinomio(nuevos_coeficientes)

def multiplicar(self, otro):
    # Multiplica dos polinomios
    grado_resultante = len(self.coeficientes) + len(otro.coeficientes) - 1
    nuevos_coeficientes = [0] * grado_resultante
    for i, coef1 in enumerate(self.coeficientes):
        for j, coef2 in enumerate(otro.coeficientes):
            nuevos_coeficientes[i + j] += coef1 * coef2
    return Polinomio(nuevos_coeficientes)

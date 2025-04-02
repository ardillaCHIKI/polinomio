from lanzador import sumar_polinomios, restar_polinomios, pedir_polinomio

if __name__ == "__main__":
    print("Operaciones con polinomios")
    while True:
        print("\nIngrese los coeficientes de los polinomios separados por espacios.")
        p1 = list(map(int, input("Primer polinomio: ").split()))
        p2 = list(map(int, input("Segundo polinomio: ").split()))

        print("\nSeleccione la operación a realizar:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            print("Resultado de la suma:", sumar_polinomios(p1, p2))
        elif opcion == "2":
            print("Resultado de la resta:", restar_polinomios(p1, p2))
        elif opcion == "3":
            print("Resultado de la multiplicación:", multiplicar_polinomios(p1, p2))
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
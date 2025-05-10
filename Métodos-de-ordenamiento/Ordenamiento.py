import sys
#Método de ordenamiento burbuja
def metodo_burbuja(lista):
    n = len(lista)
    for i in range(n):
      for j in range(0, n - i - 1):
          if lista[j] > lista[j + 1]:
              lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

#Método de ordenamiento por inserción
def metodo_secuencial(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and lista [j] > actual:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual
    return lista

#Método quicksort
def metodo_quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2]
    izquierda = [x for x in lista if x < pivote]
    centro = [x for x in lista if x == pivote]
    derecha = [x for x in lista if x > pivote]
    return metodo_quicksort(izquierda) + centro + metodo_quicksort(derecha)

#Lista del usuario
def ingresar_lista():
    datos = input("ingrese una lista de números separados por ,: ")
    try:
        lista = [(int(x.strip()) for x in datos.split(','))]
        return lista
    except ValueError:
        print("Error: por favor ingrese solo número separados por ,")
        return ingresar_lista()

#Menú de opciones
def menu():
    while True:
        print("\n --Menú de ordenamiento--")
        print("1 Método burbuja")
        print("2 Método de inserción")
        print("3 método quicksort")
        print("4 Salir")

        opcion = input("Seleccione una opción por favor: ")

        if opcion == '1':
            lista = ingresar_lista()
            print("Lista ordenada con burbujas:", metodo_burbuja(lista))

        elif opcion == '2':
            ista = ingresar_lista()
            print("Lista ordenada con inserción: ", metodo_secuencial(lista))

        elif opcion =='3':
            lista = ingresar_lista()
            print("Lista ordenada con quicksort", metodo_quicksort(lista))
            
        elif opcion == '4':
            print("Saliendo del programa")
            sys.exit()
        else:
            print("Esta opción no es válida, intente de nuevo porfavor")

#Ejecuto el programa
if __name__ == '__main__':
    menu()


#Método de ordenamiento burbuja
def metodo_burbuja(lista):
    n = len(lista)
    for i in range(n):
      for j in range(0, n - i - 1):
          if lista[j] > lista[j + 1]:
              lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

#Método de ordenamiento por inserción
def método_secuencial(lista):
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
    if lem(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2]
    izquierda = [x for x in lista if x < pivote]
    centro = [x for x in lista if x == pivote]
    derecha = [x for x in lista if x > pivote]
    return metodo_quicksort(izquierda) + centro + metodo_quicksort(derecha)

#Lista del usuario
def ingresar_lista():
    datos = input("ingrese una lista de números separados por ,: ")
    return ingresar_listas()
except ValueError:
    print("Error: por favor ingrese solo número separados por ,")
    return ingresar_lista()

//Ejercicio Lista Doble de Clientes - Nicolás Rodríguez
//Separé los archivos por clases
class Cliente {
  int cedula;
  String nombre;
  Cliente siguiente;
  Cliente anterior;

  public Cliente(int cedula, String nombre){
    this.cedula=cedula;
    this.nombre=nombre;
    this.siguiente=null;
    this.anterior=null;
  }
}
//Clase que maneja la lista doble
class ListaDoble {
  private Cliente cabeza;
  private Cliente cola;

  //Agregar cliente en la lista
  public void insertarOrden(int cedula, String nombre){
  Cliente nuevo = new Cliente(cedula, nombre);

  if (cabeza == null){
    cabeza = cola = nuevo; //Esta es la lista vacía
  } else if (cedula < cabeza.cedula){
    //agrego al inicio
    nuevo.siguiente = cabeza;
    cabeza.anterior = nuevo;
    cabeza = nuevo;
  } else {
    //agrego en medio o al final de la lista
    Cliente actual = cabeza;
    while (actual.siguiente != null && actual.siguiente.cedula < cedula)
      actual = actual.siguiente;
    
    nuevo.siguiente = actual.siguiente;
    if (actual.siguiente != null) {
      actual.siguiente.anterior = nuevo;
    } else {
      cola = nuevo; //Un nuevo al final
    } 
    actual.siguiente = nuevo;
    nuevo.anterior = actual;
  }
}
//comienzo a listar de principio a fin
public void listarEnDerecha(){
  if (cabeza == null){
    System.out.println("Lista vacía. ");
    return;
}
  Cliente actual = cabeza;
  while (actual != null) {
    System.out.println("Cédula: "+ actual.cedula + ", Nombre: " + actual.nombre);
    actual = actual.siguiente;
  }
}

//Listar de fin a principio
public void listarEnIzquierda() {
  if (cola == null) {
    System.out.println ("Lista vacía");
    return;
  }
  Cliente actual = cola;
  while (actual != null) {
    System.out.println("Cédula: " + actual.cedula + ", Nombre: " + actual.nombre);
    actual = actual.anterior;
  }
  }
}

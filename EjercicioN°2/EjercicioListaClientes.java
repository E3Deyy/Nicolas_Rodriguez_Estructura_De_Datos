//Ejercicio Lista Doble de Clientes - Nicolás Rodríguez

//Crearé la clase Nodo la cual será cliente
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
class listaDoble {
  private Cliente cabeza;
  private Cliente cola;

  //Agregar cliente en la lista
  public void insertarOrden(int cedula, String nombre){
  Cliente nuevo = new Cliente(cedula, nombre);


  }
}

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
  }
}

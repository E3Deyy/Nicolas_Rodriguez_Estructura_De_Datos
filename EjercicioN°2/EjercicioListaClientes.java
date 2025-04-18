//Ejercicio Lista Doble de Clientes - Nicolás Rodríguez

import java.util.Scanner;
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
  }
    nuevo.siguiente = actual.siguiente;
    if (actual.siguiente != null) {
      actual.siguiente.anterior = nuevo;
    } else {
      cola = nuevo; //Un nuevo al final
    } 
    actual.siguiente = nuevo;
    nuevo.anteior = actual;
  }
}
//comienzo a listar de principio a fin
public void listarEnDerecha(){
  if (cabeza == null){
    System.out.prinln("Lista vacía. ");
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
    System.out.prinln ("Lista vacía");
    return;
  }
  Cliente actual = cola;
  While (actual != null) {
    System.out.prinln("Cédula: " + actual.cedula + ", Nombre: " + actual.nombre);
    actual = actual.anterior;
  }
}

//Clase principal con el menú
public class ListasDoblesClientes {
  public static void main(string[] args) {
    Scanner scanner = new Scanner (System.in);
    ListaDoble lista = new ListaDoble();
    int opcion;

    do {
      System.ot.println("/n --Menú--");
      System.ot.println("1. Insertar cliente");
      System.ot.println("2. Listar clientes hacia la derecha");
      System.ot.println("3. Insertar clientes hacia la izquierda");
      System.ot.println("4. Salir");
      System.ot.println("Selecciones una opción por favor: ");
      opcion = scanner.nextInt();
      scanner.nextLine();

      switch (opcion) {
        case 1: 
          System.ot.println("Ingrese cédula: ");
          int cedula = scanner.nextInt();
          scanner.nextLine();
          System.ot.println("Ingrese nombre: ");
          String nombre = scanner.nextLine();
          lista.insertarOrden(cedula, nombre);
          break;
        case 2:
          System.ot.println("Clientrs (inicio -> fin):");
          lista.listarEnDerecha();
          break;
        case 3:
         System.ot.println("Clientrs (fin -> inicio):");
         lista.listarEnIzquierda();
         break;
        case 4:
         System.ot.println("La aplicación finalizó."); 
         break;
        default:
          System.out.println("La opción no es válida");
      }
    }
      while (opcion != 4);
    scanner.close();
  } 
}

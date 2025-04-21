//Separo los archiivos por clases para mejor presentación
import java.util.Scanner;

public class ListasDoblesClientes {
     public static void main(String[] args) {
    Scanner scanner = new Scanner (System.in);
    ListaDoble lista = new ListaDoble();
    int opcion;

    do {
      System.out.println("\n --Menú--");
      System.out.println("1. Insertar cliente");
      System.out.println("2. Listar clientes hacia la derecha");
      System.out.println("3. Insertar clientes hacia la izquierda");
      System.out.println("4. Salir");
      System.out.println("Selecciones una opción por favor: ");
      opcion = scanner.nextInt();
      scanner.nextLine();

      switch (opcion) {
        case 1: 
          System.out.println("Ingrese cédula: ");
          int cedula = scanner.nextInt();
          scanner.nextLine();
          System.out.println("Ingrese nombre: ");
          String nombre = scanner.nextLine();
          lista.insertarOrden(cedula, nombre);
          break;
        case 2:
          System.out.println("Clientes (inicio -> fin):");
          lista.listarEnDerecha();
          break;
        case 3:
         System.out.println("Clientes (fin -> inicio):");
         lista.listarEnIzquierda();
         break;
        case 4:
         System.out.println("La aplicación finalizó."); 
         break;
        default:
          System.out.println("La opción no es válida");
      }
    }
      while (opcion != 4);
    scanner.close();
  } 
}

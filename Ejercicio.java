import java.util.Scanner;

class Cliente {
    String cedula;
    String nombre;

    public Cliente(String c, String n) {
        cedula = c;
        nombre = n;
    }

    public void mostrar() {
        System.out.println("Cédula: " + cedula + ", Nombre: " + nombre);
    }
}

class Nodo {
    Cliente cliente;
    Nodo siguiente;

    public Nodo(Cliente c) {
        cliente = c;
        siguiente = null;
    }
}

class ListaSimple {
    Nodo cabeza;

    public void insertar(Cliente nuevoCliente) {
        Nodo nuevo = new Nodo(nuevoCliente);

        if (cabeza == null || nuevoCliente.cedula.compareTo(cabeza.cliente.cedula) < 0) {
            nuevo.siguiente = cabeza;
            cabeza = nuevo;       } else {
            Nodo actual = cabeza;
            while (actual.siguiente != null &&
                    nuevoCliente.cedula.compareTo(actual.siguiente.cliente.cedula) > 0) {
                actual = actual.siguiente;
          }
            nuevo.siguiente = actual.siguiente;
            actual.siguiente = nuevo;
        }
    }

    public void mostrar() {
        Nodo temp = cabeza;
        while (temp != null) {
            temp.cliente.mostrar();
            temp = temp.siguiente;
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ListaSimple lista = new ListaSimple();
        int opcion = 0;

        while (opcion != 3) {
            System.out.println("------ MENÚ ------");
            System.out.println("1. Insertar cliente");
            System.out.println("2. Listar clientes");
            System.out.println("3. Salir");
            System.out.print("Elija una opción: ");
            opcion = sc.nextInt();
            sc.nextLine(); // limpiar buffer

            if (opcion == 1) {
                System.out.print("Ingrese    cédula:");
                String cedula = sc.nextLine();
                System.out.print("Ingrese nombre: ");
                String nombre = sc.nextLine();
                Cliente c = new Cliente(cedula, nombre);
                lista.insertar(c);
                System.out.println("Cliente insertado.");
           } else if (opcion == 2) {
                System.out.println("Clientes en la lista:");
                lista.mostrar();
           } else if (opcion == 3) {
                System.out.println("Saliendo...");
           } else {
                System.out.println("Opción no válida");
           }
      }
      sc.close();
  }
}
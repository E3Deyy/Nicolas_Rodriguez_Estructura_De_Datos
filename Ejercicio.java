import java.util.Scanner;

// Clase Cliente
class Cliente {
    String cedula;
    String nombre;

    public Cliente(String cedula, String nombre) {
        this.cedula = cedula;
        this.nombre = nombre;
    }

    @Override
    public String toString() {
        return "Cédula: " + cedula + ", Nombre: " + nombre;
    }
}

// Nodo de la lista
class Nodo {
    Cliente cliente;
    Nodo siguiente;

    public Nodo(Cliente cliente) {
        this.cliente = cliente;
        this.siguiente = null;
    }
}

// Lista simple de clientes
class ListaClientes {
    private Nodo cabeza;

    // Insertar de forma ordenada por cédula
    public void insertarOrdenado(Cliente cliente) {
        Nodo nuevo = new Nodo(cliente);

        if (cabeza == null || cliente.cedula.compareTo(cabeza.cliente.cedula) < 0) {
            nuevo.siguiente = cabeza;
            cabeza = nuevo;
        } else {
            Nodo actual = cabeza;
            while (actual.siguiente != null &&
                   actual.siguiente.cliente.cedula.compareTo(cliente.cedula) < 0) {
                actual = actual.siguiente;
            }
            nuevo.siguiente = actual.siguiente;
            actual.siguiente = nuevo;
        }
    }

    // Listar clientes hacia la derecha
    public void listar() {
        Nodo actual = cabeza;
        if (actual == null) {
            System.out.println("Lista vacía.");
        } else {
            while (actual != null) {
                System.out.println(actual.cliente);
                actual = actual.siguiente;
            }
        }
    }
}

// Clase principal con menú
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ListaClientes lista = new ListaClientes();
        int opcion;

        do {
            System.out.println("\n--- MENÚ ---");
            System.out.println("1. Insertar cliente");
            System.out.println("2. Listar clientes hacia la derecha");
            System.out.println("3. Salir");
            System.out.print("Elija una opción: ");
            opcion = sc.nextInt();
            sc.nextLine(); // Limpiar buffer

            switch (opcion) {
                case 1:
                    System.out.print("Ingrese la cédula del cliente: ");
                    String cedula = sc.nextLine();
                    System.out.print("Ingrese el nombre del cliente: ");
                    String nombre = sc.nextLine();
                    lista.insertarOrdenado(new Cliente(cedula, nombre));
                    break;
                case 2:
                    System.out.println("\nClientes en la lista:");
                    lista.listar();
                    break;
                case 3:
                    System.out.println("Saliendo del programa...");
                    break;
                default:
                    System.out.println("Opción inválida.");
            }
        } while (opcion != 3);

        sc.close();
    }
}
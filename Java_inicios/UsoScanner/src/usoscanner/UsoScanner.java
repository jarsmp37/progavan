package usoscanner;
import java.util.Scanner;

public class UsoScanner {
    public static void main(String[] args) {
        Scanner tecleado = new Scanner(System.in);
        // Leer un número entero
        System.out.print("Ingresa tu edad: ");
        int edad = tecleado.nextInt();
        //Leer altura
        System.out.println("Ingresa tu altura en metros: ");
        double altura =tecleado.nextDouble();
        // Limpiar el buffer (necesario después de nextInt o nextDouble)
        tecleado.nextLine();
        //Leer nombre
        System.out.println("Dame tu nombre completo: ");
        String nombre= tecleado.nextLine();
        //Leer la ciudad
        System.out.println("De dónde eres?: ");
        String ciudad= tecleado.next();
        
        // imprimir datos
        System.out.println("\nDatos ingresados:");
        System.out.println("Tu edad es "+ edad + " años");
        System.out.println("Tu altura es "+ altura + " metros");
        System.out.println("Te llamas "+ nombre);
        System.out.println("Eres de: "+ciudad);
        tecleado.close();
                
                
    }
    
}

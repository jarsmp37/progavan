package ejercicio1;
import java.util.Scanner;

public class Ejercicio1 {

    public static void main(String[] args) {
        Scanner leer=new Scanner(System.in);
        System.out.println("Dame tu calificación entre 0 y 10: ");
        int calif= leer.nextInt();
        
        System.out.println("Has entregado todos tus proyectos? (si o no): ");
        String proyecto=leer.next();
        
        System.out.println("Dime el porcentaje de clases asistidas: ");
        double porcentaje= leer.nextDouble();
        
        System.out.println("Tu calificación es: "+ calif);
        System.out.println("Tu respuesta de entregar proyectos es: "+proyecto);
        System.out.println("Tu porcentaje de entregado es: "+porcentaje+"%");
        
        //Para comparar cadenas de texto se pone equals(que quieres que diga)
        
        if (calif>=6 && proyecto.equals("si")9 && porcentaje>=80){
            System.out.println("El estudiante acredito la materia");
        }
            
    }
    
}

package imc;
import java.util.Scanner;
public class IMC {

    public static void main(String[] args) {
        Scanner entrada= new Scanner(System.in);
        System.out.println("Cuál es tu nombre?: ");
        String nombre=entrada.nextLine();
        
        System.out.println("Ingresa tu peso en kilogramos: ");
        int peso=entrada.nextInt();
        
        System.out.println("Ingresa tu altura en metros: ");
        double altura=entrada.nextDouble();
       
        double imc=peso/(altura*altura);
        
        System.out.println(nombre+" tu índice de masa corporal (IMC) es: "+imc);
        System.out.println("El imc es: "+(peso/(altura*altura)));
        entrada.close();
        
    }
    
}

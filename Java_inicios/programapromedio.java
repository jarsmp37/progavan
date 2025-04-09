
import java.util.Scanner;
public class JavaApplication22 {

    public static void main(String[] args) {
        Scanner leer=new Scanner(System.in);
        int[] examenes = new int[4];
        System.out.println("Ingrese las calificaciones de los 4 exámenes: ");
        for(int i=0;i<examenes.length;i++){
            System.out.printf("Dame la calificacion del examen %d: ",i+1);
            examenes[i]=leer.nextInt();
        }
        double sumacalif=0;
        for(int i=0;i<examenes.length;i++){
            sumacalif += examenes[i];
        }
        double promedioexa =sumacalif/examenes.length;
        System.out.printf("La calificación total de examen es: %.2f \n",promedioexa);
        
        int[] practicas = new int[4];
        System.out.println("Ingrese las calificaciones de las 4 prácticas: ");
        for(int i=0;i<practicas.length;i++){
            System.out.printf("Dame la calificacion de la práctica %d: ",i+1);
            practicas[i]=leer.nextInt();
        }
        double sumacalif2=0;
        for(int i=0;i<practicas.length;i++){
            sumacalif2 += practicas[i];
        }
        double promedioprac =sumacalif2/practicas.length;
        System.out.printf("La calificación total de prácticas es: %.2f \n",promedioprac);
        
        int[] proyectos = new int[2];
        System.out.println("Ingrese las calificaciones de los 2 proyectos: ");
        for(int i=0;i<proyectos.length;i++){
            System.out.printf("Dame la calificacion del proyecto %d: ",i+1);
            proyectos[i]=leer.nextInt();
        }
        double sumacalif3=0;
        for(int i=0;i<proyectos.length;i++){
            sumacalif3 += proyectos[i];
        }
        double promedioproy =sumacalif3/proyectos.length;
        System.out.printf("La calificación total de los proyectos es: %.2f \n",promedioproy);
        
        double califfinal=0.3*promedioexa + 0.3*promedioprac +0.4*promedioproy;
        System.out.println("La calificación final es: "+califfinal);
        
        if(califfinal>6){
            System.out.println("Felicidades aprobaste el curso");
        }
        else{
            System.out.println("Te gusto tanto el curso, que lo vas a repetir");
        }
       
    }
    
}

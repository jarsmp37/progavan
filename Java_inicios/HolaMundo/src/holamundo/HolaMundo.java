package holamundo;
public class HolaMundo {
    public static void main(String[] args) {
        // Operadores aritméticos
        int a = 10, b = 5;
        System.out.println("Suma: " + (a + b));
        System.out.println("Resta: " + (a - b));
        System.out.println("Multiplicación: " + (a * b));
        System.out.println("División: " + (a / b));
        System.out.println("Módulo: " + (a % b));

        // Operadores de asignación
        int c = 10;
        c += 5; // Equivalente a c = c + 5
        System.out.println("c += 5: " + c);

        // Operadores de comparación
        System.out.println("a > b: " + (a > b));

        // Operadores lógicos
        boolean x = true, y = false;
        System.out.println("x && y: " + (x && y));

        // Operadores de incremento y decremento
        int d = 10;
        d++; // Incremento
        System.out.println("d++: " + d);

        // Operadores de bits
        int e = 5; // 0101 en binario
        int f = 13; // 0011 en binario
        System.out.println("e & f: " + (e & f)); // AND a nivel de bits
    }
}

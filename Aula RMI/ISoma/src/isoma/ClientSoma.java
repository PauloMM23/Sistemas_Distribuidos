package isoma;

import java.rmi.*;
import java.rmi.server.*;

public class ClientSoma {
    
    public static void main(String args[]) {
        try {
            ISoma c = (ISoma) Naming.lookup("rmi://localhost/Soma");
            float res = (float) c.soma(5.7, 9.3);
            System.out.println("O resultado da soma é " + res);
        } catch (Exception e) {
            System.out.println("Error: " + e);
        }
    }
}

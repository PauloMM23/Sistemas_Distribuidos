package iincrementa;

import java.rmi.*;
import java.rmi.server.*;

public class Client {
    public static void main(String args[]) {
        try {
            IIncrementa c = (IIncrementa) Naming.lookup("rmi://localhost/Incrementa");
            System.out.println("incrementando = " + c.inc(5));
            System.out.println("decrementando = " + c.dec(10));
        } catch (Exception e) {
                System.out.println("Error: " + e);
        }
    }
}

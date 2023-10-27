package iserverstring;

import java.rmi.*;
import java.rmi.server.*;

public class Client {
    public static void main(String args[]) {
        try {
            IServerString c = (IServerString)
            Naming.lookup("rmi://localhost/ServerString");
            int cont = c.contaCaracteres("teste");
            System.out.println("A palavra Teste tem = " + cont + " caracteres");
            
        } catch (Exception e) {
            System.out.println("Error: " + e);
        }
    }
}

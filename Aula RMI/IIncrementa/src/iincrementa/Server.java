package iincrementa;

import java.rmi.*;
import java.rmi.server.*;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class Server {
String HOST_URL = "rmi://localhost/Incrementa";
public Server(){
    try {
            LocateRegistry.createRegistry(Registry.REGISTRY_PORT);
            Incrementa c = new Incrementa();
            Naming.bind(HOST_URL, c);
    } catch (Exception e) {
            System.out.println("Error: " + e);
    }
}
public static void main(String args[]) {
    new Server();
    }
}


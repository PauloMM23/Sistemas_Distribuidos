package iserverstring;

import java.rmi.*;
import java.rmi.server.*;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class Server {
    String HOST_URL = "rmi://localhost/ServerString";
    
    public Server(){
        try {
                LocateRegistry.createRegistry(Registry.REGISTRY_PORT);
                ServerString objetoRemoto = new ServerString();
                Naming.bind(HOST_URL, objetoRemoto);
        }catch (Exception e) {
            System.out.println("Error: " + e);
        }
    }
    public static void main(String args[]) {
    new Server();
    }
}


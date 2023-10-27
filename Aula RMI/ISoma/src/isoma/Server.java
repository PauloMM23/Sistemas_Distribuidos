package isoma;

import java.rmi.*;
import java.rmi.server.*;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class Server {
    String HOST_URL = "rmi://localhost/Soma";
    
    public Server(){
        try {
            LocateRegistry.createRegistry(Registry.REGISTRY_PORT);
            Soma objetoRemoto = new Soma();
            Naming.bind(HOST_URL, objetoRemoto);
        }
        catch (Exception e) {
        }
    }
    
    public static void main(String args[]){
        new Server();
    }
}

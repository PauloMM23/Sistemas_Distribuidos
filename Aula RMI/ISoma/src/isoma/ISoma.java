package isoma;

import java.rmi.*;

public interface ISoma extends Remote {
    public double soma(double a, double b) throws RemoteException;
    
}

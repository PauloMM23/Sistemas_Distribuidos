package isoma;

import java.rmi.*;
import java.rmi.server.*;

public class Soma extends UnicastRemoteObject implements ISoma{

    public Soma() throws RemoteException {
    }

    public double soma(double a, double b) throws RemoteException
    {
        return a+b;
    }
}

package iincrementa;

import java.rmi.*;
import java.rmi.server.*;

public class Incrementa extends UnicastRemoteObject implements IIncrementa{
    public Incrementa() throws RemoteException {
    }
    public int inc(int x) throws RemoteException {
        x++;
        return x;
    }
    public int dec(int x) throws RemoteException {
        x--;
        return x;
    }
}

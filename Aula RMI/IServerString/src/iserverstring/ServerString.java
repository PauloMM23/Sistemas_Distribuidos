package iserverstring;

import java.rmi.*;
import java.rmi.server.*;

public class ServerString extends UnicastRemoteObject implements IServerString{

    public ServerString() throws RemoteException {
    }

    public int contaCaracteres(String s) throws RemoteException
    {
        int cont = s.length();
        return cont;
    }
}


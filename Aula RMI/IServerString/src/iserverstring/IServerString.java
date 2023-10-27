package iserverstring;

import java.rmi.*;

interface IServerString extends Remote {
    
    public int contaCaracteres(String s) throws RemoteException;

} 

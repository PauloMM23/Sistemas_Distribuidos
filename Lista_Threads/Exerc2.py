# 2. Defina uma classe chamada Contador como uma subclasse de Thread, cujo método run() imprime números de 0 a 10 e então crie outra classe, 
# para o processo principal, que instancie duas ou mais threads da classe Contador, e que em seguida inicialize a execução das mesmas.

from threading import Thread # Importa a classe Thread do módulo threading

class Contador: 

    def run(self):
        for i in range(11): # Imprime os números de 0 a 10
            print(i)

contador = Contador() # Instancia a classe Contador

t1 = Thread(target=contador.run)# Instancia a classe Thread
t2 = Thread(target=contador.run)

t1.start()# Inicializa a execução das threads
t2.start()

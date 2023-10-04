# 5. Escreva um programa em que a thread principal (main) deverá ter um loop que a cada ciclo deverá criar uma nova thread, no máximo de 10 threads. 
# Cada thread criada pela main deverá, no método run(), simplesmente suspender sua execução por um tempo aleatório entre 0 e 5 segundos e encerrar. 
# A main deve manter sempre 10 threads em execução, ou seja, nunca acima nem abaixo deste número. 
# Quando alguma thread secundária encerrar sua execução, a main deverá descobrir isso de alguma forma e então criar uma nova thread para manter sempre 10 threads em execução.

from threading import Thread
import random
import time

contador = 0 # contador de threads

def run():
    global contador # variável global para acessar o contador de threads
    print("Thread criada")
    time.sleep(random.randint(1, 5)) # tempo aleatório entre 1 e 5 segundos
    print("Thread encerrada")
    contador -= 1 # decrementa o contador de threads

while True:

    if contador < 10: # se o contador for menor que 10, cria uma nova thread
        contador += 1 # incrementa o contador de threads
        t = Thread(target=run) # cria uma nova thread
        t.start()
        print(contador)

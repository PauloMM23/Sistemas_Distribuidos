# 1. Crie uma classe que estenda a classe Thread chamada ThreadMostraNome cujo método construtor desta classe receba uma String como parâmetro, 
# e então imprima esta String na tela indefinidamente no seu método run(). 
# Em seguida, crie uma outra classe para o processo principal, e então instancie dez threads da classe ThreadMostraNome e colocá-las para execução.

from threading import Thread #importa a classe Thread
import time #importa a classe time

class ThreadMostraNome:

    def __init__(self, nome): #método construtor desta classe receba uma String como parâmetro
        self.nome = nome

    def run(self): #método run() imprima esta String na tela indefinidamente
        while True:
            print(self.nome)
            time.sleep(1) #sleep de 1 segundo

nome = input("Insira um nome: ")
thread = ThreadMostraNome(nome) #instancia a classe ThreadMostraNome

for i in range(10): #instancie dez threads da classe ThreadMostraNome
    t = Thread(target=thread.run) #colocá-las para execução
    t.start() #inicia a thread

# 4. Crie um aplicativo onde o usuário possa escolher a quantidade de threads a serem criadas e colocadas para execução em concorrência, 
# cada uma recebendo um identificador diferente. Ao serem criadas, estas Threads deverão mostrar na tela uma mensagem do tipo “thread [id] criada” e 
# também receber um número randômico N de 0 a 100000 no seu método construtor, e então os seus métodos run() deverão exibir na tela todos os valores de 0 até N. 
# Quando a thread atingir N, ela deverá exibir na tela uma mensagem do tipo “thread [id] entrando em espera” e então entrar em espera (através do método sleep(long millis) ) 
# por um tempo calculado de maneira randômica entre 0 e 5 segundos. Ao término desta espera, a thread deverá mostrar na tela uma mensagem do tipo “thread [id] saindo da espera” 
# e então finalizar sua execução exibindo uma mensagem “execução finalizada”.

from threading import Thread
import random
import time

class NumeroAleatorio:

    def __init__(self, id):
        self.n = random.randint(0, 100000) # Número randômico de 0 a 100000
        self.id = id
        print(f"Thread {self.id} criada!")

    def run(self):

        for i in range(self.n):
            print(i)

        print(f"Thread {self.id} entrando em espera!")
        time.sleep(random.randint(1, 5)) # Espera randômica entre 0 e 5 segundos
        print(f"Thread {self.id} saindo da espera! Execução Finalizada!")

def pegarInputInt(texto):
    val = 0
    while True:
        try:
            val = int(input(texto)) # Pega o input do usuário
            break
        except:
            print("Valor inválido!")
    return val

qtd = pegarInputInt("Quantas Threads gostaria de criar? ")

for i in range(qtd): 
    c = NumeroAleatorio(i)
    t = Thread(target=c.run) # Define o método run da thread
    t.start()

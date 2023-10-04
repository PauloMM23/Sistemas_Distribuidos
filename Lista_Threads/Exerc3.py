# 3. Crie uma aplicação que, na função principal, declare uma matriz de números inteiros de L linhas e C colunas, 
# sendo que estas dimensões são lidas pelo teclado, e então a matriz deve ser preenchida com valores aleatórios. 
# Em seguida, faça com que sejam criadas L threads, cada uma delas responsável por realizar a soma dos elementos de uma linha da matriz. 
# Por exemplo, a Thread 0 faz a soma dos elementos da linha 0, a Thread 1 faz a soma dos elementos da linha 1, e assim por diante.

from threading import Thread
import time
import random

class Soma_Elementos:

    def __init__(self, linha, index):
        self.linha = linha
        self.index = index

    def run(self):

        soma = 0
        for num in self.linha:
            soma += num
        time.sleep(1)
        print(f"Soma da linha {self.index} = {soma}\n")

def pegarInputInt(texto): # Função para pegar input do usuário e validar se é um número inteiro
    val = 0
    while True: 
        try:
            val = int(input(texto)) # Tenta converter o input para inteiro
            break
        except:
            print("Valor inválido!")
    return val

linhas = pegarInputInt("Número de linhas: ")

colunas = pegarInputInt("Número de colunas: ")

matriz = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(random.randint(1, 10)) # Adiciona um número aleatório entre 1 e 10 na linha
    matriz.append(linha)

print()

for linha in matriz:
    print(linha)
print()

for i in range(linhas):
    soma = Soma_Elementos(matriz[i], i) # Cria uma thread para cada linha da matriz
    t = Thread(target=soma.run)
    t.start()

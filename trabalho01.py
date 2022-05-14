#MARIANA DOS SANTOS GASPAR PEREIRA
# MATRICULA: 2021032707


def quicksort(lista1, inicio=0, fim=None):
    if fim is None:
        fim = len(lista1)-1
    if inicio < fim:
        i = particao(lista1, inicio, fim) #retorna posicao do pivo
        quicksort(lista1, inicio, i-1) #organizar elementos da esquerda do pivo
        quicksort(lista1, i+1, fim) #organizar elementos da direita do pivo

def particao(lista1, inicio, fim):
    pivo = lista1[fim] #define ultimo elemento como pivo
    i = inicio 
    for j in range(inicio, fim): 
        if lista1[j] <= pivo: #caso elemento j seja menor que o pivo 
            lista1[j], lista1[i] = lista1[i], lista1[j] # vai para a primeira posicao do inicio
            i = i + 1 #inicio passa a ser a proxima posicao 
    lista1[i], lista1[fim] = lista1[fim], lista1[i] # pivo vai para a posicao depois de seus menores elementos
    return i #retorna posicao do pivo

def bubble_sort(lista2):
    fim = len(lista2)-1
    ordenado = False #impede que o programa continue rodando quando ja estiver ordenado
    while not ordenado:
        ordenado = True
        for i in range(fim):
            if lista2[i] > lista2[i+1]:#compara numeros 
                lista2[i], lista2[i+1] = lista2[i+1],lista2[i] # faz a troca caso o numero da esquerda seja maior
                ordenado = False    
              
import random
import time
lista_aleatoria = [random.randint(1, 20000) for x in range(5000)] #cria 5000 numeros aleatorios 
lista1 = lista_aleatoria #lista para quicksort
lista2 = lista_aleatoria #lista para bubble sort
start = time.time() #contar tempo
quicksort(lista1, inicio=0, fim=None) 
end = time.time()
print(lista1)
print("Tempo utilizado para ordenar em QuickSort:")
print(end - start)

start = time.time() #contar tempo
bubble_sort(lista2)
end = time.time()
print(lista2)
print("Tempo utilizado para ordenar em Bubble Sort:")
print(end - start)
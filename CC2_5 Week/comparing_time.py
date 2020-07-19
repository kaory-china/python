import sorting_class
import time
import random

class CountingTime:
    def random_list(self, n):
        lista = [0 for x in range(n)]
        for i in range(n):
            lista[i] = random.randrange(1000)
        return lista

    def compare(self, n):
        lista1 = self.random_list(n)
        lista2 = lista1[:]

        o = sorting_class.Sorting()

        before = time.time()
        o.bubble_sort(lista1)
        after = time.time()
        print('Bubble Sort took', after - before)

        before = time.time()
        o.selection_sort(lista2)
        after = time.time()
        print('Selection Sort took', after - before)

        

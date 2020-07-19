class Sorting:
    def selection_sort(self, lista):
        # establish lenght of list
        end = len(lista) 

        # initiate loop with first index of the list
        for i in range(end - 1):
            # initially, let`s consider the first index as the minimum value of the list
            min_index = i 

            # initiate a second loop comparing the first index to all others values on the list
            for j in range(i + 1, end):
                # checks if the 'j' value is lower than the current min_index value
                if lista[j] < lista[min_index]:
                    # whenever the compared value is minor to the current minor value, it takes over the min_index variable
                    min_index = j  

            # when second loop is done, the min_index value takes the place of the index 'i' and it goes to the index place of the min_index
            lista[i], lista[min_index] = lista[min_index], lista[i]


    def bubble_sort(self, lista):
        # establish lenght of list
        end = len(lista)

        # starts the first loop by the end up to the first, going one back each loop (-1)
        # it reduces the size of the lenght at each loop since the end becomes the sorted part of the list
        for i in range(end - 1, 0, -1):
            # starts the second loop from the beggining to compare each value to the next one and swapping places whenever the first value is bigger than the next:
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                
                        
    def bubble_sort_optimized(self, lista):
        # establish lenght of list
        end = len(lista)

        # starts the first loop by the end up to the first, going one back each loop (-1)
        # it reduces the size of the lenght at each loop since the end becomes the sorted part of the list
        for i in range(end - 1, 0, -1):
            # if this status doesnt change it means the list is sorted and there is no need o continue the loop
            changed = False
            # starts the second loop from the beggining to compare each value to the next one and swapping places whenever the first value is bigger than the next:
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
        if not changed:
            return


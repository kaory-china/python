# example of using code: print binary_search(my_list, 3)
# list = sorted list given
# item = item to be search in the list 
def binary_search(list, item):
	# every list starts counting at 'zero'
	low = 0
	# ultimo slot da lista, como comeca com 'zero', o total é sempre -1
	# entao se a lista tem 4 itens, 0-1-2-3 (por isso o -1)
	high = len(list) - 1

	# enquanto valor atribuido a 'low' for menor ou igual o slot atribuido a 'high'
	while low <= high:
		# verifico o slot do meio da lista e atribuo este valor a 'mid'
		mid = (low + high) / 2
		# verificar se 'item' é o 'mid'
		guess = list[mid]
		# se for igual, retornar 'mid' que corresponde o slot do 'item'
		if guess == item:
			return mid
		# se for 'guess' for maior que item, vc atualiza o 'high' para mid -1 
		# atualizando o range de procura para a primeira metade da lista
		if guess > item:
			high = mid - 1
		# se 'guess' for menor que item, vc atualiza o 'low' para mid +1 
		# atualizando o range de procura para a segunda metade da lista
		else: 
			low = mid + 1
	# se o item nao estiver na lista, retorna 'none'
	return None

my_list = [1, 3, 5, 7, 9]

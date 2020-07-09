# INSTRUÇÕES PARA USO DE WHILE LOOP
# inicializar as variáveis de controle antes do comando;
# criar uma condição que usa a variável de controle e se mantenha verdadeira pelo número correto de iterações;
# modificar a variável de controle para garantir a terminação; e
# realizar as computações sucessivas para se chegar a resposta correta.

# ENUNCIADO

# Dados um número inteiro n > 0 e as notas finais de n alunos, determinar quantos alunos ficaram de recuperação. 
#Um aluno está de recuperação se sua nota fina está entre 3.0 e 5.0 (exclusive) A nota máxima é 10.0.
# EXERCICIO 5.1 - https://panda.ime.usp.br/aulasPython/static/aulasPython/aula05.html 

# ALGORITMO

# input de numero de alunos
# iniciar variavel sequencia de alunos
# iniciar variavel contagem de alunos em recuperacao
# enquanto variavel "sequencia de alunos" for "numero de alunos"
	# input da primeira nota  
	# se nota for maior que 3 e menor que 5
		# 'variavel contagem de alunos' += 1
		# 'variavel sequencia de alunos' += 1
	# senao
		# 'variavel sequencia de alunos' += 1
# total de alunos em recuperacao e de XXXXC

# CÓDIGO

totalAlunos = int(input("Digite a quantidade de alunos: "))

aluno = 0
contagem = 0

while aluno < totalAlunos:
	nota = float(input("Digite a nota do aluno: "))
	if nota > 3 and nota < 5:
		contagem += 1
		aluno += 1
	else:
		aluno += 1
print("O total de alunos em recuperação é de:", contagem)



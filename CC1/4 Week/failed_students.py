'checks if the students grade is enough for a pass or fail'

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



from datetime import date


def maior18():

  anoAtual = date.today()

  nome = input("Qual o seu nome?")
  aniversario = input("Qual a sua data de aniversário?")

  print("O seu nome é ", nome)
  print("A sua data de aniversário é", aniversario)

  ano = aniversario.split("/")[2]
  mes = aniversario.split("/")[1]
  dia = aniversario.split("/")[0]

  if (2023 - int(ano)) >= 18:
    print("Você é maior de 18 anos.")
  else:
    print("Você não é maior de 18 anos.")
